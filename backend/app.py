from fastapi import FastAPI
from backend.api.word_routes import word_router
from backend.api.user_routes import user_router

app = FastAPI(
    title="Vocab Platform",
    description="A platform made to help users expand their vocabulary and learn jargon terms.",
    version="1.0.0"
)

# Include routers
app.include_router(word_router, prefix="/words", tags=["Words"])
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vocab Platform"}
