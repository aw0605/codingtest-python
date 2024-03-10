# 배열 정렬하기
# 정수 배열을 정렬해서 반환하는 solution함수를 완성하세요
# (정수 배열 길이는 2이상 10^5이하, 정수 배열 각 데이터 값은 -100000이상 100000이하)

arr = list(map(int,input().split()))

def sol(arr):
    arr.sort()
    print(arr)

sol(arr)