import itertools
from hashlib import md5

from typing import Iterable

test_input = """
abc
"""

real_input = """
cxdnnyjw
"""


def main():
    input = real_input.strip()

    print(part_one(input))
    print(part_two(input))


def part_one(input: str) -> str:
    return "".join(char for char, _ in itertools.islice(hash_stream(input.strip()), 8))


def part_two(input: str) -> str:
    password: list[None | str] = [None] * 8

    for position, char in hash_stream(input.strip()):
        index = parse_int(position)

        if index is not None and index < 8 and password[index] is None:
            password[index] = char

            if all(password):
                break

    return "".join(char for char in password if char is not None)


def make_hash(string: str) -> str:
    return md5(string.encode("utf-8")).hexdigest()


def hash_stream(input: str) -> Iterable[tuple[str, str]]:
    i = 0

    while True:
        [*hashed, six, seven] = make_hash(f"{input}{i}")[:7]
        if "".join(hashed) == "00000":
            yield (six, seven)  # lol

        i += 1


def parse_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


if __name__ == "__main__":
    main()
