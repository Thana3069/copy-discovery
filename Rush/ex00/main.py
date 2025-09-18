#!/usr/bin/env python
from checkmate import checkmate


def main_example1():
    print("--- Running Example 1 ---")
    board = """\
R...
.K..
..P.
...."""
    checkmate(board)


def main_example2():
    print("\n--- Running Example 2 ---")
    board = """\
..
.K"""
    checkmate(board)
    

def main_example3():
    print("\n--- Running Example 3 ---")
    board = """\
B...
....
..K.
...."""
    checkmate(board)


# บรรทัดนี้คือจุดเริ่มต้นของโปรแกรม
if __name__ == "__main__":
    main_example1()
    main_example2()
    main_example3()