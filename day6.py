# <알고리즘 문제6, 왕실 나이트>
# 8X8 좌표 평면의 체스판의 나이트는 L자 형태로만 이동 가능, 체스판 밖으로는 나갈 수 없다.
# 다음 2가지 경우로 이동이 가능하다.
# 1, 수평으로 2칸 이동 + 수직으로 1칸 이동
# 2, 수직으로 2칸 이동 + 수평으로 1칸 이동
# 좌표 평면에서 나이트의 위치가 주어졌을 때, 나이트가 이동 가능한 경우의 수를 출력하는 프로그램을 작성하세요
# 행은 1 ~ 8, 열은 a ~ h로 표현

input = input()
x = int(input[1])
y = int(ord(input[0])) - int(ord('a')) + 1

routes = [(-2, 1), (-2, -1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2),(1, -2)]

possible = 0

for route in routes:
  nx = x + route[0]
  ny = y + route[1]
  if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
    possible += 1

print(possible)