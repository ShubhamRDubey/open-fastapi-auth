from pydantic import BaseModel
import datetime


class User(BaseModel):
    username: str
    password: str


class TokenData:
    def __init__(self, sub: str, exp: datetime):
        """
        Represents the data extracted from a JWT token.

        Parameters:
        - sub (str): The subject of the token, typically the username.
        - exp (datetime): The expiration time of the token.

        Example:
        >>> token_data = TokenData(sub="testuser", exp=datetime(2023, 12, 31, 12, 0, 0))
        """
        self.sub = sub
        self.exp = exp
