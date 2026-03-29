# Import FastAPI tools
from fastapi import Header, HTTPException

# Load environment variables
import os
from dotenv import load_dotenv

load_dotenv()

# Get token from .env
API_TOKEN = os.getenv("API_TOKEN")


# Function to verify token
def verify_token(x_token: str = Header(...)):
    """
    This function checks if the incoming request
    contains the correct API token in headers.
    """

    # Compare provided token with stored token
    if x_token != API_TOKEN:
        # If token is wrong → reject request
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )