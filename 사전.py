cabinet = {3:"유재석" , 100:"김태호"} #사전은 중괄호 사용 누가 어떤키를 가지고 있는지 표시

print(cabinet[3])   # 3번 열쇠는 누가 가지고 있는지 출력 
print(cabinet[100]) # "

print(cabinet.get(3)) # get 을 사용해서값을 가지고 올수있음 

# 캐비넷에 없는 값을 가지고 오면 프로그램이 종료됨,[대괄호 사용시] 
# 하지만 get 을 이용하면 None 이라는 글자가 출력되고 프로그램은 계속 실행됨 

print(cabinet.get(5,"사용가능")) # 사용가능한 열쇠인지 표시 가능 

print(3 in cabinet) # 사용하는 캐비넷에 3 이 있는가 있으면  ture , 없으면 false

cabinet2 = {"A-1":"유재석","B-2":"김태호"}  # 정수가 아닌 스트링(string은 문자열, 연속된 문자들의 나열) 도 사용가능 

#새로운 손님 

print(cabinet)
cabinet["A-3"] = "김종국" # 유재석이였는데 변경 
cabinet["C-20"] = "조세호" # 새손님 추가 
print(cabinet)

#간 손님 
del cabinet["A-3"] # 딜리트로 값을 지울수 있음 
print(cabinet)

# key 들만 출력 

print(cabinet.keys())

#value 들만 출력

print(cabinet.values())

#함께 출력 
print(cabinet.items())

# 폐점 
cabinet.clear() #전부다 삭제 
cabinet2.clear()

print(cabinet)  # 빈 값 출력 
print(cabinet2)