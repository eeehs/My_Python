import pay_module 

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2021=06-13")
print(pay_info.get_pay_info())