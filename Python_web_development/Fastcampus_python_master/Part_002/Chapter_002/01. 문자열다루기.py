# 1. replace
# 문자열 교체 

A = "오늘 날씨는 흐림입니다.".replace("흐림","맑음")
print(A)

# 2. find
# 문자열 찾기

B = "Hello World!".find("World")
print(B)

# 3. split
# 문자열 분리
C = '나이키신발 265 x2421 78000'.split()
print(C)

D = '나이키신발 : 265 : x2421 : 78000'.split(':')
print(D)

# 4. strip
# 문자열 공백 제거

E = '           Yeah           '.rstrip()
print(E)