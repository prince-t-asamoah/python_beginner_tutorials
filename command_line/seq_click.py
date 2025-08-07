import click

@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--separator", "-s",
              default="\n",
              help="Text used to separate numbers (default: \\n)")
@click.version_option(version="1.0.0")
@click.argument("operands", type=click.INT, nargs=-1)
def seq(operands, separator) -> None:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    elif len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    elif len(operands) == 3:
        first, increment, last = operands
    else:
        raise click.BadParameter("Invalid number of arguments")
    last = last - 1 if first > last else last + 1
    print(separator.join(str(i) for i in range(first, last, increment)))

if __name__ == "__main__":
    seq()