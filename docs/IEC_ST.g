grammar IEC_ST;

options {
    language  = Python;
    backtrack = false;
    output    = AST;
    ASTLabelType=CommonTree;
}

@parser::header {
}

expression : xor_expression {'OR' xor_expression};

xor_expression : and_expression {'XOR' and_expression};

and_expression : comparison {('&' | 'AND') comparison};

comparison : equ_expression { ('=' | '<>') equ_expression};

equ_expression : add_expression {comparison_operator add_expression};

comparison_operator : '<' | '>' | '<=' | '>=';

add_expression : term {add_operator term};

add_operator : '+' | '-';

term : power_expression {multiply_operator power_expression};

multiply_operator : '*' | '/' | 'MOD';

power_expression : unary_expression {'**' unary_expression};

unary_expression : unary_operator? primary_expression;

unary_operator : '-' | 'NOT';

primary_expression : constant | enumerated_value | variable | '(' expression ')' | function_name '(' param_assignment {',' param_assignment} ')';

statement_list : statement ';' {statement ';'};

statement : NIL | assignment_statement |subprogram_control_statement | selection_statement | iteration_statement;

assignment_statement : variable ':=' expression;

subprogram_control_statement : fb_invocation | 'RETURN';

fb_invocation : fb_name '(' {param_assignment {',' param_assignment} }? ')';

param_assignment : ( {variable_name ':='}? expression) | ( 'NOT'? variable_name '=>' variable);

selection_statement : if_statement | case_statement;

if_statement : 'IF' expression 'THEN' statement_list {'ELSIF' expression 'THEN' statement_list} {'ELSE' statement_list}? 'END_IF';

case_statement : 'CASE' expression 'OF' case_element {case_element} {'ELSE' statement_list}? 'END_CASE';

case_element : case_list ':' statement_list;

case_list : case_list_element {',' case_list_element};

case_list_element : subrange | signed_integer | enumerated_value;

iteration_statement : for_statement | while_statement | repeat_statement | exit_statement;

for_statement : 'FOR' control_variable ':=' for_list 'DO' statement_list 'END_FOR';

control_variable : identifier;

for_list : expression 'TO' expression ['BY' expression];

while_statement : 'WHILE' expression 'DO' statement_list 'END_WHILE';

repeat_statement : 'REPEAT' statement_list 'UNTIL' expression 'END_REPEAT';

exit_statement : 'EXIT';
