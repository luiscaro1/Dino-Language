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
tokens = ["PERIOD", "QUEST", "ID", "NUMBER", "NEWLINE"] + list(reserved.values())

t_PERIOD = r"\."
t_QUEST = r"\?"
t_ignore = " \t"
t_NUMBER = r"\d+"




def t_NEWLINE(t):
    r"""\n"""
    t.lexer.lineno += 1
    return t


def t_ID(t):
    r"""[a-zA-z][a-zA-Z0-9]*"""
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex(debug=0)
