# quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글이벤트를 진항하기로 했습니다 
# 댓글 작성자들 중에 추첨을 통해 1명을 치킨 , 3명은 커피 쿠폰을 받게 됩니다.
# 추첨프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정 
# 조건2 : 댓글 내용과  상관없이 무작위로 추첨하되 중복 불가 
# 조건3 : random 모듈의 shuffle 과 sample 을 활용 

# 출력 예제 

# -- 당첨자 발표 -- 
# 치킨당첨자 : 1
# 커피당첨자 : [2,3,4]
# --축하합니다--

# (활용예제)
# from random import *
# lst = (1,2,3,4,5)
# print(lst)                                                     
# shuffle(lst)
# print(lst)
# print(sample(lst,1))



from random import shuffle, sample
                      
# 아이디 생성
users = list(range(1, 21))

shuffle(users)

# 추첨: 치킨 1명, 커피 3명 (중복 불가) # 총 4명 추첨
winners = sample(users, 4)  
chicken = winners[0]
coffee = winners[1:]

# 결과
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {chicken}")
print(f"커피 당첨자 : {coffee}")
print("-- 축하합니다 --")