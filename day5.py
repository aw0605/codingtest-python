# <알고리즘 문제5, 시각>
# 정수N 입력 시, 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요
# (0 <= N <= 23)

h = int(input())
count3 = 0

for i in range(h + 1):
  for m in range(60):
    for s in range(60):
      if '3' in str(i) + str(m) + str(s):
        count3 += 1

print(count3)