Decorator

Extending functionality without touching exsisting
function or logic  

Decorator is a function which can take a function 
as argument and extend its functionality

def greet(name):
	print('welcome',name)
	
greet('sakthivel')       --> op: welcome sakthivel
------------------------------------------------------



@decorator         #Any name
def greet(name):
	print('welcome',name)
	
greet('sakthivel')
greet('sugavanam') #welcome back sugavanam

RESULT:
NameError: name 'decorator' is not defined

-----------------------------------------------------------
*)  Condition shouldn't edit def greet (name):
*)  But I need --> op: welcome sakthivel
*)  --> op: welcome back sugavanam

def decorator(func):
	return 'sugavanam' 

@decorator         #Any name
def greet(name):
	print('welcome',name)
	
greet('sakthivel')
greet('sugavanam') #welcome back sugavanam

RESULT:
	
TypeError: 'str' object is not callable
------------------------------------------------------------
#Oru Function ku mela @(any name) kudutha it is decorator
#Antha decorator killa yenna function name kuduthirkingalo
#Functiona inputa yeduthukum 

# def decorator(greet(name))
#      def greetings(name):

def decorator(func):  # func == greet(name)
	def greetings(name):
		if name=='sugavanam':
			print('welcome back',name)
		else:
			func(name) #--> greet(name) 
	return greetings   # greetings returns to decorator


@decorator         #Any name
def greet(name):
	print('welcome',name)
	
greet('sakthivel')
greet('sugavanam') #welcome back sugavanam

----------------------------------------------------------------
def decorator(func):
	def greetings(name):
		if name=='sugavanam':
			print('Welcome Back',name)
		else:
			func(name)
	return greetings

@decorator         #Any name
def greet(name):
	print('welcome',name)
	
greet('sakthivel')
greet('sugavanam') #welcome back sugavanam

RESULT:

welcome sakthivel
welcome back sugavanam

------------------------------------------------------------------
def divide(no1,no2):
	return no1/no2

print(divide(10,2))  ---> op: 5.0

------------------------------------------------------------------
def smart_divide(divide):
	def check(no1, no2):
		if no2==0:
			print('check no2')
			return
		else:
			return divide(no1, no2)
	return check 

@smart_divide
def divide(no1,no2):
	return no1/no2

print(divide(10,0))      --->op: check no2
	                             None
------------------------------------------------------------------
def smart_divide(divide):
	def check(no1, no2):
		if no2==0:
			return 'check no2'
		else:
			return divide(no1, no2)
	return check 

@smart_divide
def divide(no1,no2):
	return no1/no2

print(divide(10,0))    --> op: check no2
	
#check returns --> smart_divide returns --> decorators function 
------------------------------------------------------------------
def smart_divide(divide):
	def check(no1, no2):
		if no2==0:
			return 'check no2'
		else:
			return divide(no1, no2)
	return check 

@smart_divide
def divide(no1,no2):
	return no1/no2

print(divide(10,10))    --> op: 1.0
	
-------------------------------------------------------------------
#passing function as arguments

def lower(data):
	return data.lower()

def upper(data):
	return data.upper()

def check(function):
	display = function('ABcdEFgh')
	print(display)
	
check(lower)
check(upper)

RESULT:
	
abcdefgh
ABCDEFGH
-------------------------------------------------------------