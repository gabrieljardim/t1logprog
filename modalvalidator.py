def is_terminal(exp) :
    if exp == 'T' or exp == 'F' :
        return True
    else :
        return False

def not_func(rs):
    if rs == 'T':
        return 'F'
    else :
        return 'T'

def and_func(ls, rs) :
    if ls == 'T' and rs == 'T' :
        return 'T'
    else :
        return 'F'

def or_func(ls, rs) :
    if ls == 'T' or rs == 'T' :
        return 'T'
    else :
        return 'F'

def ifthen_func(ls, rs) :
    if ls == 'T' and rs == 'F' :
        return 'F'
    else :
        return 'T'


def evaluate_not_token(position, expression, variableSet):
    if (position+1) < len(expression) :
        variableValue = variableSet[expression[position+1]]
        expression_first = expression[:position]
        expression_second = expression[position+2:]
        return (expression_first + not_func(variableValue) + expression_second)

def evaluate_and_token(position, expression, variableSet):
    if (position+1) < len(expression) and (position-1) >= 0 :
        right_side_variable_value = variableSet[expression[position+1]]
        left_side_variable_value = variableSet[expression[position-1]]
        expression_first = expression[:position-1]
        expression_second = expression[position+2:]
        return (expression_first + and_func(left_side_variable_value, right_side_variable_value) + expression_second)

def evaluate_or_token(position, expression, variableSet):
    if (position+1) < len(expression) and (position-1) >= 0 :
        right_side_variable_value = variableSet[expression[position+1]]
        left_side_variable_value = variableSet[expression[position-1]]
        expression_first = expression[:position-1]
        expression_second = expression[position+2:]
        return (expression_first + or_func(left_side_variable_value, right_side_variable_value) + expression_second)

def evaluate_ifthen_token(position, expression, variableSet):
    if (position+2) < len(expression) and (position-1) >= 0 :
        right_side_variable_value = variableSet[expression[position+2]]
        left_side_variable_value = variableSet[expression[position-1]]
        expression_first = expression[:position-1]
        expression_second = expression[position+3:]
        return (expression_first + ifthen_func(left_side_variable_value, right_side_variable_value) + expression_second)

def find_not_token(expression):
    return expression.find('!')

def find_and_token(expression):
    return expression.find('&')

def find_or_token(expression):
    return expression.find('|')

def find_ifthen_token(expression):
    return expression.find('->')

def process_not(expression, variableSet):
    while(True):
        pos = find_not_token(expression)
        if pos == -1:
            break
        expression = evaluate_not_token(pos, expression, variableSet)
    return expression

def process_and(expression, variableSet):
    while(True):
        pos = find_and_token(expression)
        if pos == -1:
            break
        expression = evaluate_and_token(pos, expression, variableSet)
    return expression

def process_or(expression, variableSet):
    while(True):
        pos = find_or_token(expression)
        if pos == -1:
            break
        expression = evaluate_or_token(pos, expression, variableSet)
    return expression

def process_ifthen(expression, variableSet):
    while(True):
        pos = find_ifthen_token(expression)
        if pos == -1:
            break
        expression = evaluate_ifthen_token(pos, expression, variableSet)
    return expression

variableSet = {
    'p':'T',
    'q':'F',

    #do not modify
    'F':'F',
    'T':'T'
}

expression = "p|q&!p->q&!q->p"


expression = process_not(expression, variableSet)
print("EtapaNot: " + expression)
expression = process_and(expression, variableSet)
print("EtapaAnd: " + expression)
expression = process_or(expression, variableSet)
print("EtapaOr: " + expression)
expression = process_ifthen(expression, variableSet)
print("EtapaIfthen: " + expression)

print(expression)