'''
유효숫자 계산기
1. 두 숫자의 유효숫자가 얼마인지 파악하기 <- 부동소수점으로 해결
2. 두 숫자 중 작은 유효숫자를 구한다
3. 계산
    3-1. 곱셈과 나눗셈의 경우 작은 유효숫자와 유효숫자를 맞춘다
    3-2. 더하기와 빼기의 경우 소수점 아래 자리수가 가장 작은 값과 소수점 아래 숫자가 같게 한다
'''
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

print('측정된 모든 숫자를 입력해주세요.')
a = input()
b = input()
print('+, -, *, / 중에 입력해주세요.')
op = input()

significantFigure = getSignificantFigure(a, b)
decimalAmount = getDecimalAmount(a, b)

a, b = decimal.Decimal(a), decimal.Decimal(b)
result = 0

if op == '+' or op == '-':
    if op == '+':
        result = a + b
    else:
        result = a - b
    print(round(result, decimalAmount))
elif op == '*' or op == '/':
    if op == '*':
        result = a * b
    else:
        result = a / b
    print(round(result, significantFigure - len(str(int(result)))))
else:
    print('Operand Error')