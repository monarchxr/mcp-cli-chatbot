from mcp.server.fastmcp import FastMCP
from groq import Groq

client = Groq(api_key=None)
mcp = FastMCP("ChatMCP", log_level="ERROR")

# Tool for chatting
@mcp.tool(
    name="chat",
    description="Chat with the user or answer their queries"
)

def chat(message: str)->str:

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user", "content":message}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    mcp.run(transport="stdio")