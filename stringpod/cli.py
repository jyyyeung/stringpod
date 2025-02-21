"""Console script for stringpod."""

import click

from stringpod.normalizer import Normalizer, NormalizerOptions
from stringpod.number import to_number, to_number_with_language
from stringpod.stringpod import contains_substring


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Main entrypoint."""
    if ctx.invoked_subcommand is None:
        click.echo("stringpod")
        click.echo("=" * len("stringpod"))
        click.echo("Matching texts across languages")


@main.command()
@click.argument("text", type=str)
@click.argument("substring", type=str)
@click.option("--options", type=str, help="The options to use for the normalizer")
def contains(text: str, substring: str, options: str):
    """Check if the text contains the substring.

    >>> stringpod contains "Hello, world!" "world"
    True
    """
    click.echo(f"Text: {text}")
    click.echo(f"Substring: {substring}")
    options_obj = NormalizerOptions.from_string(options)
    click.echo(f"Options: {options_obj}")
    click.echo(f"Result: {contains_substring(text, substring, options_obj)}")


@main.command()
@click.argument("text", type=str)
@click.option("--options", type=str, help="The options to use for the normalizer")
def normalize(text: str, options: str):
    """Normalize the text.

    >>> stringpod normalize "Hello, world!"
    "Hello, world!"
    >>> stringpod normalize "Hello, world!" --options "ignore_case"
    "hello, world!"
    >>> stringpod normalize "Hello, world!"
    """
    click.echo(f"Text: {text}")
    options_obj = NormalizerOptions.from_string(options)
    click.echo(f"Options: {options_obj}")

    normalizer = Normalizer(options_obj)
    click.echo(f"Result: {normalizer.normalize(text)}")


@main.command()
@click.argument("text", type=str)
@click.option("--language", type=str, help="The language code of the text")
def number(text: str, language: str):
    """Parse a number from a string.

    >>> stringpod number "one two three"
    123
    >>> stringpod number "一二三"
    123
    >>> stringpod number "uno dos tres" --language "es"
    1 2 3
    """
    click.echo(f"Text: {text}")
    click.echo(f"Language: {language}")
    result = None
    if language is None or language == "":
        result = to_number(text)
    else:
        result = to_number_with_language(text, language)
    click.echo(f"Result: {result}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main(None)  # pragma: no cover
