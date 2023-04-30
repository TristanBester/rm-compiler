import sys


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

        print(self.curr_char)
        self.next_char()


if __name__ == "__main__":
    source = "PROP coffee\n"

    lexer = Lexer(source)

    for i in range(11):
        lexer.get_token()
