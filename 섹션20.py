# #리스트 [] 순서를 가지는 객채 의 집합
 
# # 지하철 칸별로 10명 , 20명 , 30명


subway = [10,20,30] # 변수를 하나로 묶어줌 
print(subway)

subway = ["A","B","C"]

print(subway)

# #조가 몇번쨰 칸에 타고있는가 ? 

print(subway.index("B"))

# #D가 다음 정류장에서 다음 칸에 탐 
subway.append("D")
print(subway)

# # E 를 A와B 사이에 끼워봄 

subway.insert(1 , "E")

print(subway)

# #변수에서 알파벳 하나를 꺼냄 (뒤에서부터 사라짐)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# #같은 알파벳이 몇개일지 확인기 

subway.append("A")
print(subway)
print(subway.count("A "))

# 정렬도 가능 

num_list = [5,2,4,3,1]
num_list.sort() # 정렬 1~5 
print(num_list)

# 순서 뒤집기 가능 
num_list.reverse() # 뒤에서 정렬 5~1 
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list) # [] 이렇게 공백만 나옴 

