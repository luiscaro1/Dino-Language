import ply.lex as lex


tokens = {"DIGIT", "PLUS", "CHARACTER", "PERIOD", "BOOL", "MULT", "SUB", "DIV"}


t_PLUS = r"plus"
t_MINUS = r"minus"
t_CHARACTER = r"[a-zA-z]"
t_TIMES = r"times"
t_DIVIDE = r"divided"
t_PERIOD = r"\."
t_BOOL = r"true|false"
