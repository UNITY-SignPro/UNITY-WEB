from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root() :
    return "welcome to the unity api server"

@app.get("/translate")
async def translate(str : str="") :
    return {"hello":str}

