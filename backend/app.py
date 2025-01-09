from fastapi import FastAPI
from backend.api.word_routes import word_router

app = FastAPI()

# Include word routes
app.include_router(word_router, prefix="/words", tags=["words"])
