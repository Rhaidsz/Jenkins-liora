from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": Alles ist super es hat alles super funktioniert, aber Lea checkt noch nicht alles !!"}
