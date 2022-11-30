# 데코레이터
# 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 때 사용
# 로깅, 권한 확인

# 데코레이터 생성하기
def logger(func):
    def wrapper():
        print("함수 시작")
        func()
        print("함수 끝")
    return wrapper

@logger
def print_hello():
    print("hello start coding")

print_hello()