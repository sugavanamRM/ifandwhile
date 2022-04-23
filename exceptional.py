#Exception - Unexpected event that disturbs the normal flow of the program
no1 = int(input('enter no1:'))
no2 = int(input('enter no2:'))
print(no3)

RESULT:
NameError: name 'no3' is not defined
------------------------------------------------------------
no1 = int(input('enter no1:'))
no2 = int(input('enter no2:'))
print(no1/no2)
print('Hello')

RESULT:
enter no1:100
enter no2:0

	print(no1/no2)
ZeroDivisionError: division by zero

-------------------------------------------------------------
no1 = int(input('enter no1:'))
no2 = int(input('enter no2:'))
try:
	print(no1/no2)
except ZeroDivisionError:
	print("check no2")
	
print('Hello')

RESULT:
except ZeroDivisionError try everything here
when ZeroDivisionError occurs do the below
	
enter no1:67
enter no2:7
9.571428571428571
Hello

enter no1:100
enter no2:0
check no2
Hello

------------------------------------------------------------
no1 = int(input('enter no1:'))
no2 = int(input('enter no2:'))
try:
	print(no1/no2)
except ZeroDivisionError:
	print("check no2")
	
print('Hello')

RESULT:
	
enter no1:23
enter no2:kjhgf
ValueError: invalid literal for int() with base 10: 'kjhgf'
---------------------------------------------------------------
try:
	no1 = int(input('enter no1:'))
	no2 = int(input('enter no2:'))
	print(no1/no2)
except ValueError:
	print('Please give only numbers')
except ZeroDivisionError:
	print("check no2")
	
print('Hello')

RESULT:
	
enter no1:12
enter no2:sugav
Please give only numbers
Hello

enter no1:12
enter no2:0
check no2
Hello


--------------------------------------------------------------
What is class?  - Blueprint or template
classifications / category
eg:
	value error category print this message
	
--------------------------------------------------------------
try:
	no1 = int(input('enter no1:'))
	no2 = int(input('enter no2:'))
	print(no1/no2)
except:
	print('something went wrong')
	
print('Hello')

RESULT:
enter no1:100
enter no2:qbc
something went wrong
Hello
--------------------------------------------------------------
try:
	no1 = int(input('enter no1:'))
	no2 = int(input('enter no2:'))
	print(no1/no2)
except (ValueError,ZeroDivisionError) as msg:
	print('check all inputs')
	
print('Hello')

RESULT:
enter no1:100
enter no2:sugav
check all inputs
Hello

-----------------------------------------------------------------
try:
	no1 = int(input('enter no1:'))
	no2 = int(input('enter no2:'))
	print(no1/no2)
except (ValueError,ZeroDivisionError) as msg:
	print('check',msg)
finally:
	print('check me')
print('Hello')

RESULT:
enter no1:100
enter no2:10
10.0
check me
Hello

enter no1:90
enter no2: hello
check invalid literal for int() with base 10: 'hello'
check me
Hello
----------------------------------------------------------------
#what is the differece between exceptional and finally
#Exception occurs when it execute ,finally occurs always
try:
	#Exception Possible Area
except (ValueError,ZeroDivisionError) as msg:
	#Exception Handling  Area
finally:
	#Code cleaning area -- mainly used for DB connection disable
	
print('Hello')

----------------------------------------------------------------
#Nested try possible:

try:
	no1 = int(input('enter no1:'))
	no2 = int(input('enter no2:'))
	try:
		print(no1/no2)
	except:
		print("check numbers")

except:
	print('check inputs')
-----------------------------------------------------------------
try:
	print(10/2)
except:
	print("check")
else:
	print('else')
finally:
	print('finally')

RESULT:
5.0
else
finally
-------------------------------------------------------------------
try:
	print(10/0)
except:
	print("check")
else:
	print('else')
finally:
	print('finally')

RESULT:

else
finally
-------------------------------------------------------------------