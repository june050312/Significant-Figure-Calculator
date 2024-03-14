import decimal

def getFloat(x):
    numList = list(x)
    flag = 0
    cnt = 0
    if int(float(x)) == 0:
        for i in numList:
            if i != '0' and i != '.':
                flag = 1
            if flag:
                cnt += 1
    else:
        for i in numList:
            cnt += 1
        cnt -= 1
    return cnt

def getSignificantFigure(x, y):
    len_x = getFloat(x)
    len_y = getFloat(y)
    if len_x < len_y:
        return len_x
    else:
        return len_y

def getDecimal(x):
    numList = list(x)
    point = numList.index('.')
    return len(numList[point + 1:])

def getDecimalAmount(x, y):
    len_x = getDecimal(x)
    len_y = getDecimal(y)
    if len_x < len_y:
        return len_x
    else:
        return len_y
    
def calculate(a, b, op):
    significantFigure = getSignificantFigure(a, b)
    decimalAmount = getDecimalAmount(a, b)

    a, b = decimal.Decimal(a), decimal.Decimal(b)
    result = 0

    if op == '+' or op == '-':
        if op == '+':
            result = a + b
        else:
            result = a - b
        return float(round(result, decimalAmount))
    elif op == '*' or op == '/':
        if op == '*':
            result = a * b
        else:
            result = a / b
        return float(round(result, significantFigure - len(str(int(result)))))
    else:
        return 'Operand Error'