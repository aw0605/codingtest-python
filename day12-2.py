# 10진수를 2진수로 변환하기
# 10진수를 입력받아 2진수로 변환해서 반환하는 sol()함수를 구현하세요

N = int(input())

def sol(N):
    stack = []
    result = ""
    
    while N != 0:
        stack.append(str(N % 2))
        N //= 2
    
    result = ''.join(reversed(stack))
    print (result)
    
sol(N)
