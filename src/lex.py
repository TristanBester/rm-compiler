import sys

from tok import Token, TokenType


class Lexer:
    def __init__(self, source: str) -> None:
        """Lexer constructor."""
        self.source = source

        # Current character index in source code
        self.curr_pos = -1
        # Current character
        self.curr_char = ""

        # Initialise attributes
        self.next_char()

    def next_char(self):
        """Move to next character in source code."""
        self.curr_pos += 1

        try:
            self.curr_char = self.source[self.curr_pos]
        except IndexError:
            # If source code is exhausted, set current character to EOF
            self.curr_char = "\0"

    def peek(self):
        """Return next character in source code."""
        try:
            return self.source[self.curr_pos + 1]
        except IndexError:
            # If source code is exhausted, return EOF
            return "\0"

    def abort(self, message):
        """Print fatal error message and exit."""
        sys.exit(f"Lexing error ocurred: {message}")

    def skip_whitespace(self):
        """Skip whitespace except newlines."""
        while self.curr_char in (" ", "\t", "\r"):
            self.next_char()

    def skip_comments(self):
        """Skip comments."""
        if self.curr_char == "#":
            while self.curr_char != "\n":
                self.next_char()

    def get_token(self):
        self.skip_whitespace()
        self.skip_comments()

        if self.curr_char == "=":
            if self.peek() == "=":
                last_char = self.curr_char
                self.next_char()
                token = Token(last_char + self.curr_char, TokenType.EQEQ)
            else:
                self.next_char()
                self.abort(f"Expected '==', got ={self.curr_char}")
        elif self.curr_char == "\n":
            token = Token(self.curr_char, TokenType.NEWLINE)
        elif self.curr_char == "\0":
            token = Token(self.curr_char, TokenType.EOF)
        elif self.curr_char.isalpha():
            start_pos = self.curr_pos

            while self.peek().isalnum():
                self.next_char()

            token_text = self.source[start_pos : self.curr_pos + 1]
            keyword = Token.get_keyword(token_text)

            if keyword:
                token = Token(token_text, keyword)
            else:
                token = Token(token_text, TokenType.IDENT)
        else:
            self.abort("Unknown token: " + self.curr_char)

        self.next_char()
        return token
