import os
import asyncio
from groq import AsyncGroq

client = AsyncGroq(
    api_key=os.environ.get("")
)

async def agent_main(content: str) -> None:
    chat_completion = await client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": content
        }],
        model="llama3-8b-8192",
    )
    
    print(chat_completion.choices[0].message.content)
    
