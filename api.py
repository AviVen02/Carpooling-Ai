"""FastAPI entry point for the React carpooling client."""
import os
from google import genai
from datetime import date
from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
security = HTTPBearer()

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


today = date.today()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)


class ChatRequest(BaseModel):
    message: str


# def get_bearer_token(authorization: str | None) -> str:
#     """Extract a JWT from the standard Authorization header."""
#     if not authorization:
#         raise HTTPException(
#             status_code=401,
#             detail="Missing Authorization header. Send Authorization: Bearer <token>.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

    # scheme, separator, token = authorization.partition(" ")
    # if scheme.lower() != "bearer" or not separator or not token.strip():
    #     raise HTTPException(
    #         status_code=401,
    #         detail="Invalid Authorization header. Expected Bearer <token>.",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    # return token.strip()


@app.get("/")
def home():
    return {"message": "CarPooling AI API is running"}


@app.post("/chat")
def chat(
    request: ChatRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=request.message,
    )

    return {"reply": response.text or "I couldn't generate a response."
    }
