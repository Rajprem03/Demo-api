from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx"
}


IGNORED_DIRECTORIES = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build"
}


def scan_repository(repository_path):
    repository = Path(repository_path)

    files = []

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        if file.suffix not in SUPPORTED_EXTENSIONS:
            continue

        if any(
            folder in file.parts
            for folder in IGNORED_DIRECTORIES
        ):
            continue

        files.append(file)

    return files