# parser.py
import ply.yacc as yacc
from lexer import tokens  # Importer la liste de tokens depuis lexer.py

# Définir la grammaire (Parser)
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = int(p[1])

# Gestion des erreurs de syntaxe
def p_error(p):
    print("Erreur de syntaxe!")

# Construire l'analyseur
parser = yacc.yacc()

# Fonction pour analyser les tokens et renvoyer le résultat (par exemple, l'AST ou une évaluation)
def parse_expression(data):
    return parser.parse(data)
