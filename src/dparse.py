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
                  | term DIVIDED factor"""

    if p[2] == "plus":
        p[0] = p[1] + p[3]
    elif p[2] == "minus":
        print(eval(p[1] - p[3]))
        p[0] = p[1] - p[3]
    elif p[2] == "times":
        print(eval(p[1] * p[3]))
        p[0] = p[1] * p[3]
    elif p[2] == "divided" and p[3] == "by":
        print(eval(p[1] / p[3]))
        p[0] = p[1] / p[4]



def p_expression(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : factor"""
    p[0] = p[1]

def p_factor(p):
    """factor : number"""
    print(p)
    print(p[0])
    print(p[1])
    p[0] = p[1]



def p_number(p):
    '''number  : NUMBER'''
    print(p[1])
    p[0] = eval(p[1])

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
