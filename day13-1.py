# 괄호 회전하기
# 대괄호, 중괄호, 소괄호로 이루어진 문자열 s가 매개변수로 주어진다.
# s를 왼쪽으로 x(0 <= x < s의 길이)칸만큼 회전시켰을 때, s가 올바른 괄호 문자열이 되게 하는 x의 개수 반환하는 sol()함수를 구현하세요
# 올바른 괄호 문자열은 다음과 같다.
# 1, "()", "[]", "{}"
# 2, 먄약 A가 올바른 괄호 문자열이라면 (A),[A],{A}도 올바른 괄호 문자열
# 3, 만약 A,B가 올바른 괄호 문자열이라면, AB도 돌바른 괄호 문자열
# (1 <= s의 길이 <= 1000)

s = input()

def sol(s):
    result = 0
    stack = []
    for i in range(len(s)):
        for j in range(len(s)):
            c = s[(i+j) % len(s)]
            if c == "(" or c == "[" or c == "{": stack.append(c)
            else: 
                if not stack: break
                if c == ")" and stack[-1] == "(": stack.pop()
                elif c == "]" and stack[-1] == "[": stack.pop()
                elif c == "}" and stack[-1] == "{": stack.pop()
                else: break
        else:
            if not stack: result += 1
    print (result)

sol(s)