%{
#include <iostream>
#include <string>
using namespace std;

void yyerror(const char *s);
int yylex();
%}

%locations

%union {
    int num;
    char *str;
}

%token <num> NUMBER
%token <str> IDENTIFIER

%token MOVIE
%token WATCH_MOVIE
%token LOOP_SCENE
%token DOES
%token NETFLIX
%token PRIME_VIDEO
%token DISNEY_PLUS
%token HAVE
%token ONLY_BLURAY
%token ANY_STREAMING_BETWEEN
%token ALL_STREAMING_BETWEEN
%token BELONGS_TO_THE_SAME_SAGA_AS
%token BETTER_RATED_THAN
%token WORST_RATED_THAN
%token MAKE_NEW_MOVIE_WITH
%token WRONG_DIRECTOR_SORRY
%token WOULD_BE_NICER_WITH
%token WON_OSCARS_WITH
%token LOST_OSCARS_FROM
%token PLOT
%token PLOT_TWIST
%token REVERSE_MOVIE
%token SELECT_MOVIE
%token EQUALS
%token COMMA
%token SEMICOLON
%token LPAREN
%token RPAREN
%token LBRACE
%token RBRACE
%token QUESTION
%token NEWLINE

%%

PROGRAM: BLOCK
    ;

BLOCK:
    STATEMENT
    | BLOCK STATEMENT
    ;

STATEMENT:
    NEWLINE
    | IDENTIFIER EQUALS BOOL_EXPRESSION SEMICOLON
    | MOVIE IDENTIFIER (EQUALS BOOL_EXPRESSION)? SEMICOLON
    | WATCH_MOVIE BOOL_EXPRESSION SEMICOLON
    | LOOP_SCENE BOOL_EXPRESSION LBRACE BLOCK RBRACE
    | DOES (NETFLIX | PRIME_VIDEO | DISNEY_PLUS) HAVE BOOL_EXPRESSION QUESTION LBRACE BLOCK RBRACE (ONLY_BLURAY LBRACE BLOCK RBRACE)?
    ;

BOOL_EXPRESSION:
    ANY_STREAMING_BETWEEN BOOL_TERM COMMA BOOL_TERM
    ;

BOOL_TERM:
    ALL_STREAMING_BETWEEN RELATIONAL_EXPRESSION
    ;

RELATIONAL_EXPRESSION:
    EXPRESSION (BELONGS_TO_THE_SAME_SAGA_AS | BETTER_RATED_THAN | WORST_RATED_THAN) EXPRESSION
    | EXPRESSION
    ;

EXPRESSION:
    TERM (MAKE_NEW_MOVIE_WITH | WRONG_DIRECTOR_SORRY | WOULD_BE_NICER_WITH) TERM
    | TERM
    ;

TERM:
    FACTOR (WON_OSCARS_WITH | LOST_OSCARS_FROM) FACTOR
    | FACTOR
    ;

FACTOR:
    NUMBER
    | IDENTIFIER
    | (PLOT | PLOT_TWIST | REVERSE_MOVIE) FACTOR
    | LPAREN BOOL_EXPRESSION RPAREN
    | SELECT_MOVIE
    ;

IDENTIFIER:
    [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUMBER:
    [0-9]+
    ;

NEWLINE:
    '\n'
    ;

%%

int main() {
    if (!yyparse()) {
        cout << "Parsing successful!" << endl;
    } else {
        cout << "Parsing failed!" << endl;
    }
    return 0;
}

void yyerror(const char *s) {
    cerr << "Error: " << s << endl;
}
