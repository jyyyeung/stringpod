"""Module for detecting the language of a string."""

from langdetect import DetectorFactory, detect_langs
from langdetect.language import Language

DetectorFactory.seed = 0


def detect_language(text: str) -> list[Language]:
    """Detect the language of a string.

    >>> detect_language("Hello, world!")
    "en"
    >>> detect_language("你好，世界！")
    "zh"

    Reference: Uses [langdetect](https://github.com/Mimino666/langdetect) to detect the language.

    Args:
        text: The text to detect the language of.

    Returns:
        The language of the text.
    """
    return detect_langs(text)


_langdetect_codes = [
    "af",
    "ar",
    "bg",
    "bn",
    "ca",
    "cs",
    "cy",
    "da",
    "de",
    "el",
    "en",
    "es",
    "et",
    "fa",
    "fi",
    "fr",
    "gu",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "kn",
    "ko",
    "lt",
    "lv",
    "mk",
    "ml",
    "mr",
    "ne",
    "nl",
    "no",
    "pa",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "so",
    "sq",
    "sv",
    "sw",
    "ta",
    "te",
    "th",
    "tl",
    "tr",
    "uk",
    "ur",
    "vi",
    "zh-cn",
    "zh-tw",
]
