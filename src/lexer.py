import ply.lex as lex

reserved = {
    "is": "IS",
    "a": "A",
    "an": "AN",
    "are": "ARE",
    "plus": "PLUS",
    "minus": "MINUS",
    "times": "TIMES",
    "divided": "DIVIDED",
    "by": "BY",
    "true": "TRUE",
    "false": "FALSE",
}
tokens = ["PERIOD", "QUEST", "ID", "DIGIT", "EOF"] + list(reserved.values())


t_PERIOD = r"\."
t_QUEST = r"\?"
t_ignore = " \t"


def t_DIGIT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_ID(t):
    r"[a-zA-z][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


data = "is an a are times divided by true false"

lexer = lex.lex()
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
