"""Test the pinyin module."""

import pytest
from pypinyin import Style

from stringpod.pinyin import get_pinyin, match_pinyin


class TestGetPinyin:
    """Test the get_pinyin function."""

    @pytest.mark.parametrize(
        "input_text, expected, style_kwarg",
        [
            ("李浩", ['li', 'hao'], {}),
            ("你好", ['ni', 'hao'], {}),
            ("重庆", ['chong', 'qing'], {"style": Style.NORMAL}),
            ("重庆", ['chóng', 'qìng'], {"style": Style.TONE}),
            ("重庆", ['chong2', 'qing4'], {"style": Style.TONE3}),
        ],
    )
    def test_get_pinyin_basic(self, input_text, expected, style_kwarg):
        """Test the get_pinyin function with basic cases."""
        assert get_pinyin(input_text, **style_kwarg) == expected


class TestMatchPinyin:
    """Test the match_pinyin function."""

    @pytest.mark.parametrize(
        "text1, text2, expected, with_tone, spoken_tone",
        [
            ("李浩", "理好", True, False, False),
            ("李浩", "理好", False, True, True),
            ("妈妈", "马麻", True, False, False),
            ("是", "市", True, True, False),
            ("重庆", "重慶", True, False, True),
        ],
    )
    def test_match_cases(self, text1, text2, expected, with_tone, spoken_tone):
        """Test the match_pinyin function with different cases."""
        assert match_pinyin(text1, text2, with_tone, spoken_tone) == expected

    def test_length_mismatch(self):
        """Test the match_pinyin function with different length of text1 and text2."""
        with pytest.raises(ValueError):
            match_pinyin("你好", "你好吗")

    @pytest.mark.parametrize(
        "text1, text2",
        [
            ("银行", "銀行"),  # Different characters but same pronunciation
            ("发现", "髮現"),  # Homophone in some contexts
        ],
    )
    def test_heteronym_matching(self, text1, text2):
        """Test the match_pinyin function with heteronym matching."""
        assert match_pinyin(text1, text2, with_tone=False)
