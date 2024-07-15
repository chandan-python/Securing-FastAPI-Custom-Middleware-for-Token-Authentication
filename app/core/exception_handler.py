from fastapi import Request, HTTPException, status
import jwt


async def token_expire_response(request: Request, exc: jwt.ExpiredSignatureError):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Token expired")


async def invalid_token_response(request: Request, exc: jwt.InvalidTokenError):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Invalid token")
