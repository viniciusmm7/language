from re import sub
from .keywords import KEYWORDS


class LexicalError(Exception):
    def __init__(self, message: str):
        self.message: str = message
        super().__init__(self.message)


class PrePro:
    @staticmethod
    def filter(source: str) -> str:
        source = sub(r'//.*?(?=\n|$)', '', source)
        return source


class Token:
    def __init__(self, token_type: str, value: any):
        self.type: str = token_type
        self.value: any = value


class Tokenizer:
    def __init__(self, source: str):
        self.source: str = source
        self.position: int = 0
        self.next: Token | None = None
        self.keywords: set[str] = KEYWORDS

    def select_next(self) -> None:
        while self.position <= len(self.source):
            # End of file
            if self.position == len(self.source):
                self.next = Token('EOF', '')
                self.position += 1
                return

            # Skip whitespaces
            if self.source[self.position] in [' ', '\t']:
                self.position += 1
                continue

            # Variable identifier or keyword logic
            if self.source[self.position].isalpha():
                start = self.position

                while self.position < len(self.source) and (
                        self.source[self.position].isalnum() or
                        self.source[self.position] == '_'):
                    self.position += 1

                token_value: str = self.source[start:self.position]
                
                
                if token_value in self.keywords:
                    self.next = Token(token_value.upper(), token_value)
                    return
                
                self.next = Token('IDENTIFIER', token_value)
                return
                
            # Integer logic
            if self.source[self.position].isdigit():
                start = self.position

                while True:
                    self.position += 1
                    if self.source[self.position].isalpha():
                        raise LexicalError(f'Invalid token "{self.source[self.position]}" at position {self.position}')
                    if self.position < len(self.source) and not self.source[self.position].isdigit():
                        break

                self.next = Token('INT', int(self.source[start:self.position]))
                return

            # Other tokens
            if self.source[self.position] == '=':
                self.next = Token('ASSIGN', '=')
                self.position += 1
                return
            
            if self.source[self.position] == ',':
                self.next = Token('COMMA', ',')
                self.position += 1
                return

            if self.source[self.position] == ';':
                self.next = Token('SEMICOLON', ';')
                self.position += 1
                return
            
            if self.source[self.position] == '(':
                self.next = Token('LPAREN', '(')
                self.position += 1
                return

            if self.source[self.position] == ')':
                self.next = Token('RPAREN', ')')
                self.position += 1
                return
            
            if self.source[self.position] == '{':
                self.next = Token('LBRACE', '{')
                self.position += 1
                return
            
            if self.source[self.position] == '}':
                self.next = Token('RBRACE', '}')
                self.position += 1
                return
            
            if self.source[self.position] == '?':
                self.next = Token('QUESTION', '?')
                self.position += 1
                return

            if self.source[self.position] == '\n':
                self.next = Token('NEWLINE', '\n')
                self.position += 1
                return

            raise LexicalError(f'Invalid token "{self.source[self.position]}" at position {self.position}')
