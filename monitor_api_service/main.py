from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()


@app.get("/")
def root():
    return {
       "version": "1.0",
       "message": "Fast, Api",
       "stage": {},
       "data": []
    }