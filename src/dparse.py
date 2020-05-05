from ply import *
import dlex
import sys

tokens = dlex.tokens


# def p_program(p):
#     """program : program statement
#                | statement"""
#
#     if len(p) == 2 and p[1]:
#         p[0] = {}
#         line, stat = p[1]
#         p[0][line] = stat
#     elif len(p) == 3:
#         p[0] = p[1]
#         if not p[0]:
#             p[0] = {}
#         if p[2]:
#             line, stat = p[2]
#             p[0][line] = stat

def p_binary_operators(p):
    """expression : expression PLUS term
                  | expression MINUS term
        term      : term TIMES factor
                  | term DIVIDED BY factor"""

    if p[2] == "plus":
        p[0] = p[1] + p[3]
    elif p[2] == "minus":
        p[0] = p[1] - p[3]
    elif p[2] == "times":
        p[0] = p[1] * p[3]
    elif p[2] == "divided" and p[3] == "by":
        if p[4] != 0:
            p[0] = int(p[1] / p[4])
        else:
            print("ZeroDivisionError: division by zero")


def p_expression(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : factor"""
    p[0] = p[1]

def p_factor(p):
    """factor : number"""
    p[0] = p[1]

def p_number(p):
    '''number  : NUMBER'''
    p[0] = eval(p[1])

def p_id(p):
    '''id : ID'''
    p[0] = p[1]
def p_error(p):
    if not p:
        print("SYNTAX ERROR AT EOF")


dparser = yacc.yacc()


def parse(data, debug=0):
    dparser.error = 0
    p = dparser.parse(data, debug=debug)
    if dparser.error:
        return None
    return p
