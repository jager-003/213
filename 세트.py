# 집합 (set)    
# 중복이 안됨 , 순서가 없음 

my_set = {1,2,3,3,3}

print(my_set) # {1, 2, 3}

java = { "유재석","김태호","양세형"}
python = set(["유재석", "박명수"])

#교집합 (java , python 을 모두 개발하는 개발자)

print(java & python )
print(java.intersection(python)) 

# 합집함 (java를 할수 있거나 python을 할 수 있는 개발자)

print(java | python)
print(java.union(python)) # {'양세형', '박명수', '유재석', '김태호'} 순서 상관없이 출력됨 

# 차집합 (java는 할줄 알지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))


# python을 할 줄 하는 사람이 늘어남 
python.add("김태호")

print(python)

#java를 잊었어요 

java.remove("김태호")
print(java)