from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("My MCP Server")

PROJECT_ROOT = Path.cwd().resolve()

def resolve_safe_path(relative_path: str) -> Path:
    path = (PROJECT_ROOT / relative_path).resolve()
    if path != PROJECT_ROOT and PROJECT_ROOT not in path.parents:
        raise ValueError('Path escapes project workspace.')
    return path

@mcp.tool()
def list_directory(path: str = '.', max_depth: int = 2) -> list[str]:
    root = resolve_safe_path(path)
    if not root.exists():
        return []

    results: list[str] = []
    base_depth = len(root.parts)
    for item in root.rglob('*'):
        depth = len(item.parts) - base_depth
        if depth <= max_depth:
            results.append(str(item.relative_to(PROJECT_ROOT)))
    return sorted(results)


@mcp.tool()
def search_files(query: str, limit: int = 30) -> list[str]:
    query_lower = query.lower()
    matches: list[str] = []
    for path in PROJECT_ROOT.rglob('*'):
        if not path.is_file():
            continue
        relative = str(path.relative_to(PROJECT_ROOT))
        if query_lower in relative.lower():
            matches.append(relative)
        if len(matches) >= limit:
            break
    return matches

if __name__ == "__main__":
    mcp.run()