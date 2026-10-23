from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EWB Student Database CRUD Application",
    description="Python Backend Development Internship Project",
    version="1.0.0",
)

app.include_router(router)


@app.get("/", tags=["Health"])
def home():
    return {
        "message": "Student Database CRUD API is running",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}
