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
        if char.isdigit():
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

calc = lambda exp : calculate(infix_to_postfix(exp))

print(calc("(3+12)*3/15"))

