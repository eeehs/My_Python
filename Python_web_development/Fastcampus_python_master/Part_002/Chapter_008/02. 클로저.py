# 1. 내부 함수 
# 함수 안에 또다른 함수를 정의할 수 있다. 

def outer(name):
    def inner():
        print(name,"님 안녕하세요!")
    return inner

func = outer("startcoding")
#func()

# 2. 클로저
# 함수가 종료되어도 자원을 할 수 있는 함수 

def greeting(name,age,gender):
    def inner():
        print(name, "님 안녕하세요!")
    return inner

closure = greeting('나미', 27, 'femaile')
closure()


# 전역 변수를 사용해서 대체 가능하다.
# 전역 변수 사용을 최소화 하는 것이 좋다.(네이밍문제, 스코프문제)