from typing import NamedTuple

class Arguments(NamedTuple):
    firstname: str
    lastname: str
    age: int = 0

def check_type(obj):
    for attr, value in obj._asdict().items():
        print(
            f"Value: {value}, "
            f"Expected type {obj.__annotations__[attr]} for {attr}, "
            f"got {type(value)}"
        )
        if type(value) != obj.__annotations__[attr]:
            print("Type Error")
        else:
            print("Type Ok")