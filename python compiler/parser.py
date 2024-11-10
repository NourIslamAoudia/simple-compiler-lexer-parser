import ply.yacc as yacc
from lexer import tokens  # Importer la liste des tokens

# Définir les précédences des opérateurs
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Définir les règles de la grammaire
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = int(p[1])
    else:
        p[0] = p[2]

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

# Fonction pour analyser une expression et retourner le résultat
def parse_expression(data):
    result = parser.parse(data)
    return result
