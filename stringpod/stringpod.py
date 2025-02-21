"""Main module."""

import re

import hanzidentifier

from stringpod.normalizer import Normalizer, NormalizerOptions


def contains_chinese(text: str) -> bool:
    """Check if the text contains Chinese characters.

    Example:
    >>> contains_chinese('你好，世界！')
    True
    >>> contains_chinese('Hello, world!')
    False
    """
    return bool(hanzidentifier.has_chinese(text))


def contains_english(text: str) -> bool:
    """Check if the text contains English characters.

    Example:
    >>> contains_english('Hello, world!')
    True
    >>> contains_english('你好，世界！')
    False
    >>> contains_english('HelloWorld')
    True
    """
    return bool(re.search(r"[a-zA-Z]", text))


def contains_number(text: str) -> bool:
    """Check if the text contains numbers.

    Example:
    >>> contains_number('Hello, world!')
    False
    >>> contains_number('你好，世界！')
    False
    >>> contains_number('你好123')
    True
    """
    return bool(re.search(r"\d", text))


def contains_punctuation(text: str) -> bool:
    """Check if the text contains punctuation.

    Example:
    >>> contains_punctuation('Hello, world!')
    True
    >>> contains_punctuation('你好，世界！')
    True
    >>> contains_punctuation('你好世界')
    False
    """
    return bool(re.search(r"[^\w\s]", text))


def contains_special_character(text: str) -> bool:
    """Check if the text contains special characters.

    Example:
    >>> contains_special_character('Hello,world!')
    True
    >>> contains_special_character('Helloworld!')
    True
    >>> contains_special_character('Hello World')
    False
    >>> contains_special_character('HelloWorld')
    False
    """
    return bool(re.search(r"[^a-zA-Z0-9\s]", text))


def contains_whitespace(text: str) -> bool:
    """Check if the text contains whitespace.

    Example:
    >>> contains_whitespace('Hello, world!')
    True
    >>> contains_whitespace('Hello world!')
    True
    >>> contains_whitespace('HelloWorld!')
    False
    """
    return bool(re.search(r"\s", text))


def contains_url(text: str) -> bool:
    """Check if the text contains a URL.

    Example:
    >>> contains_url('https://www.google.com')
    True
    >>> contains_url('http://www.google.com')
    True
    >>> contains_url('www.google.com')
    False
    >>> contains_url('google.com')
    False
    """
    return bool(re.search(r"https?://", text))


def contains_email(text: str) -> bool:
    """Check if the text contains an email.

    Example:
    >>> contains_email('test@example.com')
    True
    >>> contains_email('test@example.com.tw')
    True
    >>> contains_email('test@example')
    False
    """
    return bool(re.search(r"^\S+@\S+\.\S+$", text))


def contains_substring(text: str, substring: str, options: NormalizerOptions | None = None) -> bool:
    """Check if the text contains a substring.

    Text will undergo the following transformations before checking:
    - Normalize to lowercase
    - Remove whitespace
    - Remove punctuation
    - Remove special characters
    - Romanize Chinese characters

    The following will be checked:
    - Traditional and Simplified Chinese
        (If the substring is in Traditional Chinese, it will also be checked in Simplified Chinese)

    Example:

    >>> contains_substring('你好，世界！', '你好')
    True
    >>> options = NormalizerOptions(ignore_chinese_variant=True)
    >>> contains_substring('計算機', '计算', options)
    True
    >>> options_all = NormalizerOptions.enable_all()
    >>> contains_substring('計算機', 'Ji', options_all)
    False

    Args:
        text: The text to check
        substring: The substring to check for
        options: Normalization options to apply

    Returns:
        True if the text contains the substring, False otherwise
    """
    normalizer = Normalizer(options=options)
    text_normalized = normalizer.normalize(text)
    substring_normalized = normalizer.normalize(substring)

    # Check if the substring is in Simplified Chinese
    return bool(re.search(substring_normalized, text_normalized))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
