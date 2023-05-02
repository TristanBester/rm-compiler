from enum import Enum


class TokenType(Enum):
    EOF = -1
    NEWLINE = 0
    IDENT = 1
    # Keywords
    PROP = 100
    WHILE = 101
    BLOCK = 102
    TRUE = 103
    FALSE = 104
    # Operators
    EQEQ = 201


class Token:
    def __init__(self, text: str, type: TokenType) -> None:
        """Token constructor."""
        self.text = text
        self.type = type

    def __repr__(self) -> str:
        return f"{self.type}: {self.text}"

    @staticmethod
    def get_keyword(text: str) -> TokenType:
        """Return keyword token type."""
        for t in TokenType:
            if t.name == text and t.value >= 100 and t.value < 200:
                return t
        return None
