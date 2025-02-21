"""Module for parsing numbers from strings."""

from number_parser import parse, parse_number, parse_ordinal

from stringpod.language import detect_language


def to_number_with_language(text: str, language: str) -> str:
    """Convert a string to a number.

    Reference: Uses [number-parser](https://github.com/fengsp/number-parser) to parse the number.

    >>> to_number_with_language("one two three", "en")
    "123"
    >>> to_number_with_language("一萬兩千六", "zh")
    "12600"
    >>> to_number_with_language("Une centaine et une dizaine", "fr")
    "110"
    >>> to_number_with_language("Einhundertzehn", "de")
    "110"

    Args:
        text: The string to convert.
        language: The language of the string.

    Returns:
        The number parsed from the string.
    """
    # Convert the language code to the number parser code
    language_code = __to_number_parser_code(language)

    if language_code == "en":
        parsed_ordinal = parse_ordinal(text)
        if parsed_ordinal is not None:
            return parsed_ordinal

    parsed_number = parse_number(text, language=language_code)
    if parsed_number is not None:
        return parsed_number

    # Parse the number
    parsed_result = parse(text, language=language_code)
    if parsed_result is not None:
        return parsed_result

    raise ValueError(f"Could not parse number from text: {text}")


def to_number(text: str) -> str:
    """Convert a string to a number.

    >>> to_number("one two three")
    "123"
    >>> to_number("一萬兩千六")
    "12600"
    >>> to_number("一萬兩千零六")
    "12006"
    >>> to_number("doscientos cincuenta y doscientos treinta y uno y doce")
    "250 y 231 y 12"

    Args:
        text: The string to convert.

    Returns:
        The number parsed from the string.
    """
    languages = detect_language(text)
    for language in languages:
        language_code = language.lang
        print(f"Trying language: {language_code}")
        try:
            return to_number_with_language(text, language_code)
        except ValueError:
            continue
    raise ValueError(f"Could not parse number from text: {text}")


_number_parser_codes = [
    "af",
    "ak",
    "am",
    "ar",
    "az",
    "be",
    "bg",
    "bs",
    "ca",
    "ccp",
    "chr",
    "cs",
    "cy",
    "da",
    "de-CH",
    "de",
    "ee",
    "el",
    "en-IN",
    "en",
    "eo",
    "es",
    "et",
    "fa-AF",
    "fa",
    "ff",
    "fi",
    "fil",
    "fo",
    "fr-BE",
    "fr-CH",
    "fr",
    "ga",
    "he",
    "hi",
    "hr",
    "hu",
    "hy",
    "id",
    "is",
    "it",
    "ja",
    "ka",
    "kl",
    "km",
    "ko",
    "ky",
    "lb",
    "lo",
    "lrc",
    "lt",
    "lv",
    "mk",
    "ms",
    "mt",
    "my",
    "nb",
    "nl",
    "nn",
    "pl",
    "pt-PT",
    "pt",
    "qu",
    "ro",
    "ru",
    "se",
    "sk",
    "sl",
    "sq",
    "sr-Latn",
    "sr",
    "su",
    "sv",
    "sw",
    "ta",
    "th",
    "tr",
    "uk",
    "vi",
    "yue-Hans",
    "yue",
    "zh-Hant",
    "zh",
]

mapping = {
    # Language codes: number_parser_codes
    "zh-cn": "zh-Hans",
    "zh-tw": "zh-Hant",
}


def __to_number_parser_code(language: str) -> str:
    """Convert a language to a number parser code.

    >>> __to_number_parser_code("en")
    "en"
    """
    language_lower = language.lower()
    if language in mapping:
        return mapping[language]
    if language_lower in _number_parser_codes:
        return language_lower
    if language.split("-")[0] in _number_parser_codes:
        return language.split("-")[0]

    raise ValueError(f"Language {language} not supported")
