from pydantic_ai import Agent, mcp
import os
from dotenv import load_dotenv
from fastmcp.client.transports import StdioTransport
from pydantic_ai.mcp import MCPToolset

load_dotenv()


agent = Agent(
    os.environ["GROQ_AGENT_LLM"]
)
print(agent.run_sync("Hi")) 