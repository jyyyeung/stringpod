"""Segmentation of Chinese text."""

import jieba

jieba.enable_paddle()


def segment_text(text: str) -> list[str]:
    """Segment the text into characters."""
    return list(jieba.cut(text, cut_all=False))
