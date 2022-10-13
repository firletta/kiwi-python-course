import click


@click.command()
@click.argument("numbers", nargs=3, type=int)
def average(numbers):
    average = sum(numbers) / len(numbers)
    print(average)

    
if __name__ == "__main__":
    average()