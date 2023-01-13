#========================================================================
#앞뒤가 같은 수는 바로 쓴 값과 거꾸로 쓴 값이 같은 수이다. 다음과 같은 예를 들 수 있다.
#1
#44
#101
#2002
#8972798
#1111111111111
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ... 과 같이, 0 이상의 앞뒤가 같은 수를 크기 순으로 나열할 때, n 번째 수를 계산하는 프로그램을 작성하라.
#n은 1부터 시작하며 크기에는 제한이 없다.

#입출력예
#예 1) 1 => 0
#예 2) 4 => 3
#예 3) 30 => 202
#예 4) 100 => 909
#예 5) 30000 => 200000002
#예 6) 1000000 => 90000000009
#========================================================================
#과제1. 앞뒤가 같은 수(n)를 크기순으로 나열하세요 (0 <= n <= 100).
#     - 출력값 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99

#과제 1 풀이
result = []                                                      # result 명의 빈 리스트 생성
for n in range(1,100):                                           # for문을 이용하여 처음부터 1부터 99까지 n 반복
    a = int(str(n)[:2])                                          # a = n의 처음부터 2번째까지 값을 숫자로 변환한 값
    b = 10**(len(str(n))-1)                                      # b = n을 문자로 변환, 이의 길이 -1에 10을 거듭제곱한 값

    if 0 < n < 11:                                               # if문을 이용해 n 값이 0보다 크고 11보다 작을 때 
        result.append(n-1)                                       # 빈 리스트, result에 n-1값을 추가
    elif a < 11:                                                 # 만약 a가 11보다 작을 때
        result.append(str(n-int(b/10))+str(n-int(b/10))[-2::-1]) # 빈리스트 result에 str(n-int(b/10))+str(n-int(b/10))[-2::-1]값 추가 
    elif a < 20:                                                 # 만약 a가 20보다 작을 때 
        result.append(str(n-b)+str(n-b)[::-1])                   # 빈리스트 result에 result.append(str(n-b)+str(n-b)[::-1])값 추가
    else:                                                        # 다 아니면
        result.append(str(n-b)+str(n-b)[-2::-1])                 # 빈리스트 result에 str(n-b)+str(n-b)[-2::-1] 값을 추가
        
output = []                        # output 명의 빈 리스트 생성/차이 

for x in result:                   # for문을 이용해 result만큼 x 반복/차이 
    if 0 <= int(x) <= 100:         # if문을 이용해 x를 int로 변환한 값이 0보다 크거나 같거나 100보다 작거나 같으면/차이 
        output.append(str(x))      # output 빈 리스트에 x를 문자로 변환한 값 추가/차이 
print(', '.join(output))           #결과 출력/차이

#========================================================================
#과제2. 0 이상의 앞뒤가 같은 수를 크기순으로 나열하고 30,000번째 수를 출력하세요.
#      - 출력값 : 200000002

#과제 2 풀이
n = 30000                                                    # n = 30000 할당/차이점

a = int(str(n)[:2])                                          # a = 문자 n의 처음부터 2번째 자리 값을 숫자로 변환하여 할당
b = 10**(len(str(n))-1)                                      # b = n을 문자로 변환, 이의 길이 -1에 10을 거듭제곱한 값

if 0 < n < 11:                                               # if문을 이용해 n 값이 0보다 크고 11보다 작을 때 
    print(n-1)                                               # 빈 리스트, result에 n-1값을 추가
elif a < 11:                                                 # 만약 a가 11보다 작을 때
    print(str(n-int(b/10))+str(n-int(b/10))[-2::-1])         # 빈리스트 result에 str(n-int(b/10))+str(n-int(b/10))[-2::-1]값 추가 
elif a < 20:                                                 # 만약 a가 20보다 작을 때 
    print(str(n-b)+str(n-b)[::-1])                           # 빈리스트 result에 result.append(str(n-b)+str(n-b)[::-1])값 추가
else:                                                        # 다 아니면
    print(str(n-b)+str(n-b)[-2::-1])                         # 빈리스트 result에 str(n-b)+str(n-b)[-2::-1] 값을 추가
#=======================================================================
