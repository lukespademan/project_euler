from typing import Any


def reverse(num: Any) -> Any:
    t = type(num)
    s = str(num)
    return t(s[::-1])
