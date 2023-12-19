from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from manage_password import hash_password, verify_password
from manage_models import User, TokenData
from manage_database import UserDB, get_db
from manage_token import create_access_token, decode_token


app = FastAPI()
user_route = APIRouter(prefix="/user")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_current_user(decoded_data: TokenData, db: Session, credentials_exception: HTTPException):
    db_user = db.query(UserDB).filter(UserDB.username == decoded_data.sub).first()
    user = {
        "username": db_user.username,
    }
    if user is None:
        raise credentials_exception
    return user


def create_user(db: Session, user_create: User):
    hashed_password = hash_password(user_create.password)
    db_user = UserDB(username=user_create.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@user_route.post("/new")
def add_user(user_create: User, db: Session = Depends(get_db)):
    return create_user(db, user_create)


@user_route.post("/login", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@user_route.get("/me", response_model=dict)
async def read_users_me(decoded_data: TokenData = Depends(decode_token), db: Session = Depends(get_db)):
    exception = HTTPException(
        status_code=401,
        detail="User not found",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_data = get_current_user(decoded_data, db, exception)
    return user_data


app.include_router(user_route)
