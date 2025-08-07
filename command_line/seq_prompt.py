from typing import List
from prompt_toolkit.shortcuts import button_dialog, input_dialog, message_dialog

def version():
    print("Version 1.0.0")

def help():
    print("Print numbers from FIRST to LAST, in steps of INCREMENT.")

def seq(operands: List[int], sep: str = "\n"):
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    elif len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    elif len(operands) == 3:
        first, increment, last = operands
    last = last - 1 if first > last else last + 1
    print(sep.join(str(i) for i in range(first, last, increment)))

def error_dlg():
    message_dialog(
        title="Error",
        text="Ensure that you enter a number",
    ).run()

def seq_dlg():
    labels = ["FIRST", "INCREMENT", "LAST"]
    operands = []
    while True:
        n = input_dialog(
            title="Sequence",
            text=f"Enter argument {labels[len(operands)]}:",
        ).run()
        if n is None:
            break
        if n.isdigit():
            operands.append(int(n))
        else:
            error_dlg()
        if len(operands) == 3:
            break

    if operands:
        seq(operands)
    else:
        print("Bye")        

actions = {"SEQUENCE": seq_dlg, "HELP": help, "VERSION": version}

def main():
    result = button_dialog(
        title="Sequence",
        text="Select an action:",
        buttons=[
            ("Sequence", "SEQUENCE"),
            ("Help", "HELP"),
            ("Version", "VERSION"),
        ],
    ).run()
    actions.get(result, lambda: print("Unexpected action"))()

if __name__ == "__main__":
    main()