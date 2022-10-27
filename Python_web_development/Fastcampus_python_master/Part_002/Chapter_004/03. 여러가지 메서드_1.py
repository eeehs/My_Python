class Unit:
	count = 0
	def __init__(self,name,hp,shield,demage):
		self.name = name
		self.hp = hp
		self.shield = shield
		self.demage = demage
		Unit.count += 1

	def __str__(self):
		return (f"[{self.name}]체력:{self.hp} 실드:{self.shield} 공격력:{self.demage}")
	
	# 인스턴스 메서드 (instance method)
	def hit(self, damage):
		# 방어막 변경 
		if self.shield >= damage:
			self.shield -= damage
			demage = 0
		else:
			demage -= self.shield
			self.shield = 0

		# 체력 변경
		if damage > 0:
			if self.hp > demage:
				self.hp -= demage
			else:
				self.hp = 0
	# 클래스 메서드 
	# 클래스 속성에 접근하는 메서드
	@classmethod
	def print_count(cls):
		print(f"생성된 유닛 개수: [{cls.count}]")
		

		
probe = Unit("프로브",20,20,5) 
zealot = Unit("질럿",100,60,16)
dragoon = Unit("드라군",100,80,20)

Unit.print_count()