"""Pinyin module for StringPod."""

import logging

from pypinyin import Style, lazy_pinyin

from stringpod.language import to_simplified_chinese

logger = logging.getLogger(__name__)


def get_pinyin(text: str, **kwargs) -> list[str]:
    """Get the pinyin of a text.

    >>> get_pinyin("李浩")
    ['lǐ', 'hào']

    Args:
        text (str): The text to get the pinyin of.
        **kwargs: Additional keyword arguments for the pinyin function.
    """
    pinyin_list = lazy_pinyin(text, **kwargs)
    return pinyin_list


def match_pinyin(text1: str, text2: str, with_tone: bool = False, spoken_tone: bool = False) -> bool:
    """Match the pinyin of a text with a pinyin string.

    >>> match_pinyin("李浩", "理好", with_tone=False)
    True
    >>> match_pinyin("李浩", "理好", with_tone=True)
    False

    Args:
        text1 (str): The text to match.
        text2 (str): The pinyin string to match.
        with_tone (bool, optional): Whether to include the tone in the pinyin. Defaults to False.
        spoken_tone (bool, optional): Whether to use the spoken tone. Defaults to False.

    Returns:
        bool: True if the pinyin of text1 matches the pinyin of text2, False otherwise.
    """
    if len(text1) != len(text2):
        raise ValueError("The length of text1 and text2 must be the same.")

    style = Style.TONE3 if with_tone else Style.NORMAL
    tone_sandhi = bool(spoken_tone)

    # 以簡體中文為標准轉拼音
    text1_cn = to_simplified_chinese(text1)
    text2_cn = to_simplified_chinese(text2)

    # 获取拼音
    pinyin1 = get_pinyin(text1_cn, style=style, tone_sandhi=tone_sandhi)
    pinyin2 = get_pinyin(text2_cn, style=style, tone_sandhi=tone_sandhi)
    logger.debug("pinyin1: %s, pinyin2: %s", pinyin1, pinyin2)

    length = len(pinyin1)

    for i in range(length):
        logger.debug("pinyin1[i]: %s, pinyin2[i]: %s, %s", pinyin1[i], pinyin2[i], pinyin1[i] == pinyin2[i])
        if pinyin1[i] != pinyin2[i]:
            return False

        # # Character i
        # char_list1 = pinyin1[i]
        # char_list2 = pinyin2[i]

        # char_py_matched = False
        # # Ensure that at least one character in char_list1 is in char_list2
        # for py1 in char_list1:
        #     if py1 in char_list2:
        #         char_py_matched = True
        #         break

        # if not char_py_matched:
        #     return False
    return True
