import click


@click.group()
def main():
    pass


@main.command()
def init():
    print("Init called")


@main.command()
def chat():
    print("Chat called")


cli = click.CommandCollection(sources=[main])


if __name__ == "__main__":
    cli()
