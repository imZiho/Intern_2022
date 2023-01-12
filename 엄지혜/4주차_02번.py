#=============================================================================
#일단 어떤 수를 받아서 그 수를 뒤집은 다음 뒤집어진 수를 원래의 수에 더하는 과정을 뒤집어서 더하기라고 부르자.
#그 합이 회문(palindrome, 앞뒤 어느 쪽에서 읽어도 같은 말이 되는 어구. 예:eye, madam, 소주만병만주소)이 아니면 회문이 될 때까지 이 과정을 반복한다.
#예를 들어 처음에 195에서 시작해서 다음과 같이 네 번 뒤집어서 더하기를 반복하면 9339라는 회문이 만들어진다.

# 195      786       1473      5214
#+591     +687      +3741     +4125
#----     -----     -----     -----
# 786     1473       5214      9339

#대부분의 정수는 이 방법을 몇 단계만 반복하면 회문이 된다. 하지만 예외도 있다. 회문을 찾을 수 없는 것으로 밝혀진 첫번째 수는 196이다. 하지만 회문이 없다는 것이 증명된 적은 없다.
#어떤 수가 주어졌을 때 회문이 있으면 출력하고, 그 회문을 찾기까지 뒤집어서 더하기를 반복한 횟수를 출력하는 프로그램을 만들어야 한다.
#테스트 데이터로 사용되는 수는 모두 뒤집어서 더하기를 1,000번 미만 반복해서 회문을 찾을 수 있는 수고, 그렇게 만들어진 회문을 4,294,967,295보다 크지 않다고 가정해도 된다.

#Input
#첫번째 줄에는 테스트 케이스를 나타내는 정수 N(0<N<=100)이 들어있고, 그 아래로 N개의 줄에 걸쳐서 회문을 구해야 하는 정수가 한 줄에 하나씩 들어있다.

#output
#N개의 각 정수에 대해 회문을 발견하는 데 필요한 최소한의 반복 횟수를 출력하고, 스페이스를 한 칸 출력한 다음, 그 회문을 출력한다.

#Sample Input
#3
#195
#265
#750

#Sample Output
#4 9339
#5 45254
#3 6666
#=============================================================================
#과제 1. input 값의 회문을 발견하는데 필요한 최소한의 반복 횟수를 출력하고, 스페이스를 한 칸 출력한 다음
#       그 회문을 출력하시오.
#        - input = 195
#        - output = 4 9339

#과제 1 풀이   
def PR(n):                           #def를 이용해 PR 명의 함수 생성
    RE1 = 1                          #RE1에 숫자 1 저장
    while RE1<1000 :                 #while문으로 무한반복 루프 생성/RE1가 1000보다 작다면
        down_n  = int(str(n)[::-1])  #down_n은 n을 str(문자)로 변환 다시 int로 숫자로 변환하고 처음부터 끝까지 -1칸 단격으로 띄움
        n = str(n +down_n)           #n에 n과 down_n를 더한 값을 str를 통해 문자로 변환 후 할당
        RE2 = 0                      #RE2에 0 저장
        for y in range(len(n)//2):   #for문을 이용해 y를 n의 길이를 2로 나눈 몫만큼 반복
            if n[y] ==n[-(y+1)]:     #if문을 이용하여 n[y]값이 n[-(y+1)]값과 같다면
                RE2 +=1              #RE2에 1씩 더하여 할당
        if RE2 == len(n)//2:         #if문을 이용하여 RE2값이 n을 2로 나눈 몫과 같다면     
            break                    #break를 통해 무한반복 루프 탈출 
        RE1 +=1                      #RE에 1씩 더하여 할당
        n = int(n)                   #n에 n을 정수로 변환해 저장
    print(str(RE1)+" "+str(n))        #str로 문자로 변환한 RE와 str로 숫자로 변환한 n을 붙혀서 프린트 / RE와 n 사이를 " " 한칸 띄음
PR(195)                              #PR에 195 대입

#=============================================================================
#과제 2. input 값 만큼 정수를 입력받아 각 정수별로 가장 작은 회문을 출력하시오
#        - 조건1 : 정수를 모두 입력받은 후 결과값을 한꺼번에 출력하시오.
#        - 조건2 : 정수를 입력받을 때 input() 함수를 사용하시오.
#        - input = 3
#        - 입력받을 정수 = 195, 265, 750
#        - output :
#                    9339
#                    45254
#                    6666

#과제 2 풀이
def PR2(n):                          #def를 이용해 PR2 명의 함수 생성
    RE1 = 1                          #RE1에 숫자 1 저장
    while RE1<1000 :                 #while문으로 무한반복 루프 생성/RE1가 1000보다 작다면
        down_n  = int(str(n)[::-1])  #down_n은 n을 str(문자)로 변환 다시 int로 숫자로 변환하고 처음부터 끝까지 -1칸 단격으로 띄움
        n = str(n +down_n)           #n에 n과 down_n를 더한 값을 str를 통해 문자로 변환 후 할당
        RE2 = 0                      #RE2에 0 저장
        for y in range(len(n)//2):   #for문을 이용해 y를 n의 길이를 2로 나눈 몫만큼 반복
            if n[y] ==n[-(y+1)]:     #if문을 이용하여 n[y]값이 n[-(y+1)]값과 같다면
                RE2 +=1              #RE2에 1씩 더하여 할당
        if RE2 == len(n)//2:         #if문을 이용하여 RE2값이 n을 2로 나눈 몫과 같다면 
            break                    #break를 통해 무한반복 루프 탈출
        RE1 += 1                       #RE에 1씩 더하여 할당
        n = int(n)                   #n에 n을 정수로 변환해 저장
    print(str(n))                    #str로 n를 문자로 변환후 출력
def PRL(n):                          #def로 PRL 명의 함수 생성
    number_list = []                         #PRL의 빈리스트 생성
    for Z in range(n):               #for문을 이용해 z를 n만큼 반복
        number = int(input('INPUT = '))  #input_number에 input으로 외부값을 받고 이를 int로 바꾸어 저장
        number_list.append(number)   #input_number_list에 input_list를 appand를 이용하여 추가
    for i in number_list:           #for문을 이용하여 z를 input_number_list만큼 반복
        PR2(i)                       #PR2 에 z 대입 
PRL(3)                 #input_number_list에 3 대입
#=============================================================================
            break                    #break를 통해 무한반복 루프 탈출
        RE +=1                       #RE에 1씩 더하여 할당
        n = int(n)                   #n에 n을 정수로 변환해 저장
    print(str(n))                    #str로 n를 문자로 변환후 출력
def PRL(n):                          #def로 PRL 명의 함수 생성
    PRL = []                         #PRL의 빈리스트 생성
    for Z in range(n):               #for문을 이용해 z를 n만큼 반복
        input_number = int(input())  #input_number에 input으로 외부값을 받고 이를 int로 바꾸어 저장
        input_number_list.append(input_number)   #input_number_list에 input_list를 appand를 이용하여 추가
    for i in input_number_list:      #for문을 이용하여 z를 input_number_list만큼 반복
        PR2(i)                       #PR2 에 z 대입 
input_number_list(3)                 #input_number_list에 3 대입
#=============================================================================
