# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하십시오 

# 예) http://naver.com 
# 규칙1: http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리+ 글자갯수 + 글자내 'e' 갯수 + "!" 로 구성 
#                  (nav)              (5)             (1)        (!)
# 예) 생성된 비밀번호 : nav51! 

# http = ("http://naver.com")
# print(http[7:])
# print(http[7:12])

# http2 = http[7:12]

# # print(http2)
# print(http2.count)
# print(http2.index("e"))

# print(http2[-3:] + http2.count("e")+"!")




http = "http://naver.com"
print(http[7:])  # naver.com

http2 = http[7:]               # naver.com
http2 = http2[:http2.index(".")]  # naver

# 디버깅용 출력
print(http2)                  # naver
print(http2.count("e"))       # 1
print(http2.index("e"))       # 3 (첫 번째 e 위치)

# 비밀번호 생성
print(http2[:3] + str(len(http2)) + str(http2.count("e")) + "!")
