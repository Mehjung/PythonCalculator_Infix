import operator

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calculate(expression):
    stack = []
    for char in expression.split():
        if char in operators:
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            result = operators[char](op1, op2)
            stack.append(result)
        else:
            stack.append(char)
    return stack.pop()
    
def infix_to_postfix(expression):
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    postfix = []
    operand = ""
    for char in expression:
        if char.isdigit() or char == '.':
            operand += char
        else:
            if operand:
                postfix.append(operand)
                operand = ""
            if char in '+-*/^':
                while stack and precedence[char] <= precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
    if operand:
        postfix.append(operand)
    while stack:
        postfix.append(stack.pop())
    return " ".join(postfix)

def time2Float(time):
    time = time.split(':')
    return float(time[0]) + float(time[1])/60 if len(time) == 2 else float(time[0])

def float2Time(f):
    h = int(f)
    m = int(round((f - h) * 60,0))
    return str(h) + ':' + f'{m:02d}'


def replaceTimeWithFloat(expression):
    time = ""
    newExpression = ""
    for index, char in enumerate(expression):
        if char.isdigit() and index != len(expression)-1:
            time += char
            continue
        if char in ':.,':
            time += ':'
            continue
        if index == len(expression)-1:
            time += char
        if time:
            newExpression += str(time2Float(time))
            time = ""
        newExpression += char if index != len(expression)-1 else ''
    return newExpression

def removeWhiteSpace(expression):
    return ''.join(expression.split())

calc = lambda exp : float2Time(calculate(infix_to_postfix(replaceTimeWithFloat(removeWhiteSpace(exp)))))


