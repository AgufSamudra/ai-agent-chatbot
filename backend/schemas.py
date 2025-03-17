from pydantic import BaseModel
from typing import Literal

class Agent(BaseModel):
    input_message = str
    methode = Literal["ollama", "groq"] # choose only one