from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "version": os.getenv("SWEARINOX_API_VERSION"),
        "motto": "Everything counts in large amounts",
        }
