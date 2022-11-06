from fastapi import FastAPI
app = FastAPI()

import time
from pathlib import Path

#root page
@app.get("/")
def read_root() :
    return "welcome to the unity api server"

@app.get("/translate")
async def translate(str : str="") :
    return {"hello":str}

# @app.get("/test")
# def test(str : str="") :
#     time.sleep(3)
#     return {"test":str}

def make_file() :
    Path('newfile.txt').touch()
    while not (Path('filename.txt').is_file) :
        time.sleep(1)

    return "newfile.txt"

make_file()



