# 자료구조의 변경 

menu = {"커피","우유","주스"} #{'커피', '주스', '우유'} <class 'set'> 대괄호
print(menu, type(menu))

menu = list(menu)             #['커피', '주스', '우유'] <class 'list'> 중괄호
print(menu, type(menu))

menu = tuple(menu)            #('커피', '주스', '우유') <class 'tuple'> 소괄호
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))       #{'커피', '우유', '주스'} <class 'set'>