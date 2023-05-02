import sys

from emit import Emitter
from lex import Lexer
from tok import TokenType


class Parser:
    def __init__(self, lexer: Lexer, emitter: Emitter) -> None:
        self.lexer = lexer
        self.emitter = emitter

        self.curr_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()

    def check_curr_token(self, kind):
        """Check type of current token is as expected."""
        return self.curr_token.type == kind

    def check_peek_token(self, kind):
        """Check type of peek token is as expected."""
        return self.peek_token.type == kind

    def match(self, kind):
        """Ensure current token matches expected type, return next."""
        if not self.check_curr_token(kind):
            self.abort(f"Expected {kind}, got {self.curr_token.type}")
        self.next_token()

    def next_token(self):
        """Parse next token."""
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.get_token()

    def abort(self, message):
        """Abort parsing."""
        sys.exit(f"Parse error: {message}")

    def program(self):
        """Program grammar rule."""

        # Parse all newlines before source code
        while self.check_curr_token(TokenType.NEWLINE):
            self.next_token()

        # Parse all statements until file is complete
        while not self.check_curr_token(TokenType.EOF):
            self.statement()

    def statement(self):
        """Statement grammar rule."""

        if self.check_curr_token(TokenType.PROP):
            # print(f"Declared proposition: {self.peek_token.text}")

            self.emitter.declare_proposition(self.peek_token.text)

            self.next_token()
            self.match(TokenType.IDENT)
            self.nl()
        elif self.check_curr_token(TokenType.BLOCK):
            self.emitter.init_assignments()
            # print("Block while detected: ", end="")

            self.next_token()
            self.match(TokenType.WHILE)
            self.formula()
            self.nl()
        else:
            self.abort("Invalid statement:  " + self.curr_token.text)

    def formula(self):
        """Formula grammar rule."""
        # print(f"{self.curr_token.text} ", end="")
        proposition = self.curr_token.text
        self.match(TokenType.IDENT)
        # print(f"{self.curr_token.text} ", end="")
        self.match(TokenType.EQEQ)
        # print(f"{self.curr_token.text} ", end="\n")

        if self.check_curr_token(TokenType.TRUE):
            self.emitter.block_while(proposition, True)
            self.next_token()
        elif self.check_curr_token(TokenType.FALSE):
            self.emitter.block_while(proposition, False)
            self.next_token()
        else:
            self.abort(
                "Invalid token, expected TRUE or FALSE, got " + self.curr_token.type
            )

    def nl(self):
        """Newline grammar rule."""
        self.match(TokenType.NEWLINE)
        while self.check_curr_token(TokenType.NEWLINE):
            self.next_token()
