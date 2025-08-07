# sha1sum_val.py

from typing import List
import hashlib
import pathlib
import sys
import argparse

def process_file(filename: str) -> bytes:
    return pathlib.Path(filename).read_bytes()

def process_stdin() -> bytes:
    return bytes("".join(sys.stdin), "utf-8")

def sha1sum(data: bytes) -> str:
    m = hashlib.sha1()
    m.update(data)
    return m.hexdigest()

def output_sha1sum(data: bytes, filename: str = "-") -> None:
    print(f"{sha1sum(data)}  {filename}")


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Print or check SHA1 (160-bit) checksums."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('files', nargs='*')
    return parser

def main(argv: List[str]) -> None:
    parser = init_argparse()
    args = parser.parse_args(argv)
    if not args.files:
        output_sha1sum(process_stdin())
    for file in args.files:
        if file == "-":
            output_sha1sum(process_stdin(), "-")
            continue
        try:
            output_sha1sum(process_file(file), file)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1:])