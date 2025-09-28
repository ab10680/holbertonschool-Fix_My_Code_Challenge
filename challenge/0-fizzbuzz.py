#!/usr/bin/python3
"""Correct FizzBuzz implementation for the Fix My Code challenge."""

import sys


def fizzbuzz(n: int) -> str:
    """Return a space-separated FizzBuzz string from 1 to n."""
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return " ".join(out)


if __name__ == "__main__":
    try:
        limit = int(sys.argv[1])
    except (IndexError, ValueError):
        limit = 100
    print(fizzbuzz(limit))
