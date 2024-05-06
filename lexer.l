%{
#include "y.tab.h"
%}

DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT}|_)*
NUMBER      {DIGIT}+
SPACE       [ ]
COMMENT     \/\/[^\n]*
NEWLINE     [\n]

%%

"movie"                         { return MOVIE; }
"watch movie"                   { return WATCH_MOVIE; }
"loop scene"                    { return LOOP_SCENE; }
"does"                          { return DOES; }
"Netflix"                       { return NETFLIX; }
"PrimeVideo"                    { return PRIME_VIDEO; }
"Disney+"                       { return DISNEY_PLUS; }
"have"                          { return HAVE; }
"only Bluray"                   { return ONLY_BLURAY; }
"any streaming between"         { return ANY_STREAMING_BETWEEN; }
"all streaming between"         { return ALL_STREAMING_BETWEEN; }
"belongs to the same saga as"   { return BELONGS_TO_THE_SAME_SAGA_AS; }
"better rated than"             { return BETTER_RATED_THAN; }
"worst rated than"              { return WORST_RATED_THAN; }
"make new movie with"           { return MAKE_NEW_MOVIE_WITH; }
"wrong director, sorry"         { return WRONG_DIRECTOR_SORRY; }
"would be nicer with"           { return WOULD_BE_NICER_WITH; }
"won oscars with"               { return WON_OSCARS_WITH; }
"lost oscars from"              { return LOST_OSCARS_FROM; }
"plot"                          { return PLOT; }
"plot twist"                    { return PLOT_TWIST; }
"reverse movie"                 { return REVERSE_MOVIE; }
"select movie"                  { return SELECT_MOVIE; }
"="                             { return EQUALS; }
","                             { return COMMA; }
";"                             { return SEMICOLON; }
"("                             { return LPAREN; }
")"                             { return RPAREN; }
"{"                             { return LBRACE; }
"}"                             { return RBRACE; }
"?"                             { return QUESTION; }
{NEWLINE}                       { return NEWLINE; }
{NUMBER}                        { yylval.num = atoi(yytext); return NUMBER; }
{IDENTIFIER}                    { yylval.str = strdup(yytext); return IDENTIFIER; }
{SPACE}                         ;
{COMMENT}                       ;

%%

int yywrap() {
    return 1;
}
