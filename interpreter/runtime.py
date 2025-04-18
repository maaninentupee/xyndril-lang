def execute(ast):
    print("🔍 Executing Xyndril program...\n")
    for token in ast["tokens"]:
        if token[0] == "STRING":
            print(token[1].strip('"'))
