from fastapi import FastAPI, HTTPException
import random 


app = FastAPI()

@app.get("/")
async def root():
    return {"example": "This is an exmaple", "data": 0}

@app.get("/random/{limit}")
async def get_random(limit: int):
    rn = random.randint(0, limit)
    return {"number": rn, "limit": limit}

items = []

@app.post("/items")
def create_item(item:str):
    if item == "0":
        raise HTTPException(status_code=404, detail="Not allowed")
    else:
        items.append(item)
        return item
