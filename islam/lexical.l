%{
#include <stdio.h>
%}

/* Définition des tokens */
DIGIT           [0-9]
LETTER          [a-zA-Z]
ID              {LETTER}({LETTER}|{DIGIT})*
NUMBER          {DIGIT}+

%%

"if"            { printf("KEYWORD IF\n"); }
"else"          { printf("KEYWORD ELSE\n"); }
"for"           { printf("KEYWORD FOR\n"); }
"while"         { printf("KEYWORD WHILE\n"); }
"do"            { printf("KEYWORD DO\n"); }
{ID}            { printf("IDENTIFIER: %s\n", yytext); }
{NUMBER}        { printf("NUMBER: %s\n", yytext); }
"+"             { printf("PLUS\n"); }
"-"             { printf("MINUS\n"); }
"*"             { printf("MULTIPLY\n"); }
"/"             { printf("DIVIDE\n"); }
"("             { printf("LEFT PARENTHESIS\n"); }
")"             { printf("RIGHT PARENTHESIS\n"); }
[ \t\n]         ;  // Ignorer les espaces blancs
.               { printf("UNKNOWN CHARACTER: %s\n", yytext); }

%%

/* Fonction principale */
int main() {
    yylex();  // Lance l'analyse lexicale
    return 0;
}

/* Définition de yywrap */
int yywrap() {
    return 1;
}
