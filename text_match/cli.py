"""Console script for text_match."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("text-match")
    click.echo("=" * len("text-match"))
    click.echo("Matching texts across languages")


if __name__ == "__main__":
    main()  # pragma: no cover
