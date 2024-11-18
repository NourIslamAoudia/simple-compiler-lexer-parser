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
    ('right', 'UMINUS'),  # Opérateur unaire moins
)

# Règle de grammaire principale pour les expressions
def p_expression(p):
    '''expression : arithmetic_expression
                  | logical_expression
                  | comparison_expression'''
    p[0] = p[1]

# Expressions arithmétiques
def p_arithmetic_expression(p):
    '''arithmetic_expression : arithmetic_expression PLUS arithmetic_expression
                             | arithmetic_expression MINUS arithmetic_expression
                             | arithmetic_expression TIMES arithmetic_expression
                             | arithmetic_expression DIVIDE arithmetic_expression
                             | LPAREN arithmetic_expression RPAREN
                             | MINUS arithmetic_expression %prec UMINUS
                             | NUMBER'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            if p[3] == 0:
                print("Erreur: Division par zéro!")
                p[0] = 0
            else:
                p[0] = p[1] / p[3]
        elif p[1] == '(' and p[3] == ')':
            p[0] = p[2]
    elif len(p) == 3:  # Moins unaire
        p[0] = -p[2]
    else:
        p[0] = p[1]

# Expressions logiques
def p_logical_expression(p):
    '''logical_expression : logical_expression AND logical_expression
                         | logical_expression OR logical_expression
                         | NOT logical_expression
                         | LPAREN logical_expression RPAREN
                         | comparison_expression'''
    if len(p) == 4:
        if p[2] == '&&':
            p[0] = 1 if p[1] and p[3] else 0
        elif p[2] == '||':
            p[0] = 1 if p[1] or p[3] else 0
        elif p[1] == '(' and p[3] == ')':
            p[0] = p[2]
    elif len(p) == 3:  # NOT
        p[0] = 1 if not p[2] else 0
    else:
        p[0] = p[1]

# Expressions de comparaison
def p_comparison_expression(p):
    '''comparison_expression : arithmetic_expression LT arithmetic_expression
                             | arithmetic_expression LE arithmetic_expression
                             | arithmetic_expression GT arithmetic_expression
                             | arithmetic_expression GE arithmetic_expression
                             | arithmetic_expression EQ arithmetic_expression
                             | arithmetic_expression NE arithmetic_expression'''
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

def p_expression_ignore_comment(p):
    '''expression : expression COMMENT
                  | COMMENT expression
                  | COMMENT'''
    if len(p) == 3:
        # Si le commentaire est avant ou après une expression
        p[0] = p[1] if p[1] != 'COMMENT' else p[2]
    elif len(p) == 2:
        # Si c'est juste un commentaire
        p[0] = None

# Gestion des erreurs de syntaxe
def p_error(p):
    if p and p.type == 'COMMENT':
        # Ignorer simplement les tokens de commentaire
        return
    if p:
        print(f"Erreur de syntaxe! Token: {p.type}, Valeur: {p.value}")
    else:
        print("Erreur de syntaxe à la fin de l'expression")
# Construire l'analyseur
parser = yacc.yacc()

# Fonction pour analyser une expression et retourner le résultat
def parse_expression(data):
    try:
        result = parser.parse(data)
        return result
    except Exception as e:
        print(f"Erreur lors de l'analyse : {e}")
        return None