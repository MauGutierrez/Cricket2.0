import ply.lex

reserved = {
	"if" 		: "IF",
	"else"		: "ELSE",
	"while"		: "WHILE",
	"for"		: "FOR",
	"read"		: "READ",
	"print"		: "PRINT",
	"function"	: "FUNCTION",
	"main"		: "MAIN",
	"return"	: "RETURN",
	"program"	: "PROGRAM",
	"int"		: "INT",
	"float"		: "FLOAT",
	"arrint"	: "ARRINT",
}

tokens = ['NEQ', 'EQ', 'GTEQ', 'LTEQ', 'AND', 'OR', 'ID', 'NUMINT', 'NUMFLOAT', 
		  'CTES', 'SEMMICOLON', 'RPAREN', 'LPAREN', 'RSQUARE', 'LSQUARE', 'RKEY',
		  'LKEY', 'LT', 'GT', 'PLUS', 'MINUS', 'TIMES', 'DIVISION', 'ASSIGN', 'COMMA'] + list(reserved.values())


t_ignore		= ' \t'
t_NUMINT		= r'[0-9]+'
t_NUMFLOAT		= r'[0-9]+\.[0-9]+'
t_CTES			= r'".*"'
t_OR			= r'\|\|'
t_AND			= r'\&\&'
t_NEQ			= r'!='
t_EQ			= r'=='
t_GTEQ			= r'>='
t_LTEQ			= r'<='
t_PLUS			= r'\+'
t_MINUS			= r'-'
t_TIMES			= r'\*'
t_DIVISION		= r'/'
t_ASSIGN		= r'='
t_LT			= r'<'
t_GT			= r'>'
t_LPAREN		= r'\('
t_RPAREN		= r'\)'
t_LSQUARE		= r'\['
t_RSQUARE		= r'\]'
t_LKEY			= r'\{'
t_RKEY			= r'\}'
t_COMMA			= r'[,]'
t_SEMMICOLON	= r';'

#ID Definition
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

#Next Line definition
def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

#Errors definition
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

#Build the lexer
import ply.lex as lex
lex.lex()