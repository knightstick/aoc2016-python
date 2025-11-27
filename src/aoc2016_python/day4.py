import re
from typing import Counter
from aoc2016_python.utils import load_day

test_input = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""


def main():
    data = load_day(4)
    print(str(part_one(data)))
    print(str(part_two(data)))


def part_one(input: str):
    lines = [parse_line(line) for line in input.strip().splitlines()]
    ids = [sector_id for [_, sector_id, _] in real_rooms(lines)]

    return sum(ids)


def part_two(input: str):
    lines = [parse_line(line) for line in input.strip().splitlines()]
    rooms = [(name, sector_id) for name, sector_id, _ in real_rooms(lines)]
    (_, sector_id) = next(
        (decrypted, id)
        for name, id in rooms
        if "north" in (decrypted := decrypt_name(name, id))
    )

    return sector_id


def real_rooms(lines: list[tuple[str, int, str]]) -> list[tuple[str, int, str]]:
    return [
        (encrypted_name, int(id), checksum)
        for [encrypted_name, id, checksum] in lines
        if is_real_room(encrypted_name, checksum)
    ]


def is_real_room(encrypted_name: str, checksum: str) -> bool:
    actual_checksum = calculate_checksum(encrypted_name)

    return actual_checksum == checksum


def calculate_checksum(encrypted_name: str) -> str:
    counter = Counter(encrypted_name)
    by_count_then_letter = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    top5 = by_count_then_letter[:5]
    chars = [letter for letter, _ in top5]

    return "".join(chars)


def parse_line(line: str) -> tuple[str, int, str]:
    ID_AND_CHECKSUM = re.compile(r"(?P<sector_id>.+)\[(?P<checksum>.+)\]")

    [*letters, last] = line.split("-")
    encrypted_name = "".join(letters)

    match = ID_AND_CHECKSUM.fullmatch(last)

    if not match:
        raise ValueError("Invalid format")

    return (encrypted_name, int(match["sector_id"]), match["checksum"])


def decrypt_name(encrypted, id) -> str:
    chars = [rotate(char, id) for char in encrypted]

    return "".join(chars)


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_LENGTH = len(ALPHABET)


def rotate(char, distance) -> str:
    index = ALPHABET.index(char)
    new_index = (index + distance) % ALPHABET_LENGTH

    return ALPHABET[new_index]


if __name__ == "__main__":
    main()
