class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for tok in tokenList:
        if tok in prec:
            if tok == '(' or opStack.isEmpty():
                pass
            else:
                while prec[opStack.peek()] >= prec[tok]:
                    postfixList.append(opStack.pop())
                    if opStack.isEmpty():
                        break
            opStack.push(tok)
        elif tok == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            postfixList.append(tok)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
                    

    return postfixList


def postfixEval(tokenList):
    op = ['+', '-', '*', '/']
    evalStack = ArrayStack()
    for tok in tokenList:
        if tok in op:
            v2 = evalStack.pop()
            v1 = evalStack.pop()
            if tok == '+':
                evalStack.push(v1+v2)
            elif tok == '-':
                evalStack.push(v1-v2)
            elif tok == '*':
                evalStack.push(v1*v2)
            elif tok == '/':
                evalStack.push(v1/v2)
        else:
            evalStack.push(tok)
    
    
    return evalStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val