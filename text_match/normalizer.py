"""Factory for normalizing text.
"""

import re
from dataclasses import dataclass
import unicodedata

import opencc


# Type dict
@dataclass
class NormalizerOptions:
    """
    Options for the normalizer.

    Only `nfkc` is enabled by default.

    >>> options = NormalizerOptions()
    >>> print(options)
    NormalizerOptions(remove_whitespace=False, strip_whitespace=False, ignore_chinese_variant=False, ignore_case=False)
    >>> options.enable_all()
    NormalizerOptions(remove_whitespace=True, strip_whitespace=True, ignore_chinese_variant=True, ignore_case=True)
    """

    """Whether to remove whitespace from the text."""
    remove_whitespace: bool = False

    """Whether to trim whitespace at the beginning and end of the text."""
    strip_whitespace: bool = False

    """Whether to ignore the variant of Chinese characters."""
    ignore_chinese_variant: bool = False

    """Whether to ignore the case of the text."""
    ignore_case: bool = False

    """Whether to normalize the text to NFKC."""
    nfkc: bool = True

    def __init__(self, **kwargs):
        self.strip_whitespace = kwargs.get('strip_whitespace', False)
        self.remove_whitespace = kwargs.get('remove_whitespace', False)
        self.ignore_chinese_variant = kwargs.get('ignore_chinese_variant', False)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.nfkc = kwargs.get('nfkc', True)

    @classmethod
    def enable_all(cls) -> 'NormalizerOptions':
        """Enable all options."""
        return cls(
            strip_whitespace=True,
            remove_whitespace=True,
            ignore_chinese_variant=True,
            ignore_case=True,
            nfkc=True,
        )

    @classmethod
    def from_string(cls, options_string: str) -> 'NormalizerOptions':
        """Create a NormalizerOptions from a string."""
        if options_string is None or options_string.strip() == '':
            return cls()
        options = cls()
        for option in options_string.split(','):
            if option == 'strip_whitespace':
                options.strip_whitespace = True
            elif option == 'remove_whitespace':
                options.remove_whitespace = True
            elif option == 'ignore_chinese_variant':
                options.ignore_chinese_variant = True
            elif option == 'ignore_case':
                options.ignore_case = True
            elif option == 'nfkc':
                options.nfkc = True
        return options


class Normalizer:
    """
    Normalizer for text.

    >>> normalizer = Normalizer()
    >>> normalizer.normalize('Hello, world!')
    'Helloworld'

    Args:
        options: Options for the normalizer.
    """

    options: NormalizerOptions

    def __init__(self, options: NormalizerOptions | None = None):
        if options is None:
            options = NormalizerOptions()
        self.options = options

    def normalize(self, text: str, _options: NormalizerOptions | None = None) -> str:
        """Normalize the text based on provided options."""
        if _options is None:
            _options = self.options

        if _options.strip_whitespace:
            text = self._strip_whitespace(text)
        if _options.remove_whitespace:
            text = self._remove_whitespace(text)
        if _options.nfkc:
            text = self._normalize_to_nfkc(text)
        if _options.ignore_chinese_variant:
            # Convert the text to Simplified Chinese
            text = self._convert_to_simplified_chinese(text)
        if _options.ignore_case:
            text = text.lower()
        return text

    def _strip_whitespace(self, text: str) -> str:
        """
        Strip whitespace from the text.
        """
        return text.strip()

    def _remove_whitespace(self, text: str) -> str:
        """
        Remove whitespace from the text.
        """
        return re.sub(r'\s+', '', text)

    def _convert_to_simplified_chinese(self, text: str) -> str:
        """
        Convert the text to Simplified Chinese.
        """
        opencc_converter = opencc.OpenCC('t2s')
        return opencc_converter.convert(text)

    def _normalize_to_nfkc(self, text: str) -> str:
        """
        Normalize the text to NFKC.

        The “NFKC” stands for “Normalization Form KC [Compatibility Decomposition, followed by Canonical Composition]”, and replaces full-width characters by half-width ones, which are Unicode equivalent.

        Note that it also normalizes all sorts of other things at the same time, like separate accent marks and Roman numeral symbols.

        Reference: https://stackoverflow.com/a/2422245
        """
        return unicodedata.normalize('NFKC', text)
