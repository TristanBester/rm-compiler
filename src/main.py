import sys
import time

from lex import Lexer
from tok import TokenType

if __name__ == "__main__":
    print("Compiler started.")

    if len(sys.argv) != 2:
        sys.exit("Compiler missing source file as argument.")

    with open(sys.argv[1], "r") as f:
        source = f.read()

    print(source)

    lexer = Lexer(source)

    token = lexer.get_token()
    while token.type != TokenType.EOF:
        print(token)
        token = lexer.get_token()
        # time.sleep(2)
