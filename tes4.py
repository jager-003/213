# 숫자 처리 함수  

print(abs(-5)) # 5  (절대값)
print(pow(4, 2)) # 4^2 = 4x4 = 16 (제곱) 
print(max(5, 12 )) # 12 (최대값)
print(min(5, 12)) # 5 (최소값)
print(round(3.14)) # 3 (반올림)
print(round(4.99)) # 5

# 파이썬에서 재공하는 math 기능을 이용할수 있음 

from math import *
print(floor(4.99)) # 내림 . 4 
print(ceil(3.14)) # 올림 . 4
print(sqrt(16)) # 제곱근 4x4 = 16 이르로 4가 출력됨

# 각 부분 설명:

# 1, from math import *

# math 모듈에 있는 모든 함수와 상수를 현재 코드에서 바로 쓸 수 있게 가져온다는 뜻입니다.

# 예: floor, ceil, sqrt, pi 등을 사용할 수 있게 됨.

# 2, floor(4.99)

# floor는 "내림" 함수입니다.

# floor(4.99)는 4.99보다 작거나 같은 정수 중 가장 큰 수인 4를 반환합니다.

# 3, print(floor(4.99))

# floor(4.99)의 결과인 4를 화면에 출력합니다.


