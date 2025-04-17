from parser.tokenizer import tokenize

def parse(code):
    tokens = tokenize(code)
    return {"type": "Program", "tokens": tokens}
