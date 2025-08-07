# Print integers from <first> to <last>, in steps of <increment>

# Usage:
#   python seq.py --help
#   python seq.py [-s SEPARATOR] <last>
#   python seq.py [-s SEPARATOR] <first> <last>
#   python seq.py [-s SEPARATOR] <first> <increment> <last>

# Mandatory arguments to long options are mandatory for short options too.
#   -s, --separator=STRING use STRING to separate numbers (default: \n)
#       --help             display this help and exit

# If <first> or <increment> are omitted, they default to 1. When <first> is
# larger than <last>, <increment>, if not set, defaults to -1.
# The sequence of numbers ends when the sum of the current number and
# <increment> reaches the limit imposed by <last>.

import re, sys
from typing import Dict, List

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--seperator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
    """,
    re.VERBOSE
)
arg_line = " ".join(sys.argv[1:])

def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items() if v is not None}
    return args

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

def main() -> None:
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit("USAGE")
    if args.get("HELP"):
        print("USAGE")
        return
    operands = [int(v) for k, v in args.items() if k.startswith("OP")]
    sep = args.get("SEP", "\n")
    print(seq(operands, sep))

if __name__ == "__main__":
    main()