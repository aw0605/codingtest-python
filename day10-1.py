# 행렬의 곱셈
# 2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 sol함수를 구현하세요
# (arr1,arr2의 행/열 길이는 2이상 100이하, arr1,arr2 데이터는 -10이상 20이하 자연수, 곱할 수 있는 배열만 주어집니다.)

arr1 = [[1,4],[3,2],[4,1]]
arr2 = [[3,3],[3,3]]

def sol(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    
    result = [[0] * c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
                
    print (result)

sol(arr1, arr2)
