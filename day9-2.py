# 모의고사
# 수포자 3인방이 문제를 찍는 방법은 다음과 같다.
# 수포자1: 1,2,3,4,5,1,2,3,4,5,...
# 수포자2: 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5,...
# 수포자3: 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5,...
# 1번부터 마지막 문제까지 순서대로의 정답 배열 answers가 주어졌을 때,
# 가장 문제를 많이 맞힌 사람이 누구인지 배열에 담아 반환하는 sol함수를 구현하세요
# (시험은 최대 10000문제, 문제정답은 1부터 5까지, 가장 높은 점수 받은 사람이 여럿이라면 오름차순으로 정렬해서 반환)

answers = list(map(int, input().split()))

def sol(answers):
    marks = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    scores = [0] * 3
    for i, answer in enumerate(answers):
        for j, mark in enumerate(marks):
            if answer == mark[i % len(mark)]:
                scores[j] += 1
    max_score = max(scores)
    highest_scores = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i+1)
    print(highest_scores)

sol(answers)