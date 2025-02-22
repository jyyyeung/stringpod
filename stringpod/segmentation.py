"""Segmentation of Chinese text."""

import jieba


def segment_text(text: str) -> list[str]:
    """Segment the text into characters.

    >>> segment_text("你好，世界！")
    ['你好', '，', '世界', '！']
    >>> segment_text("我爱北京天安门")
    ['我', '爱', '北京', '天安门']
    """
    # jieba.enable_paddle()
    return list(jieba.cut(text, cut_all=False))
