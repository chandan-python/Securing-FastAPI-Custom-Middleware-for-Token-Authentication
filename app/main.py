# Import necessary modules from FastAPI
import jwt
from fastapi import FastAPI
from core.middleware import CustomMiddleware
from fastapi.middleware.cors import CORSMiddleware
from core.exception_handler import *


# Create a FastAPI app instance
app = FastAPI()

# Add the custom middleware to the FastAPI app
app.add_middleware(CustomMiddleware)


# Add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handler to catch global level exceptions
app.add_exception_handler(jwt.ExpiredSignatureError, token_expire_response)
app.add_exception_handler(jwt.InvalidTokenError, invalid_token_response)

# Define a route handler for handling requests '
# app.include_router()


# Only for debugging purpose
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9001)
