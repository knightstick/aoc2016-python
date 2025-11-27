from pathlib import Path


def load_input(path: str) -> str:
    return Path(path).read_text().strip()


def load_day(day: int) -> str:
    file_path = f"data/day{day}.txt"
    return load_input(file_path)


def load_day_lines(day: int) -> list[str]:
    return load_day(day).strip().splitlines()
