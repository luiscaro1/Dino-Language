from ply import *
import dlex
import sys

tokens = dlex.tokens


def p_program(p):
    """program : program sentence
               | sentence"""

    if len(p) == 2 and p[1]:
        p[0] = {}
        sen, stat = p[1]
        p[0][sen] = stat
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            a = p[2]
            sen, stat = p[2]
            p[0][sen] = stat


def p_sentence(p):
    '''sentence : expression PERIOD
                | definition PERIOD
                | question QUEST'''
    p[0] = (sen_num, p[1])


# expression
def p_expression(p):
    """expression : term"""
    p[0] = p[1]


# expression operations
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
            print("ZeroDivisionError: division by zero!")


# term
def p_term(p):
    """term : factor"""
    p[0] = p[1]


# factor
def p_factor(p):
    """factor : number"""
    p[0] = p[1]


# definition
def p_definition(p):
    '''definition : id IS A id
                  | id IS AN id
                  | id ARE COLON list
                  | id IS COLON list
                  | id IS datatype'''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1], p[4])


# question
def p_question(p):
    '''question : WHAT IS entity '''
    p[0] = p[3]


def p_question_is(p):
    '''question : IS_UP entity bool
                | IS_UP entity A datatype
                | IS_UP entity entity '''
    if p[3] == 'a':
        p[0] = (p[2], p[4])
    else:
        p[0] = (p[2], p[3])


def p_question_are(p):
    '''question : ARE_UP list entity
                | ARE_UP entity A datatype '''
    if p[3] == 'a':
        p[0] = (p[2], p[4])
    else:
        p[0] = (p[2], p[3])


# entity
def p_entity(p):
    '''entity : id
              | datatype'''
    p[0] = p[1]


# datatype
def p_datatype(p):
    '''datatype : number
                | bool'''
    p[0] = p[1]


# list
def p_list(p):
    '''list : entity COMMA list
            | entity'''
    if (len(p) > 3):
        p[0] = p[3]
        p[0].append(p[1])
    else:
        p[0] = [p[1]]
    # bool


# bool
def p_bool(p):
    '''bool : TRUE
            | FALSE'''
    if p[1] == 'true':
        p[0] = True
    else:
        p[0] = False


# number
def p_number(p):
    '''number : NUMBER
              | NEGATIVE NUMBER'''
    if p[1] == '-':
        p[0] = -eval(p[2])
    else:
        p[0] = eval(p[1])


# id
def p_id(p):
    '''id : ID'''
    p[0] = p[1]


# error
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

# brandon, luis,                                                                                      joshua
