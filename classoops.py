Class - object

particular memory area. In that memory area we  write 
some function

Before we reuse modules

In oops  - we reuse classes

procedure oriented approach -- before oops or class
eg:
	file1.py   -   file2.py
	used  import  to access file1.py  in   file2.py
	

similar approach in oops:

class  - is almost similat to module  but not exactly
       - in class we use alot of functions and variables
	
why object oriented programminng?

we do programm by object specify.

but in procedure oriented programminng we do by procedure


what is object specify?
----------------------------------------------------------------

class student():
	"""check"""       # prints documentation output string
print(student.__doc__)       --> op: check

---------------------------------------------------------------

what  is class?
class is  template.
---------------------------------------------------------------

class student:
	                      #init stores the value of student1 in that area 
	def __init__(self):   #initialise means students is self  
		self.name = 'sakthivel'   #(student1 - details)
		self.no = 123     #(student1 and init part connected by *self*)
		self.marks = 100
		
student1 = student()
print(student1.name)     --> op: sakthivel
print(student1.no)       --> op: 123

	
ithu oru structure directa poi init contact pannum

-------------------------------------------------------------------------

class student:
	
	def __init__(self):
		self.name = 'sakthivel'
		self.no = 123
		self.marks = 100
		
student1 = student()
print(student1.name)     --> op: sakthivel
print(student1.no)       --> op: 123
-------------------------------------------------------------------------
class student:
	
	def __init__(self,name,age,occupation):
		self.name = name
		self.no = age
		self.quali = occupation
	
#Memory Representation of  student class 
student1 = student('sakthivel',22,student)
student2 = student('murugan',25,student)
print(student1.name)                    ---> op: sakthivel
print(student2.name)                    ---> op: murugan
print(student1.no)                      ---> op: 22
print(student2.no)                      ---> op: 25

--------------------------------------------------------------------------
class student:
	
	def __init__(self,name,age,occupation):
		self.name = name
		self.no = age
		self.quali = occupation
		
	def display(self):
		print(self.name)   
		print(self.no)
	
#Memory Representation of  student class 
student1 = student('sakthivel',22,student)
student2 = student('murugan',25,student)
student2.display()

RESULT:
	
murugan
25
-------------------- -----------------------------------------------------
#class - object specific value & class specific

#self - object
#cls  - class

class shop:
	name = 'sri  sugavanam super market'

#constuctor - special function(automatically calls the value in function)

	def __init__(self,brand,mrp,discount):
		self.brand = brand
		self.mrp = mrp
		self.discount = discount
		
	def buy(self):
		print(self.mrp)
		
	def after_discount(self):
		print(self.mrp-self.discount)
	
	#Aanatation
	@classmethod #Decorator
	def white_wash(cls):
		print('white wash')
		
soap = shop("lux",15,2)
biscuit = shop("tiger",20,3)
soap.buy()
soap.after_discount()
print(shop.name)
shop.white_wash()

RESULT:
15
13
sri  sugavanam super market
white wash

----------------------------------------------------------------------

class school:
	name = 'srmv school'
	def __init__(self,name,address):
		self.name = name
		self.address = address
		
	def appear_exams(self):
		print(self.name,'is appearing for exam')
		
	@classmethod
	def conduct_exam(cls):
		print(cls.name,'is conducting exam')
		
student1 = school('sugavanam','erode')
student2 = school('sakthivel','madurai')
school.conduct_exam()
student1.appear_exams()


class school:
	name = 'srmv school'
	def __init__(obj,name,address):
		obj.name = name
		obj.address = address
		
	def appear_exams(obj):
		print(obj.name,'is appearing for exam')
		
	@classmethod
	def conduct_exam(abc):
		print(abc.name,'is conducting exam')
		
student1 = school('sugavanam','erode')
student2 = school('sakthivel','madurai')
school.conduct_exam()
student1.appear_exams()

RESULT:

srmv school is conducting exam
sugavanam is appearing for exam

------------------------------------------------------------------
class python:
	titl = 'payilagam software institue'
	
	def __init__(self,name,age,place):
		self.name = name
		self.age = age
		self.place = place
		
	def display(self):
		print(self.name)
		print(self.age)
		print(self.place)
	
	def display(self):
		print(self.name)
		print(self.age)
		print(self.place)
		 
	@classmethod
	def method(cls):
		print(cls.titl)

print(python.titl)
trainee1 = python('sugavanam',24,'Dharmapuri')
trainee2 = python('sakthivel',22,'Trichy')
trainee3 = python('murugapandi',27,'kodaikaanal')
trainee1.display()
trainee2.display()
python.method()
--------------------------------------------------------------------
#passing members of one class to another class
class company:
	
	def __init__(self,name,id):
		self.name = name
		self.id = id
		
	def develop(self):
		print('Developers')
		
	def test(self):
		print('Testers')
		
emp1 = company('sugavanam','19mat042')
emp2 = company('murugapandi','15uma040')


class car_showroom:
	def discount(emp):
		print(emp.name,'is  eligible for discount')
		emp.develop()
		
emp = company('sakthivel','pyb12')
car_showroom.discount(emp)

RESULT:
	
sakthivel is  eligible for discount
Developers

-----------------------------------------------------------------