d = {}

for no in range(1,6):
	d[no] = 2*no
else:
	print(d)

d2 = {no:2*no for no in range(1,6)}
print(d2)

RESULT:

{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

----------------------------------------------------------
def add(no1,no2):
	return no1+no2

result = add(10,20)
print(result)         ---> op: 30
	
----------------------------------------------------------

def withdraw(amount):
	return amount

print(withdraw(100))    ---> op: 100
	
------------------------------------------------------------
def withdraw(amount):
	amount = amount + (amount/10)
	return amount

def spend(cash):
	print('I am going to spend',cash)

#cash = withdraw(100)
#spend(cash)
spend(withdraw(100))

               ---> op: I am going to spend 110.0
		
--------------------------------------------------------------

def calculate(no1, no2):
	sum = no1 + no2
	sub = no1 - no2
	mul = no1 * no2
	div = no1 / no2
	return sum, sub, mul, div

no1 = int(input('Enter no :'))
no2 = int(input('Enter no :'))
print(calculate(no1,no2))

RESULT:
Enter no :56
Enter no :4
(60, 52, 224, 14.0)

-------------------------------------------------------------------

#2. Keyword Arguments

def add(amount, interest):
	print('your amount is',amount)
	print('your interest is',interest)

add(amount=1000,interest=100)
add(interest=1000,amount=100)

RESULT:
your amount is 1000
your interest is 100
your amount is 100
your interest is 1000

---------------------------------------------------------------------

#3. Default Arguments:
def add(amount, interest=4):
	print(amount)
	print(interest)
	
add(1000, interest=10)
add(1000)

RESULT:
1000
10
1000
4

--------------------------------------------------------------------

#4.Variable Length Arguments:

def addition(*num):
	total = 0
	for no in num:
		total = total + no
	return total

num1 = int(input('Enter no:'))
num2 = int(input('Enter no:'))
num3 = int(input('Enter no:'))
result = addition(num1,num2,num3)
print(result)

RESULT:
Enter no:4
Enter no:6
Enter no:10
20

---------------------------------------------------------------------

#Types of Variables

#1. Global
#2. local
no1 = 10       #Global variable   
def display():
	no2 = 20   #local variable
	print(no1)
	print(no2)
	
display()
print(no1)
print(no2)

RESULT:
10
20
10
NameError: name 'no2' is not defined
	
---------------------------------------------------------------------
