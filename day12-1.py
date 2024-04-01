# 괄호 짝 맞추기
# 열린 괄호'('나 닫힌 괄호')'가 뒤섞인 문자열이 주어졌을 때,
# 소괄호가 정상적으로 열고 닫혔는지 판별해서 정상적으로 열고 닫혔다면 True를, 아니라면 False를 반환하는 sol()함수를 구현하세요
# (열린 괄호는 가장 가까운 닫힌 괄호와 만나면 상쇄된다.
# 열린 괄호가 먼저, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 상쇄 조건 만족한다.
# 더 상쇄할 괄호 없을 때까지 반복한다.)

input = input()

def sol(input):
    result = []
    
    for str in input:
        if str == "(":
            result.append(str)
        elif str == ")":
            if not result:
                print (False)
            else:
                result.pop()
    
    if result:
        print (False)
    else:
        print (True)

sol(input)
