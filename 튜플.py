# 변경되지 않는 목록에 튜플 사용가능 

menu=("돈가스","치즈가스")

print(menu[0])
print(menu[1])

#메뉴 추가 (add 기능 사용불가)
# menu.add("생선까스")
# File "c:\Users\세진\Desktop\python\213\튜플.py", line 9, in <module>
#     menu.add("생선까스")
#     ^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'add'
#------------------------------------------------------------------------
# name = "김종국"
# age = 20 
# hobby = "코딩"
# print(name,age,hobby)

(name, age , hobby) = ("김종국", 20 , "코딩")
print(name, age , hobby) 