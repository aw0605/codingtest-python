# 방문길이
# 다음 4가지 명령어로 이동 (U:위로 한칸, D: 아래로 한칸, L: 왼쪽으로 한칸, R: 오른쪽으로 한칸)
# (0,0)위치에서 시작 (-5,5),(-5,-5),(5,5),(5,-5)로 경계 위치
# 명령어 dirs가 매개변수로 주어질 때, 게임 캐릭터가 지나간 길 중 처음 걸어본 길의 길이를 구해서 반환하는 sol함수를 구현하세요
# (경계를 벗어나는 명령어는 무시, dirs는 string형이며 500이하 자연수)

dirs = input()

def valid_move(nx, ny):
    return 0 <= nx < 11 and 0 <= ny < 11

def next_location(x, y, dir):
    if dir == "U":
        nx, ny = x, y+1
    elif dir == "D":
        nx, ny = x, y-1
    elif dir == "L":
        nx, ny = x-1, y
    elif dir == "R":
        nx, ny = x+1, y
    return nx, ny

def sol(dir):
    x, y = 5, 5
    result = set()
    for dir in dirs:
        nx, ny = next_location(x, y, dir)
        if not valid_move(nx, ny):
            continue
        result.add((x, y, nx, ny))
        result.add((nx, ny, x, y))
        x, y = nx, ny
    print (int(len(result)/2))

sol(dir)