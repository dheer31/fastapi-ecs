
import os
from fastapi import FastAPI

# Create the FastAPI application instance
app = FastAPI()


# Main route - returns app status and environment info
@app.get("/")
def home():
    environment = os.environ.get("ENVIRONMENT", "development")

    return {
        "message": "Hello from ECS Fargate!",
        "environment": environment,
        "status": "running"
    }


# Health check endpoint - used by ECS and the load balancer
@app.get("/health")
def health():
    return {"status": "healthy"}


# Run the app using Uvicorn
if __name__ == "__main__":
    import uvicorn

    debug_mode = os.environ.get("ENVIRONMENT", "development") == "development"

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=debug_mode
    )
