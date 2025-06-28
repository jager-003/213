python = "Python is Amazing"

print(python.lower()) # 문자를 모두 소문자로 표시 
print(python.upper()) # 문자를 모두 대문자로 표시 
print(python[0].isupper()) #문자의 0번째 위치의글자가 대문자인지 참,거짓 
print(len(python)) # 변수의 전체문자열의 길이를 반환해줌 (17줄,띄어쓰기도 포함)

print(python.replace("Python", "java"))
# print(python.replace("python", "java")) 틀림
# 대소문자 구분 중요
#깃허브 커밋 및 푸시

index = python.index("n")  # 변수에서 어떤 문자가 어느 자리에있는지 확인할수 있음 
print(index) # 5번쨰 
index = python.index("n",index + 1) 
# 원하는 문자를 찿은 위치 그다음 문자열에 같은 문자가 어디에 있는지 확인
# 2번쨰 n 을 찿기   
print(index)

print(python.find("java"))

# print(python.find("?")) ? 안에 글자가 몇번쨰에 있는지 찿을수있음 
# 찿는 글자가 변수에 포함되있지 않은경우 -1 이라고 표시 해줌 

#//////print(python.index("java"))
# 그런데 "인덱스"로 찿게되면 오류가 출력됨 


# Traceback (most recent call last):
#   File "c:\Users\세진\Desktop\python\213\문자열처리함수.py", line 25, in <module>
#     print(python.index("java"))
#           ~~~~~~~~~~~~^^^^^^^^
# ValueError: substring not found


# find 에서는 원하는 값이 없을떄 -1 이라고 표시해주고 
#인덱스 에서는 원하는 값이 없을떄는 오류가 나고 프로그램이 종료됨 
print("hi")
#여기있는 문자는 출력이 안됨 find 에서는 -1 만 출력되고 계속 프로그램이 진행됨 


print(python.count("n")) # python 이라는 변수에서 n이 총 몇번 나오는지 알려줌 
