def is_terminal(exp) :
    if exp == 'T' or exp == 'F' :
        return True
    else :
        return False

def not_func(op):
    if op == 'T':
        return 'F'
    else :
        return 'T'

def or_func(ls, rs) :
    if ls == 'T' or rs == 'T' :
        return 'T'
    else :
        return 'F'

def or_and(ls, rs) :
    if ls == 'T' and rs == 'T' :
        return 'T'
    else :
        return 'F'

def find_not_token(expression):
    return expression.find('!')

def process_not_token(position, expression, variableSet):
    if (position+1) < len(expression) :
        variableValue = variableSet[expression[position+1]]
        expression_first = expression[:position]
        expression_second = expression[position+2:]
        return (expression_first + not_func(variableValue) + expression_second)

















#// process_all_nots
#//process_e
#//process

variableSet = {
    'p':'T',
    'q':'F'
}

expression = "p|q&!p"


pos = find_not_token(expression)
if pos!=-1:
    resultStr = process_not_token(pos, expression, variableSet)

print(expression)
print(resultStr)



#print(or_func('F', 'F'))