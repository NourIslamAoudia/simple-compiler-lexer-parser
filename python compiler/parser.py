import ply.yacc as yacc
from lexer import tokens

# Définir les précédences des opérateurs (du moins prioritaire au plus prioritaire)
precedence = (
    ('left', 'OR'),     # ||
    ('left', 'AND'),    # &&
    ('left', 'EQ', 'NE'),  # ==, !=
    ('left', 'LT', 'LE', 'GT', 'GE'),  # <, <=, >, >=
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),   # !
)

# Règles de grammaire pour les expressions
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
            if p[3] == 0:  # Protection contre la division par zéro
                print("Erreur: Division par zéro!")
                p[0] = 0
            else:
                p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

# Règles pour les opérateurs logiques
def p_expression_logical(p):
    '''expression : expression AND expression
                  | expression OR expression
                  | NOT expression'''
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = 1 if p[1] and p[3] else 0
        elif p[2] == '||':
            p[0] = 1 if p[1] or p[3] else 0
    else:  # NOT
        p[0] = 1 if not p[2] else 0

# Règles pour les opérateurs de comparaison
def p_expression_comparison(p):
    '''expression : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    if p[2] == '<':
        p[0] = 1 if p[1] < p[3] else 0
    elif p[2] == '<=':
        p[0] = 1 if p[1] <= p[3] else 0
    elif p[2] == '>':
        p[0] = 1 if p[1] > p[3] else 0
    elif p[2] == '>=':
        p[0] = 1 if p[1] >= p[3] else 0
    elif p[2] == '==':
        p[0] = 1 if p[1] == p[3] else 0
    elif p[2] == '!=':
        p[0] = 1 if p[1] != p[3] else 0

def p_factor(p):
    '''factor : NUMBER
              | LPAREN expression RPAREN
              | boolean'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''
    p[0] = 1 if p[1] == 'true' else 0

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