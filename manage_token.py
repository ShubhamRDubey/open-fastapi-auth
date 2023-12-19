from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from manage_models import TokenData
from datetime import datetime, timedelta
from settings import (
    SECRET_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create an access token with the given data and expiration delta.

    Parameters:
    - data (dict): The data to be encoded in the token.
    - expires_delta (timedelta, optional): The expiration delta for the token.
      If not provided, a default delta is used.

    Returns:
    - str: The encoded access token.

    Example:
    >>> token = create_access_token(data={"username": "testuser"})
    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, **data}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create a refresh token with the given data and expiration delta.

    Parameters:
    - data (dict): The data to be encoded in the token.
    - expires_delta (timedelta, optional): The expiration delta for the token.
    If not provided, a default delta is used.

    Returns:
    - str: The encoded refresh token.

    Example:
    >>> token = create_refresh_token(data={"username": "testuser"})
    """
    if expires_delta is None:
        expires_delta = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, **data}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    """
    Decode and verify a JWT token and return the extracted data.

    Parameters:
    - token (str, optional): The JWT token to be decoded.
    Defaults to the value obtained from the "Authorization" header.

    Returns:
    - TokenData: An instance of TokenData containing the decoded token data.

    Raises:
    - HTTPException: If the token is invalid or cannot be decoded.

    Example:
    >>> token_data = decode_token(token="encoded_jwt_token")
    """
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        sub = payload.get("sub")
        exp = payload.get("exp")

        if sub is None or exp is None:
            raise credentials_exception

        if datetime.utcnow() >= datetime.fromtimestamp(exp):
            raise HTTPException(status_code=401, detail="Token has expired")

        return TokenData(sub=sub, exp=exp)

    except jwt.JWTError:
        raise credentials_exception
