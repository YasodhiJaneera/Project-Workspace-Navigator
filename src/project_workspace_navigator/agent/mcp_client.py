
import asyncio
from pathlib import Path
from fastmcp import Client

async def main():
    server_path = Path(
        "G:/Project_Workspace_Navigator/src/project_workspace_navigator/agent/mcp_server.py"
    ).resolve()

    print("Server path:", server_path)

    client = Client(server_path)

    async with client:
        print("Connected")

        result = await client.call_tool(
            "search_files",
            {"query": "agent\\cli.py"}
        )
        print("Search results:", result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
