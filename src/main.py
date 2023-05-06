import sys
import time

from emit import Emitter
from lex import Lexer
from parse import Parser
from tok import TokenType

if __name__ == "__main__":
    print("Compiler started.", end="\n\n")

    if len(sys.argv) != 2:
        sys.exit("Compiler missing source file as argument.")

    with open(sys.argv[1], "r") as f:
        source = f.read() + "\n"

    lexer = Lexer(source)
    emitter = Emitter()
    parser = Parser(lexer, emitter)

    parser.program()
    print()

    print(
        "Truth table cotaining the elements of the powerset of P (this set is the input alphabet to the reward machine):"
    )
    for i, x in enumerate(emitter.assignments):
        print(f"Alphabet symbol: {i}\tProposition assigments: {x}")

    print()
    print(f"Output regular expression: {emitter.language}")
