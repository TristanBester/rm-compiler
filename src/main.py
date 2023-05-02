import sys
import time

from emit import Emitter
from lex import Lexer
from parse import Parser
from tok import TokenType

if __name__ == "__main__":
    print("Compiler started.")

    if len(sys.argv) != 2:
        sys.exit("Compiler missing source file as argument.")

    with open(sys.argv[1], "r") as f:
        source = f.read() + "\n"

    lexer = Lexer(source)
    emitter = Emitter()
    parser = Parser(lexer, emitter)

    parser.program()

    for i in emitter.assignments:
        print(i)

    print(emitter.language)
