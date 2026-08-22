"""
This is basically a wrapper file, used as a module
in the main file, just to make things simple
"""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal

    from _typeshed import SupportsWrite


def add_line_seps(symbol: str, length: int):
    line_sep = symbol * length

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(line_sep)
            result = func(*args, **kwargs)
            print(line_sep)

            return result

        return wrapper

    return decorator


@add_line_seps(symbol="-", length=40)
def print_with_line_seps(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False,
) -> None:
    print(*values, sep=sep, end=end, file=file, flush=flush)

