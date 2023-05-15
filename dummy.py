import random
import string

from fastapi import FastAPI

app = FastAPI()

# Sumple FastAPI Server
@app.get('/')
async def index():
    my_str = ''.join(random.choices(string.ascii_lowercase, k=5))
    return {'data': my_str}

# GET Requests endpoint
@app.get('/items/{item_id}')
async def read(item_id: int):
    return {'item_id': item_id}