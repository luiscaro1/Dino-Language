# Yacc example

import ply.yacc as yacc
from lexer import tokens


def p_factor(p):
    """factor : DIGIT"""
    p[0] = p[1]


def p_factor_exp(p):
    "factor : expression"
    p[0] = p[1]


def p_binary_operators(p):
    """expression : expression PLUS term
                  | expression MINUS term
        term      : term TIMES factor
                  | term DIVIDE factor"""

    if p[2] == "times":
        p[0] = p[1] * p[3]
    elif p[2] == "divided" and p[3] == "by":
        p[0] = p[1] / p[4]
    elif p[2] == "plus":
        p[0] = p[1] + p[3]
    elif p[2] == "minus":
        p[0] = p[1] - p[3]


def p_expression(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : factor"""
    p[0] = p[1]
