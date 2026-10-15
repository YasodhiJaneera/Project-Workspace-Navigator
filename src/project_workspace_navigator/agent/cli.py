from pathlib import Path

PROJECT_ROOT = Path.cwd().resolve()


def resolve_safe_path(relative_path: str) -> Path:
    path = (PROJECT_ROOT / relative_path).resolve()
    if path != PROJECT_ROOT and PROJECT_ROOT not in path.parents:
        raise ValueError('Path escapes project workspace.')
    return path