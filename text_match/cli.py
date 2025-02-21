"""Console script for text_match."""

import click

from text_match.normalizer import NormalizerOptions
from text_match.text_match import contains_substring


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Main entrypoint."""
    if ctx.invoked_subcommand is None:
        click.echo("text-match")
        click.echo("=" * len("text-match"))
        click.echo("Matching texts across languages")


@main.command()
@click.argument('text', type=str)
@click.argument('substring', type=str)
@click.option('--options', type=str, help='The options to use for the normalizer')
def contains(text: str, substring: str, options: str):
    """
    Check if the text contains the substring.

    >>> text-match contains "Hello, world!" "world"
    True
    """
    click.echo(f"Text: {text}")
    click.echo(f"Substring: {substring}")
    options_obj = NormalizerOptions.from_string(options)
    click.echo(f"Options: {options_obj}")
    click.echo(f"Result: {contains_substring(text, substring, options_obj)}")


if __name__ == "__main__":
    main(None)  # pragma: no cover
