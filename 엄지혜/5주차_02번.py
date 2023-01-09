#========================================================================
#음수가 아닌 수들이 주어졌을 때 그 수들을 이어서 만들 수 있는 가장 큰 수를 구하시오.
#예를 들어 [1,2,3]이 주어졌을 때 만들 수 있는 가장 큰 수는 321이고, [3, 30, 34, 5, 9]가 주어지면 만들 수 있는 가장 큰 수는 9534330이다.
#========================================================================
#과제1. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
#      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
#      - num_list = [1, 2, 3] 
#      - 출력값 : 321

# 과제 1 풀이
num_list = input('num_list = ').split(', ')  #num_list에 input을 통해 외부값을 받고
                                             #split를 통해 ','를 기준으로 쪼개서 저장

for i in range(len(num_list)):               #for문을 이용해 i를 num_list의 길이만큼 반복
    for j in range(i+1, len(num_list)):      #for문을 이용해 j를 (i+1부터 ~ num_list의 길이까지) 반복
        if int(num_list[i] + num_list[j]) < int(num_list[j] + num_list[i]): #if문을 통해 만약 [(num_list의 i번째 + num_list의 j번째) int로 정수로 변환 값 < (num_list의 j번째 + num_list의 i번째) int로 정수로 변환 한 값] 이라면 
            num_list[i], num_list[j] = num_list[j], num_list[i]             #num_list의 i번째, num_list의 j번째 = num_list의 j번째, num_list의 i번째

#========================================================================
#과제2. 아래에 입력이 num_list로 주어졌을 때, 그 수들을 이어서 만들 수 있는 가장 큰 수인 출력값을 구하시오. 
#      - 조건 1. 입력된 숫자들은 음수가 아닌 자연수
#      - 조건 2. 아래와 같은 입력값을 도출하시오. 
#      - num_list = [3, 30, 34, 5, 9] 
#      - 출력값 : 9,534,330

# 과제 2 풀이
num_list = input('num_list = ').split(', ')  #num_list에 input을 통해 외부값을 받고
                                             #split를 통해 ','를 기준으로 쪼개서 저장

for i in range(len(num_list)):               #for문을 이용해 i를 num_list의 길이만큼 반복
    for j in range(i+1, len(num_list)):      #for문을 이용해 j를 (i+1부터 ~ num_list의 길이까지) 반복
        if int(num_list[i] + num_list[j]) < int(num_list[j] + num_list[i]): #if문을 통해 만약 [(num_list의 i번째 + num_list의 j번째) int로 정수로 변환 값 < (num_list의 j번째 + num_list의 i번째) int로 정수로 변환 한 값] 이라면 
            num_list[i], num_list[j] = num_list[j], num_list[i]             #num_list의 i번째, num_list의 j번째 = num_list의 j번째, num_list의 i번째

#========================================================================
# 과제 1 출력
print(','.join(num_list))

# 과제 2 출력
print(','.join(num_list))
#========================================================================
