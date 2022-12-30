"""
-----------------  Question  -----------------
어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다.
예를 들어, n=22이면 다음과 같은 수열이 만들어진다.
- 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다.
위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다.
i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.
----------------------------------------------
"""
"""
=============================================================================
과제 1. 입력 값(n)이 40일때, 사이클 길이를 구하시오.
       - input = 40
       - 출력 : 9
=============================================================================
"""
print("======과제1======")

n = int(input("input=")) #변수n을 설정하여 input값을 입력받은 후 정수값으로 변환해주었습니다.

cycle = 1
while True:             #while문을 사용하여 무한반복
    if n%2==0:          
        n = n//2        # n이 짝수일 때 n//2 
        cycle = cycle+1 # while 조건식이 실행 될때마다 cycle에 1씩 추가
        if n ==1:       # n이 1이 나오면 while 무한루프 탈출
            break
    
    elif n%2==1:        
        n = n*3+1       # n이 홀수일 때 n*3+1
        cycle = cycle+1
        if n ==1: 
            break   
    
print(cycle)


"""
=============================================================================
과제 2. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
       - start = 1
       - end = 10
       - 출력 : 20
=============================================================================
"""

print("======과제2======")

i = 1
j = 10
n_list = []

for n in range(i,j+1):      # 1부터 10까지의 싸이클을 전부 계산하기 위해 반복문을 하나 더 추가 
    cycle = 1
    while True:
        if n%2==0:
            n = n//2
            cycle = cycle+1
            if n ==1:
                break
        
        elif n%2==1:
            n = n*3+1
            cycle = cycle+1
            if n ==1:
                break
        
    n_list.append(cycle)    # 싸이클 값을 n_list에 추가

n_list.sort(reverse=True)   # n_list를 내림차순 정리하여 가장 큰 0번째항을 출력
print(n_list[0])


"""
=============================================================================
과제 3. i와 j라는 두개의 수가 주어졌을때, i와 j사이의 모든 수에 대한 최대 사이클 길이(i와 j도 사이클 길이에 포함됨)를 구하라.
       - start_num_list = [1, 100, 201, 900]
       - end_num_list = [10, 200, 210, 1000] 
       - 출력 : [20, 125, 89, 174]
=============================================================================
"""

print("======과제3======")

i = [1, 100, 201, 900]
j = [10, 200, 210, 1000]
result_list= []

for k in range(4):                  # 입력값이 리스트로 바뀌었기 때문에 각각의 요소들을 전부 계산하기 위한 for 문 추가

    n_list = []
    for n in range(i[k],j[k]+1):
        cycle = 1
        while True:
            if n%2==0:
                n = n//2
                cycle = cycle+1
                if n ==1:
                    break
            
            elif n%2==1:
                n = n*3+1
                cycle = cycle+1
                if n ==1:
                    break
            
        n_list.append(cycle)

    n_list.sort(reverse=True)
    result_list.append(n_list[0])

print(*result_list)