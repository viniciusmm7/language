/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_PARSER_TAB_H_INCLUDED
# define YY_YY_PARSER_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    NUMBER = 258,                  /* NUMBER  */
    IDENTIFIER = 259,              /* IDENTIFIER  */
    MOVIE = 260,                   /* MOVIE  */
    WATCH = 261,                   /* WATCH  */
    LOOP = 262,                    /* LOOP  */
    SCENE = 263,                   /* SCENE  */
    DOES = 264,                    /* DOES  */
    NETFLIX = 265,                 /* NETFLIX  */
    PRIME_VIDEO = 266,             /* PRIME_VIDEO  */
    DISNEY_PLUS = 267,             /* DISNEY_PLUS  */
    HAVE = 268,                    /* HAVE  */
    ONLY = 269,                    /* ONLY  */
    BLURAY = 270,                  /* BLURAY  */
    ANY = 271,                     /* ANY  */
    STREAMING = 272,               /* STREAMING  */
    BETWEEN = 273,                 /* BETWEEN  */
    ALL = 274,                     /* ALL  */
    BELONGS = 275,                 /* BELONGS  */
    TO = 276,                      /* TO  */
    THE = 277,                     /* THE  */
    SAME = 278,                    /* SAME  */
    SAGA = 279,                    /* SAGA  */
    AS = 280,                      /* AS  */
    BETTER = 281,                  /* BETTER  */
    RATED = 282,                   /* RATED  */
    THAN = 283,                    /* THAN  */
    WORST = 284,                   /* WORST  */
    MAKE = 285,                    /* MAKE  */
    NEW = 286,                     /* NEW  */
    WITH = 287,                    /* WITH  */
    WRONG = 288,                   /* WRONG  */
    DIRECTOR = 289,                /* DIRECTOR  */
    SORRY = 290,                   /* SORRY  */
    WOULD = 291,                   /* WOULD  */
    BE = 292,                      /* BE  */
    NICER = 293,                   /* NICER  */
    WON = 294,                     /* WON  */
    OSCARS = 295,                  /* OSCARS  */
    LOST = 296,                    /* LOST  */
    FROM = 297,                    /* FROM  */
    PLOT = 298,                    /* PLOT  */
    TWIST = 299,                   /* TWIST  */
    REVERSE = 300,                 /* REVERSE  */
    SELECT = 301,                  /* SELECT  */
    ASSIGN = 302,                  /* ASSIGN  */
    COMMA = 303,                   /* COMMA  */
    SEMICOLON = 304,               /* SEMICOLON  */
    LPAREN = 305,                  /* LPAREN  */
    RPAREN = 306,                  /* RPAREN  */
    LBRACE = 307,                  /* LBRACE  */
    RBRACE = 308,                  /* RBRACE  */
    QUESTION = 309,                /* QUESTION  */
    NEWLINE = 310                  /* NEWLINE  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 16 "parser.y"

    int num;
    char *str;

#line 124 "parser.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif


extern YYSTYPE yylval;
extern YYLTYPE yylloc;

int yyparse (void);


#endif /* !YY_YY_PARSER_TAB_H_INCLUDED  */
