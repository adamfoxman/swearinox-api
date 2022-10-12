from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Swearinox API",
        "version": "0.1",
        "motto": "Everything counts in large amounts.",
        }
