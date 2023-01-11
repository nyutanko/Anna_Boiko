from fastapi import FastAPI
from test import Scenario
import config as cfg

if cfg.ACCESS_TOKEN == "":
    print('Set Access token in "config.py" for dropbox')

app = FastAPI()
tester = Scenario(cfg.ACCESS_TOKEN, 'cat.jpg')


@app.get("/")
def read_root():
    return {"Status": 200}


@app.post("/upload_image")
def upload_file():
    return tester.upload()


@app.get("/upload_image/metadata")
def file_get_metadata():
    return tester.get_metadata()


@app.delete("/delete")
def delete_file():
    return tester.delete()
