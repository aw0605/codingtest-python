# 실패율
# 실패율 정의: 스테이지에 도달했으나 아직 클리어하지 못한 프레이어 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 수가 N, 게임 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열 stages가 주어질 때,
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 반환하는 sol함수를 구현하세요
# (스테이지개수는 1이상 500이하 자연수, stages길이는 1이상 200000이하, stages에는 1이상 N+1이하 자연수 존재(각 자연수는 현재 도전 중인 스테이지 번호, N+1은 마지막 스테이지), 실패율 같은 스테이지가 있으면 작은 번호 스테이지가 먼저, 스테이지 도달한 유저 없으면 해당 스테이지의 실패율은 0)

N = int(input())
stages = list(map(int, input().split()))

def sol(N, stages):
    user = [0] * (N+2)
    for i in stages:
        user[i] += 1
        
    fails = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if user[i] == 0:
            fails[i] = 0
        else:
            fails[i] = user[i] / total
            total -= user[i]
    
    result = sorted(fails, key = lambda x: fails[x], reverse=True)
    print (result)

sol(N, stages)

