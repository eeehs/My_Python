#Player 클래스를 구현해보자
#1) 속성: 이름, 미네랄, 가스 ,유닛리스트

class Player:
    unit = {
        "probe":{
            "name" : "프로브",
            "mineral" : 50,
            "gas" : 0 ,
            "hp" : 20,
            "shield" : 20,
            "demage" : 5,
        },
        "zealot":{
            "name" : "질럿",
            "mineral" : 100,
            "gas" : 0 ,
            "hp" : 100,
            "shield" : 60,
            "demage" : 16,
        },
        "dragon":{
            "name" : "드라군",
            "mineral" : 125,
            "gas" : 50 ,
            "hp" : 100,
            "shield" : 80,
            "demage" : 20,
        }
    }
    def __init__(self,name,mineral,gas,unit_list):
        self.name = name
        self.mineral = mineral
        self.gas = gas
        self.unit_list = unit_list

    def plus_unit(self,unit):
        # 미네랄,가스 충분한 경우
        if self.mineral >= Player.unit[unit]["mineral"] and self.gas >= Player.unit[unit]["gas"]:
            print(f"{Player.unit[unit]['name']}을 생성합니다.")
            self.unit_list.append(Player.unit[unit]['name'])
        # 미네랄이 부족한 경우
        elif self.mineral < Player.unit[unit]["mineral"]: 
            print('미네랄이 부족합니다.')
        # 가스가 부족한 경우
        elif self.gas < Player.unit[unit]["gas"]:
            print('가스가 부족합니다.')

Player_1 = Player("이현수", 130, 10, [])


Player_1.plus_unit(input("어떤 유닛을 추가하시겠습니까? probe ,zealot,dragon>>> "))

print(Player_1.unit_list)