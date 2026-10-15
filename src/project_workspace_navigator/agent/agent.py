from pydantic_ai import Agent, mcp
import os
from dotenv import load_dotenv
from fastmcp.client.transports import StdioTransport
from pydantic_ai.mcp import MCPToolset

workspace_toolset = MCPToolset(
   StdioTransport(
        command="Python",
        args=["G:/Project_Workspace_Navigator/src/project_workspace_navigator/agent/mcp_server.py"]
    )
)

load_dotenv()


agent = Agent(
    os.environ["GROQ_AGENT_LLM"],
    toolsets=[workspace_toolset]
)
print(agent.run_sync("Can you find the cli.py")) 