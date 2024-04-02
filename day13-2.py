# 짝지어 제거하기
# 알파벳 소문자로 된 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾는다.
# 짝이 맟춰지면 제거한 뒤, 앞뒤로 문자열을 이어붙인다.
# 위 과정을 반복해 모든 문자열을 제거한다면 종료한다.
# 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행하면 1을 아니면 0을 반환하는 sol()함수를 구현하세요
# (문자열 길이: 1000000이하 자연수, 문자열은 모두 소문자)

S = input()

def sol(S):
    stack =[]
    for i in S:
        if stack and stack[-1] == i: stack.pop()
        else: stack.append(i)
    print (int(not stack))

sol(S)