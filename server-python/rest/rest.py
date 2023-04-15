from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(
    host='localhost',
    port=6379)


@app.get("/predictions/{id_client}")
async def get_predictions(id_client):
    return r.hgetall(f"predictions:{id_client}")
