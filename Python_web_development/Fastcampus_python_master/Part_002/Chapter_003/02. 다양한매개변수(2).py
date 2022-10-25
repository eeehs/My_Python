# 1. 위치 가변 매개변수

# 함수 정의
def print_fruits(*args):
	for arg in args:
		print(arg)

# 함수 호출
print_fruits('apple','orange','mango')

# 2. 키워드 가변 매개변수

# 함수 정의
def comment_info(**kwargs):
	for key,value in kwargs.items():
		print(f'{key}:{value}')
# 함수 호출
comment_info(name='파린이',content='정말 감사합니다!')

