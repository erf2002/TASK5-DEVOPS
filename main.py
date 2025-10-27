from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Hello from FastAPI!", 
        "status": "running",
        "host": os.getenv("HOSTNAME", "unknown")
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "app": "FastAPI"}

@app.get("/info")
async def info():
    return {
        "app_name": "Simple FastAPI App",
        "version": "1.0.0",
        "description": "A simple FastAPI application for Kubernetes deployment"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)