
url = "http://naver.com"

my_str = url.replace("http://" , "") # http 부분을 "" 빈칸으로 만들겠다 

my_str = my_str[:my_str.index(".")]    # my_str 에서 나오는 문자 . 직전까지 출력 [0:5]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"

print(password)