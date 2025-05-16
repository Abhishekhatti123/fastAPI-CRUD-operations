from fastapi import FastAPI
from app.routes import router as api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)