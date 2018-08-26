"""Lexer tokens
"""

EOF = 'EOF'

INTEGER = 'INTEGER'
INTEGER_CONST = 'INTEGER_CONST'
REAL = 'REAL'
REAL_CONST = 'REAL_CONST'
STRING = 'STRING'
STRING_CONST = 'STRING_CONST'
BOOLEAN = 'BOOLEAN'
BOOLEAN_CONST = 'BOOLEAN_CONST'

TRUE, FALSE = ('TRUE', 'FALSE')

LPAREN, RPAREN, = ('(', ')',)
PLUS, MINUS = ('PLUS', 'MINUS')
MUL = 'MUL'
FLOAT_DIV, INTEGER_DIV = ('FLOAT_DIV', 'INTEGER_DIV')

ID = 'ID'
ASSIGN = 'ASSIGN'
SEMI, COLON, DOT, COMMA, = ('SEMI', 'COLON', 'DOT', 'COMMA')

NE, EQ, LT, LTE, GT, GTE = ('NE', 'EQ', 'LT', 'LTE', 'GT', 'GTE')

IF, ELSE, THEN = ('IF', 'ELSE', 'THEN')
FOR, TO, DO = ('FOR', 'TO', 'DO')

BEGIN, END = ('BEGIN', 'END')
PROGRAM = 'PROGRAM'
WRITELN = 'WRITELN'
VAR = 'VAR'
PROCEDURE = 'PROCEDURE'
