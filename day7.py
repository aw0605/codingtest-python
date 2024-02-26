# <알고리즘 문제7, 문자 재정렬>
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열S가 입력값으로 주어졌을 때,
# 모든 알파벳을 오름차순으로 정렬해서 출력하고 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
# (1 <= S 길이 <= 10000))

input = input()

alpha = []
num = 0

for i in input:
  if i.isalpha():
    alpha.append(i)
  else:
    num += int(i)
alpha.sort()

if num != 0:
  alpha.append(str(num))

print(''.join(alpha))
