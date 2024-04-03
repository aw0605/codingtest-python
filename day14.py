# 주식 가격
# 초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 반환하도록 sol()함수를 구현하세요
# (1 <= prices의 각 가격 <= 10000, 2 <= prices의 길이 <= 100000)

prices = list(map(int, input().split()))

def sol(prices):
    stack = []
    result = [0] * len(prices)
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        result[j] = len(prices)-1-j
    
    print (result)

sol(prices)        