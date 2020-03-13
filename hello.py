#!/usr/bin/env python3
import click  # Step 2: import the command-line tool library


@click.command()  # Step 4: Use click decorator
@click.option("--name", prompt="Enter the name", help="This name adds an apple to it")
def make_apple(name):
    value = f"{name}-apple"  # Step 3: Create a function
    click.echo(value)


# print(make_apple("charlie"))

# var=

if __name__ == "__main__":  # Step 5: Call function in __name__ method
    # pylint: disable=no-value-for-parameter
    make_apple()
