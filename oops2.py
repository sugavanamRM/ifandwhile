from abc import * 
class parents(ABC):
	@abstractmethod	def study(self):
		pass
	
class child1(parents):
	def play(self):
		print('playing all time')
		
		
class child2(parents):
	def study(self):
		print('studying B.com')
		
raja = child1()
raja.play()
rani = child2()
rani.study()
