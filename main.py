from fastapi import FastAPI

app = FastAPI()

#root page
@app.get("/")
def read_root() :
    return "welcome to the unity api server"

@app.get("/translate")
async def translate(str : str="") :
    return {"hello":str}