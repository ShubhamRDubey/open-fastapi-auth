# FastAPI JWT Authentication

FastAPI JWT Authentication is a web service built with the FastAPI framework, providing secure user authentication through JSON Web Tokens (JWT).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/open-source-app/open_fastapi_auth.git
    cd open_fastapi_auth
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger documentation.

3. Explore the authentication endpoints and usage examples.

## Dependencies

- [uvicorn](https://www.uvicorn.org/) (Version 0.24.0.post1)
- [bcrypt](https://pypi.org/project/bcrypt/) (Version 4.1.1)
- [cryptography](https://cryptography.io/) (Version 41.0.7)
- [fastapi](https://fastapi.tiangolo.com/) (Version 0.104.1)
- [passlib](https://passlib.readthedocs.io/) (Version 1.7.4)
- [pydantic](https://pydantic-docs.helpmanual.io/) (Version 2.5.2)
- [PyJWT](https://pyjwt.readthedocs.io/) (Version 2.8.0)
- [python-multipart](https://pypi.org/project/python-multipart/) (Version 0.0.6)
- [SQLAlchemy](https://www.sqlalchemy.org/) (Version 2.0.23)
- [starlette](https://www.starlette.io/) (Version 0.27.0)

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

Please ensure your code follows the project's coding standards and includes relevant tests.
## Code Formatting and Linting

This project adheres to code formatting and linting standards for clean and consistent code.

### Code Formatting with `black` and Linting with `Flake8`

I have use [black](https://black.readthedocs.io/) for code formatting.

I have use [flake8](https://flake8.pycqa.org/en/latest/) for code formatting. To test your code, run the following command:

```
flake8 .
```

Feel free to customize the sections based on your application's specific details. This README template provides a starting point for users to understand how to install, use, and contribute to your FastAPI application.

## Todo

### Send Refresh Token with Access Token:
 - Update the authentication endpoint to include the refresh token in the response when generating an access token.
### Get Access Token with Refresh Token:
 - Implement an endpoint to refresh an access token using a valid refresh token.


## Sample Module Docstring

```python
"""Module Name

This module contains functions for handling JWT-based authentication in a FastAPI application.

Functions:
- `create_refresh_token(data: dict, expires_delta: timedelta = REFRESH_TOKEN_EXPIRE_MINUTES) -> str`: Creates a refresh token.
- `create_access_token(data: dict, expires_delta: timedelta = ACCESS_TOKEN_EXPIRE_MINUTES) -> str`: Creates an access token.
- `decode_token(token: str = Depends(oauth2_scheme)) -> TokenData`: Decodes and verifies a JWT token.

Classes:
- `TokenData`: Represents the data extracted from a JWT token.

"""
