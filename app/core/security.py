# token_validation.py
import jwt
from core.config import Config

settings = Config()


class Security:
    def __init__(self, request) -> None:
        self.request = request
        self.token = self.get_token_from_request()

    def verify_access_token(self):
        """Function to verify the access token extracted from the request"""
        try:
            # Decode and verify the token using the secret key and algorithm
            payload = jwt.decode(self.token, settings.secret_key,
                                 algorithms=[settings.algorithm])
            return payload
        except Exception as e:
            raise e

    def get_token_from_request(self):
        return self.request.headers.get("Authorization").replace('Bearer ', '')
