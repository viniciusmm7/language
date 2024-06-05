%{
#include <iostream>
#include <string>
using namespace std;

extern "C" int yylex();
extern int yyparse();
extern FILE *yyin;
extern int yylineno;

void yyerror(const char *s);
%}

%locations

%union {
    int num;
    char *str;
}

%token <num> NUMBER
%token <str> IDENTIFIER

%token MOVIE
%token WATCH
%token LOOP
%token SCENE
%token DOES
%token NETFLIX
%token PRIME_VIDEO
%token DISNEY_PLUS
%token HAVE
%token ONLY
%token BLURAY
%token ANY
%token STREAMING
%token BETWEEN
%token ALL
%token BELONGS
%token TO
%token THE
%token SAME
%token SAGA
%token AS
%token BETTER
%token RATED
%token THAN
%token WORST
%token MAKE
%token NEW
%token WITH
%token WRONG
%token DIRECTOR
%token SORRY
%token WOULD
%token BE
%token NICER
%token WON
%token OSCARS
%token LOST
%token FROM
%token PLOT
%token TWIST
%token REVERSE
%token SELECT
%token ASSIGN
%token COMMA
%token SEMICOLON
%token LPAREN
%token RPAREN
%token LBRACE
%token RBRACE
%token QUESTION
%token NEWLINE

%%

PROGRAM:
    BLOCK
    ;

BLOCK:
    STATEMENT
    | BLOCK STATEMENT
    ;

STATEMENT:
    NEWLINE
    | IDENTIFIER ASSIGN BOOL_EXPRESSION SEMICOLON
    | MOVIE IDENTIFIER SEMICOLON
    | MOVIE IDENTIFIER ASSIGN BOOL_EXPRESSION SEMICOLON
    | WATCH MOVIE BOOL_EXPRESSION SEMICOLON
    | LOOP SCENE BOOL_EXPRESSION LBRACE BLOCK RBRACE
    | DOES STREAMING_OPTIONS HAVE BOOL_EXPRESSION QUESTION LBRACE BLOCK RBRACE
    | DOES STREAMING_OPTIONS HAVE BOOL_EXPRESSION QUESTION LBRACE BLOCK RBRACE ONLY BLURAY LBRACE BLOCK RBRACE
    ;

STREAMING_OPTIONS:
    NETFLIX
    | PRIME_VIDEO
    | DISNEY_PLUS
    ;

BOOL_EXPRESSION:
    BOOL_TERM
    | ANY STREAMING BETWEEN BOOL_TERM BOOL_EXPRESSION_RECURSION
    ;

BOOL_EXPRESSION_RECURSION:
    COMMA BOOL_TERM
    | COMMA BOOL_TERM BOOL_EXPRESSION_RECURSION
    ;

BOOL_TERM:
    RELATIONAL_EXPRESSION
    | ALL STREAMING BETWEEN RELATIONAL_EXPRESSION BOOL_TERM_RECURSION
    ;

BOOL_TERM_RECURSION:
    COMMA RELATIONAL_EXPRESSION
    | COMMA RELATIONAL_EXPRESSION BOOL_TERM_RECURSION
    ;

RELATIONAL_EXPRESSION:
    EXPRESSION
    | EXPRESSION BELONGS TO THE SAME SAGA AS RELATIONAL_EXPRESSION
    | EXPRESSION BETTER RATED THAN RELATIONAL_EXPRESSION
    | EXPRESSION WORST RATED THAN RELATIONAL_EXPRESSION
    ;

EXPRESSION:
    TERM
    | TERM MAKE NEW MOVIE WITH EXPRESSION
    | TERM WRONG DIRECTOR SORRY EXPRESSION
    ;

TERM:
    FACTOR
    | FACTOR WON OSCARS WITH FACTOR
    | FACTOR LOST OSCARS FROM FACTOR
    ;

FACTOR:
    NUMBER
    | IDENTIFIER
    | FACTOR_OPTIONS
    | LPAREN BOOL_EXPRESSION RPAREN
    | SELECT MOVIE LPAREN RPAREN
    ;

FACTOR_OPTIONS:
    PLOT FACTOR
    | PLOT TWIST FACTOR
    | REVERSE MOVIE FACTOR
    ;

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>.mnl" << endl;
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");

    if (!input_file) {
        cerr << "Error: Could not open file " << argv[1] << endl;
        return 1;
    }

    yyin = input_file;

    if (!yyparse()) {
        cout << "Parsing successful!" << endl;
    } else {
        cout << "Parsing failed!" << endl;
    }

    return 0;
}

void yyerror(const char *s) {
    cerr << "Error: " << s << " at line " << yylineno << endl;
    exit(1);
}
