# 랜덤 함수 

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성

print(random() * 10) # 0.0 ~ 10.0 미만의 임의 값을 생성

print(int(random () * 10)) # 0 ~ 10 미만의 임의값 생성 
print(int(random () * 10))
print(int(random () * 10))  

# 0 에서 10 을 뽑는데 0을 보기 싫을떄 

print(int(random()* 10 )+ 1) # 1부터 10 이하의 임의의 값을 생성 하게됨 


# 로또값을 출력하는법

print(int(random()* 45) + 1) # 1~ 45 이하의 임의의 값을 생성 
print(int(random()* 45) + 1)
print(int(random()* 45) + 1)
print(int(random()* 45) + 1)
print(int(random()* 45) + 1)
print(int(random()* 45) + 1)
print(int(random()* 45) + 1) 

print(randrange(1, 46)) # 1 ~ 46 "미만"의 값을 생성  (1은 포함됨 (a ≤ x < b) )     

print(randint(1 , 45)) # 1 ~ 45 "이하"의 값을  생성 
