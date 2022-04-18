# Recursive Function
# function calling itself

5! = 5*4*3*2*1
4! = 4*3*2*1
3! = 3*2*1
2! = 2*1
1! = 1

5! = 5*4!
4! = 4*3!
3! = 3*2!
2! = 2*1!
1! = 1

#(5! -> Factorial(5), -- changing mathematical symbol to programming symbol)

factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1

factorial(5) = 5*factorial(4) | factorial(4) is dependent on factorial(3)
factorial(4) = 4*factorial(3) | factorial(3) is dependent on factorial(2)
factorial(3) = 3*factorial(2) | factorial(2) is dependent on factorial(1)
factorial(2) = 2*factorial(1) | factorial(2) is dependent on 1
factorial(1) = 1




def fact1(no):
	return 1

def fact2(no):
	return no * fact1(no-1)

def fact3(no):
	return no * fact2(no-1)

def fact4(no):
	return no * fact3(no-1)

def fact5(no):
	return no * fact4(no-1)

fact5(5)

#Stack Memory 
#(First in Last Out )
#(Last in First out )
fact(1) = 1
fact(2) = 2*fact(1)
fact(3) = 3*fact(2)
fact(4) = 4*fact(3)
fact(5) = 5*fact(4)

-------------------------------------------------------------------

def fact(no):
	if no==1:
		return 1
	else:
		return no*fact(no-1)
	
print(fact(5))    --> op: 120
	
-------------------------------------------------------------------

#Lambda Functions: Anonymous Functions

#concise Programming: --
#   --one time usage and i want function only so we use lambda

def display(no):
	return no**2

print(display(5))     --> op: 25

#lambda arguments:expression

result = lambda no:no**2
print(result(5))      --> op: 25
	
---------------------------------------------------------------------

def power_no(no):
	return no**2

print(power_no(3))     --> op: 9

#1. Remove function name
(no):
	return no**2
#2. Remove brackets
no:
	return no**2
#3.remove return and empty space

no:no**2
	
#4.Add lambda infront of it
lambda no:no**2


result = lambda no:no**2
print(result(3))     --> op: 9
	
-----------------------------------------------------------------------
def great(no1,no2):
	if no1>no2:
		return no1
	else:
		return no2
print(great(100,200))      --> op: 200
	
result = lambda no1,no2:no1 if no1>no2 else no2
print(result(10,20))       --> op: 20

-----------------------------------------------------------------------
