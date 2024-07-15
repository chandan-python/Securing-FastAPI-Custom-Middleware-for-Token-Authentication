import os
from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        ROOT_PATH = os.path.abspath('')
        ENV = os.path.join(ROOT_PATH, '.env')
        load_dotenv(ENV)

    # Retrieve the secret key and algorithm from environment variables
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('ALGORITHM')
