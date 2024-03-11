# 두 개 뽑아서 더하기
# 정수 배열 numbers가 주어졌을 때, numbers에서 서로 다른 인덱스의 2개 수를 뽑아서 더했을 때 만들 수 있는
# 모든 수를 배열에 오름차순으로 담아 반환하는 sol함수 완성하세요
# (numbers길이는 2이상 100이하, numbers 모든 수는 0이상 100이하)

numbers = list(map(int,input().split()))

def sol(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result.append(numbers[i] + numbers[j])
    result = sorted(set(result))
    print(result)

sol(numbers)

