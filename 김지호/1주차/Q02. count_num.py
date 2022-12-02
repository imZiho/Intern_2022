"""
-----------------  Question  -----------------
1~1000에서 각 숫자의 개수 구하기

예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
- 10 = 1, 0
- 11 = 1, 1
- 12 = 1, 2
- 13 = 1, 3
- 14 = 1, 4
- 15 = 1, 5
그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
----------------------------------------------
"""



# 과제 1. 10~15까지의 각 숫자 개수를 출력하세요(1). 
## 출력 : 0 = 1개, 1 = 7개, 2 = 1개, 3 = 1개, 4 = 1개, 5 = 1개

a = ""      # 빈 문자열 생성

for i in range(10,16):     # 10부터 15까지의 수를 생성
    a += (str(i))          # 문자열로 바꾸어 변수 a에 차례대로 저장


for j in range(6):         # 1부터 5까지 생성하며 반복
    j = str(j)             # count함수를 사용하기 위해 문자열로 변환
    print(f"{j}={a.count(j)}개",end=", ")      #c 그리고 c에 해당하는 문자 개수를 a에서 찾아 ,으로 구분하여 한 줄에 출력


#--------------------------------------------------------------------------------------------------------------


# 과제 2. 10~15까지의 각 숫자 개수를 출력하세요(2).
## 출력 : 0 = 1개, 1 = 7개, 2 = 1개, 3 = 1개, 4 = 1개, 5 = 1개, 6 = 0개, 7 = 0개, 8 = 0개, 9 = 0개

a = ""

for i in range(10,16): 
    a += (str(i))      


for j in range(10):     # 1부터 10까지 생성하며 반복
    j = str(j)         
    print("{}={}개".format(j,a.count(j)),end=", ") 


#--------------------------------------------------------------------------------------------------------------


# 과제 3. 1~1000까지의 각 숫자 개수를 출력하세요
## 출력 : 0 = 192개, 1 = 301개, 2 = 300개, 3 = 300개, 4 = 300개, 5 = 300개, 6 = 300개, 7 = 300개, 8 = 300개, 9 = 300개 

a = ""

for i in range(1,1001):     #10부터 1000까지의 수를 생성
    a += (str(i))


for j in range(10):         #1부터 10까지 생성하며 반복
    j = str(j)
    print("{}={}개".format(j,a.count(j)),end=", ")