import re

TOKEN_REGEX = [
    ("STRING", r'"[^"]*"'),
    ("NUMBER", r'\d+'),
    ("ID", r'[a-zA-Z_]\w*'),
    ("LPAREN", r'\('),
    ("RPAREN", r'\)'),
    ("LBRACE", r'\{'),
    ("RBRACE", r'\}'),
    ("COLON", r':'),
    ("COMMA", r','),
    ("PLUS", r'\+'),
    ("EQ", r'='),
    ("ARROW", r'=>'),
    ("NEWLINE", r'\n'),
    ("SKIP", r'[ \t]+'),
    ("UNKNOWN", r'.'),
]

def tokenize(code):
    tokens = []
    index = 0
    while index < len(code):
        match = None
        for token_type, pattern in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(code, index)
            if match:
                if token_type != "SKIP":
                    tokens.append((token_type, match.group(0)))
                index = match.end()
                break
        if not match:
            raise SyntaxError(f"Illegal character: {code[index]}")
    return tokens
