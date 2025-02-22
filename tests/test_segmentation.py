"""Test the segmentation module."""

import pytest

from stringpod.segmentation import segment_text


class TestSegmentText:
    """Test the segment_text function."""

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("你好，世界！", ['你好', '，', '世界', '！']),
            ("我爱北京天安门", ['我', '爱', '北京', '天安门']),
        ],
    )
    def test_segment_text(self, text, expected):
        """Test the segment_text function with basic cases."""
        assert segment_text(text) == expected
