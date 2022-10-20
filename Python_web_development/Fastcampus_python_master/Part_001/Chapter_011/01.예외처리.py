# 원화를 입력, 환율 입력 -> 달러 값 

won = input("원화 금액을 입력 하세요>>> ")
dollar = input("환율을 입력 하세요>>> ")


try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e: # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e: 
    print("나누기 0은 불가합니다.", e)
else: 
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: #파일을 열고 나서 닫기를 꼭 해야하는 코드가 필요할 때 finally 부분에 작성 
    print("예외가 발생하던지 않던지 항상 실행되는 코드")