# seq_parse.py

from typing import List, Tuple
import collections
import sys

USAGE = (f"Usage: {sys.argv[0]} "
         "[--help] | [-s <sep>] [first [incr]] last")

def seq(operands: List[int], sep: str = "\n") -> str:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    if len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    if len(operands) == 3:
        first, increment, last = operands
    last = last + 1 if increment > 0 else last - 1
    return sep.join(str(i) for i in range(first, last, increment))

def parse(args: List[str]) -> Tuple[str, List[int]]:
    arguments = collections.deque(args)
    separator = "\n"
    operands: List[int] = []
    while arguments:
        arg = arguments.popleft()
        if not len(operands):
            if arg == "--help":
                print(USAGE)
                sys.exit(0)
            if arg in ("-s", "--separator"):
                separator = arguments.popleft() if arguments else "\n"
                continue
        try:
            operands.append(int(arg))
        except ValueError:
            raise SystemExit(USAGE)
        if len(operands) > 3:
            raise SystemExit(USAGE)

    return separator, operands

def main() -> None:
    sep, operands = parse(sys.argv[1:])
    if not operands:
        raise SystemExit(USAGE)
    print(seq(operands, sep))

if __name__ == "__main__":
    main()