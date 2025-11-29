from dataclasses import dataclass

from aoc2016_python.utils import load_day_lines


@dataclass(frozen=True)
class CharSequence:
    value: str


@dataclass(frozen=True)
class HypernetSequence:
    value: str


Segment = CharSequence | HypernetSequence


def main():
    input = load_day_lines(7)

    assert supports_tls("abba[mnop]qrst")
    assert not supports_tls("abcd[bddb]xyyx")
    assert not supports_tls("aaaa[qwer]tyui")
    assert supports_tls("ioxxoj[asdfgh]zxcvbn")

    print(part_one(input))

    assert supports_ssl("aba[bab]xyz")
    assert not supports_ssl("xyx[xyx]xyx")
    assert supports_ssl("aaa[kek]eke")
    assert supports_ssl("zazbz[bzb]cdb")

    print(part_two(input))


def part_one(input: list[str]) -> int:
    return sum(1 for line in input if supports_tls(line))


def part_two(input: list[str]) -> int:
    return sum(1 for line in input if supports_ssl(line))


def supports_tls(input: str) -> bool:
    parsed = parse(input)
    chars = (elem for elem in parsed if isinstance(elem, CharSequence))
    hypers = (elem for elem in parsed if isinstance(elem, HypernetSequence))

    return any(is_abba(elem.value) for elem in chars) and not any(
        is_abba(elem.value) for elem in hypers
    )


def supports_ssl(input: str) -> bool:
    parsed = parse(input)
    chars = (elem for elem in parsed if isinstance(elem, CharSequence))
    hypers = [elem for elem in parsed if isinstance(elem, HypernetSequence)]
    abas = [aba for seq in chars for aba in find_abas(seq)]

    return any(has_matching_bab(aba, [hyper.value for hyper in hypers]) for aba in abas)


def is_abba(input: str) -> bool:
    match list(input):
        case [a1, b1, b2, a2, *rest]:
            if a1 == a2 and b1 == b2 and not a1 == b1:
                return True
            return is_abba("".join([b1, b2, a2, *rest]))
        case [*_]:
            return False


def find_abas(input: Segment) -> list[str]:
    value = list(input.value)

    def triples(list):
        return zip(list, list[1:], list[2:])

    result = []
    for [a, b, a2] in triples(value):
        if is_aba(a, b, a2):
            result.append("".join([a, b, a2]))

    return result


def is_aba(x, y, z: str) -> bool:
    return x == z and not x == y


def has_matching_bab(aba: str, values: list[str]) -> bool:
    print("aba: ", aba, "hypers: ", repr(values))

    match list(aba):
        case [a, b, _]:
            bab = "".join([b, a, b])
            return any(True for value in values if bab in value)
        case _:
            raise ValueError(f"Invalid aba: {aba}")


def parse(input: str) -> list[Segment]:
    parts = []
    buf = []
    hyper = False

    def flush():
        if buf:
            if hyper:
                parts.append(HypernetSequence("".join(buf)))
            else:
                parts.append(CharSequence("".join(buf)))
            buf.clear()

    for char in input:
        if char == "[":
            if hyper:
                raise ValueError("Nested HypernetSequence not allowed")
            flush()
            hyper = True
        elif char == "]":
            if not hyper:
                raise ValueError("Unmatched ']'")
            flush()
            hyper = False

        else:
            if not ("a" <= char <= "z"):
                raise ValueError(f"Invalid char: {char!r}")
            buf.append(char)

    if hyper:
        raise ValueError("Unclosed HypernetSequence")

    flush()

    return parts


if __name__ == "__main__":
    main()
