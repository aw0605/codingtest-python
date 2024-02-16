# <알고리즘 문제1, 1이 될 때까지>
# 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
# 1, N에서 1을 뺍니다.
# 2, N을 K로 나눕니다. (단, 이 연산은 N이 K로 나누어 떨어질 때만 선택 가능)
# 자연수 N과 K가 주어질 때, N이 1이 될 때까지 1번/2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성하세요

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    n //= k
    result += 1

result += (n - 1)
print(result)
