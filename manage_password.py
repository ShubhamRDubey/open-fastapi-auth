from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode, urlsafe_b64decode
import secrets


def hash_password(password: str) -> str:
    """
    Hashes a password using PBKDF2-HMAC-SHA256 with a randomly generated salt.

    Parameters:
    - password (str): The plaintext password to be hashed.

    Returns:
    - str: A string representing the hashed password in the format "salt$hashed_key".

    Example:
    >>> hashed_password = hash_password("my_secure_password")
    """

    salt = urlsafe_b64encode(secrets.token_bytes(16))
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=urlsafe_b64decode(salt),
        iterations=100000,
        length=32,
    )
    key = kdf.derive(password.encode())
    return f"{salt.decode()}${urlsafe_b64encode(key).decode()}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plaintext password matches a given hashed password.

    Parameters:
    - plain_password (str): The plaintext password to be verified.
    - hashed_password (str): The hashed password to compare against, in the format "salt$hashed_key".

    Returns:
    - bool: True if the plaintext password matches the hashed password, False otherwise.

    Example:
    >>> hashed_password = hash_password("my_secure_password")
    >>> verify_password("my_secure_password", hashed_password)
    True
    >>> verify_password("wrong_password", hashed_password)
    False
    """

    salt, key = hashed_password.split("$")
    salt = urlsafe_b64decode(salt)
    key = urlsafe_b64decode(key)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), salt=salt, iterations=100000, length=32)
    new_key = kdf.derive(plain_password.encode())
    return new_key == key
