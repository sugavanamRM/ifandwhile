import first
print(dir(first))
print(first.__name__)


f = open("one.txt", "a")
name = ('python','trainee')
f.writelines(name)
f = open("one.txt", "r")
content = f.readlines() 
for line in content:
	print(line)
f.close()



f = open("one.txt", 'a') #a - APPEND, write - over write
name = ['python','linux','java']
f.writelines(name)
f.close()

try:
    print(10/0)
except:
    print("check")
else:
    print('else')
finally:
    print('finally')

	
no1 = int(input('enter no1:'))
no2 = float(input('enter no2:'))
try:
    print(no1/no2)
except (ZeroDivisionError,ValueError) as msg:
    print("Enter only positive integers",msg)
finally:
	print('Hello')

	
from abc import *
class RoadTransport(ABC):
	def fix_indicator(self):
		pass

class Royal_enfield(RoadTransport):
	def fix_indicator(self):
		pass
	
class classic_350(Royal_enfield):
	def fix_indicator(self):
		print('fix indicators')
		
raja = classic_350()
raja.fix_indicator()


def decorator(function): #function = greet(name)
	def greetings(name):
		if name=='sugavanam':
			print('welcome back',name)
		else:
			function(name)
	return greetings

@decorator
def greet(name):
	print('welcome',name)
	
greet('sakthivel')
greet('sugavanam')


def decorator(func):
	def check(no1,no2):
		if no2==0:
			return 'check no2'
		else:
			return func(no1,no2)
	return check
			
@decorator
def divide(no1,no2):
	return no1/no2

print(divide(10,0))
print(divide(10,2))