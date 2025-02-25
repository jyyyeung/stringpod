"""Sort strings."""


def sort(strings: list[str]) -> list[str]:
    """Sort strings.

    >>> sort(["4", "2", "3b", "3a", "1", "5"])
    ['1', '2', '3a', '3b', '4', '5']
    """
    # 1, 2, 3a, 3b, 4, 5
    return sorted(strings)
