# <알고리즘 문제4, 상하좌우>
# (1,1)부터 (N,N)까지 NXN크기의 정사각형 공간에서 (1,1)을 시작점으로 서 있는 여행가는 상,하,좌,우로 이동이 가능
# 계획서에 띄어쓰기를 기준으로 L(왼쪽으로 한칸), R(오른쪽으로 한칸), U(위로 한칸), D(아래로 한칸) 중 하나의 문자가 반복적으로 적혀 있음
# 여행가가 최종적으로 도착할 지점의 좌표(X, Y)를 공백으로 구분하여 출력하세요
# (단, NXN을 벗어나는 움직임은 무시된다.)

n = int(input())
plans = input().split()
x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for move in plans:
    for i in range(len(move_type)):
        if move == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny
    
print(x,y)