# \n : 줄바꿈 
print("백문이 불여일견\n백견이 불여일타")
#출력 결과
'''
백문이 불여일견
백견이 불여일타
'''

#저는 "나도코딩입니다."
print('저는"나도코딩입니다."') # " ' 두개 사용 해서 출력 가능   
print("저는\"나도코딩\"입니다.") # \" , \' 역슬러쉬 따음표 이용으로 출력가능 

# \\ : 문장 내에서는 \ 로 바뀜 

# print("C:\Users\세진\Desktop\python\213>")

# 출력시 오류 발생 
# PS C:\Users\세진\Desktop\python\213> & C:/Users/세진/AppData/Local/Programs/Python/Python313/python.exe c:/Users/세진/Desktop/python/213/탈출문자.py
#   File "c:\Users\세진\Desktop\python\213\탈출문자.py", line 15
#     print("C:\Users\세진\Desktop\python\213>")
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print("C:\\Users\\세진\\Desktop\\python\\213>") # 역슬러쉬 2개로 만들어서  하나로 출력되게하여 오류 해결

# 또 다른 탈출문자 \r :커서는 맨앞으로 이동해줌 (/r뒤에 문자를 맨앞으로 출력해줌 )
print("REd Apple\rPine")


# 또 다른 탈출문자 \b : 백스페이스 역할을함 \b앞에 한글자를 지워줌 

print("Redd\bApple")

# \t : 탭 역할을 해줌 
print("Red\tApple")

# 출력결과 Red     Apple 