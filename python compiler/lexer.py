import ply.lex as lex

# Existing tokens remain the same
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN','AND',   'OR', 'NOT',  'LT',  
    'LE',   'GT',   'GE',  'EQ',    'NE',   'TRUE',  'FALSE', 
    'COMMENT',  # New token for comments
)

# Existing rules remain the same
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'    
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_AND = r'&&'
t_OR  = r'\|\|'
t_NOT = r'!'
t_LT  = r'<'
t_LE  = r'<='
t_GT  = r'>'
t_GE  = r'>='
t_EQ  = r'=='
t_NE  = r'!='

# Rule for comments
def t_COMMENT(t):
    r'%%.*'
    t.type = 'COMMENT'
    return t

# Existing rules continue...
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore comments and whitespace
t_ignore = ' \t'

# Existing error and utility functions remain the same
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractère illégal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
