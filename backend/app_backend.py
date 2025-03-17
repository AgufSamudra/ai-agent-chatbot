from fastapi import FastAPI
from .schemas import Agent

app = FastAPI()

@app.post("/agent")
async def agent(message_input: Agent):
    pass