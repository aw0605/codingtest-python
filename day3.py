# <알고리즘 문제3, 모험가 길드>
# 모험가 길드에서 N명의 모험가를 대상으로 공포도를 측정,
# 안전하게 그룹을 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 모험이 가능
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요
# (모든 모험가를 특정한 그룹에 넣을 필요는 없다.)

n = int(input())
x = list(map(int, input().split()))

groups = 0
people = 0

x.sort()

for i in x:
  people += 1
  if people >= i:
    groups += 1
    people = 0

print(groups)