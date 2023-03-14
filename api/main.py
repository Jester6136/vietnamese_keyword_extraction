from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from configparser import ConfigParser
from src.main import Extractor
app = FastAPI()


config = ConfigParser()
config.read('config.ini')
config_default = config['DEFAULT']
extractor = Extractor(config_default)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/extracting")
async def extracting(document:str,num_keywords:int):
    return {"keywords": extractor.run(document,num_keywords)}