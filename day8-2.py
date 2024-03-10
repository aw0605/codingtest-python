# 배열 제어하기
# 정수 배열을 받아서 중복값을 제거하고 배열 데이터를 내림차순으로 정렬 및 반환하는 sol함수를 구현하세요
# (배열의 길이는 2이상 1000이하, 각 배열 데이터 값은 -100000이상 100000이하)

arr = list(map(int,input().split()))

def sol(arr):
    answer_arr = list(set(arr))
    answer_arr.sort(reverse=True)                                                                                                                                                      
    print(answer_arr)

sol(arr)