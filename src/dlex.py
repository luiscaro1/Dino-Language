import ply.lex as lex

reserved = {
    "is": "IS", "Is":"IS_UP",
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
    "What": "WHAT",
    "of" : "OF",
    "the": "THE", "The": "THE_UP",
    "length":"LENGTH"
}
tokens = ["PERIOD", "QUEST", "ID", "NUMBER", "COMMA", "NEGATIVE", "COLON"] + list(reserved.values())

t_PERIOD = r"\."
t_QUEST = r"\?"
t_NUMBER = r"\d+"
t_COMMA = r"\,"
t_ignore = " \t\n"
t_NEGATIVE = r"\-"
t_COLON = r"\:"


def t_ID(t):
    r"""[a-zA-z][a-zA-Z0-9]*"""
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex(debug=0)
