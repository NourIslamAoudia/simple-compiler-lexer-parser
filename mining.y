%{
#include <stdio.h>%{
#include <stdio.h>
#include <stdlib.h>
#include "mining.tab.h"

extern int yylex();    // Lexical analyzer function
extern FILE *yyin;     // Input file
void yyerror(const char *s);
%}

%union {
    int int_val;
    float float_val;
    char* str_val;
}

%token VAR_GLOBAL DECLARATION_TOKEN INSTRUCTION_TOKEN COMMENT INTEGER FLOAT CHAR CONST IF ELSE FOR READ WRITE
%token PLUS MINUS MUL DIV AND OR NOT GT LT GE LE EQ NEQ
%token IDF NUMBER FLOAT_NUMBER TYPE STRING

%type <int_val> expression
%type <str_val> variable
%type <float_val> float_expression

%%

program:
    VAR_GLOBAL '{' DECLARATIONS '}' INSTRUCTIONS
;

DECLARATIONS:
    declaration_list
;

declaration_list:
    declaration_list declaration
;
#include <stdlib.h>
#include "mining.tab.h"

extern int yylex();    // Lexical analyzer function
extern FILE *yyin;     // Input file
void yyerror(const char *s);
%}

%union {
    int int_val;
    float float_val;
    char* str_val;
}

%token VAR_GLOBAL DECLARATION INSTRUCTION COMMENT INTEGER FLOAT CHAR CONST IF ELSE FOR READ WRITE
%token PLUS MINUS MUL DIV AND OR NOT GT LT GE LE EQ NEQ
%token IDF NUMBER FLOAT_NUMBER TYPE STRING

%type <int_val> expression
%type <str_val> variable
%type <float_val> float_expression

%%

program:
    VAR_GLOBAL '{' DECLARATIONS '}' INSTRUCTIONS
;

DECLARATION:
    declaration_list
;

declaration_list:
    declaration_list declaration
    | declaration
;

declaration:
    TYPE variable_list ';'
;

variable_list:
    variable_list ',' variable
    | variable
;

variable:
    IDF
;

INSTRUCTION:
    instruction_list
;

instruction_list:
    instruction_list instruction
    | instruction
;

instruction:
    assignment
    | condition
    | loop
    | input_output
;

assignment:
    IDF '=' expression ';'
;

expression:
    NUMBER
    | FLOAT_NUMBER
    | variable
    | expression PLUS expression
    | expression MINUS expression
    | expression MUL expression
    | expression DIV expression
;

condition:
    IF '(' expression ')' '{' INSTRUCTIONS '}' ELSE '{' INSTRUCTIONS '}'
;

loop:
    FOR '(' assignment ':' expression ':' expression ')' '{' INSTRUCTIONS '}'
;

input_output:
    READ '(' variable ')'
    | WRITE '(' string_expression ')'
;

string_expression:
    STRING
    | variable
    | string_expression PLUS string_expression
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(int argc, char** argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror("Error opening file");
            return 1;
        }
    }
    
    yyparse();  // Start parsing
    return 0;
}
