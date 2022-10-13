import click


@click.command()
@click.argument("name")
@click.argument("surname")
@click.option("--age","age")
def application(name, surname, age):
    print(f"Hello {name} {surname}! You are {age} years old!")


if __name__ == "__main__":
    application()