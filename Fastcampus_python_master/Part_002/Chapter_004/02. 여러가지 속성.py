class Unit:
	"""
    인스턴스 속성: 이름, 체력 방어막, 공격력
    -> 객체마다 다른 값을 가지는 속성
    클래스 속성 : 전체 유닛 개수
    -> 모든 객체가 공유하는 속성
    """
	def __init__(self,name,hp,shield,demage):
		self.name = name
		self.hp = hp
		self.shield = shield
		self.demage = demage

	def __str__(self):
		return (f"[{self.name}]체력:{self.hp} 실드:{self.shield} 공격력:{self.demage}")
	

probe = Unit("프로브",20,20,5) 
zealot = Unit("질럿",100,60,16)
dragoon = Unit("드라군",100,80,20)

# 인스턴스 속성 수정
probe.demage += 6

print(probe)