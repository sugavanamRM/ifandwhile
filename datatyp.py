MODULUS OPERATOR:                                      SITE:realpython.com
The modulo operator, like the other arithmetic operators, can be used 
with the numeric types int and float.
  
WITH INT:
Most of the time you’ll use the modulo operator with integers. The modulo operator, when used with two positive integers, will return the remainder of standard Euclidean division:
>>> 15 % 4
3
 
>>> 17 % 12
5
 
>>> 240 % 13
6
 
>>> 10 % 16
10
 
Be careful! Just like with the division operator (/), Python will return a ZeroDivisionError if you try to use the modulo operator with a divisor of 0:
>>> 22 % 0
ZeroDivisionError: integer division or modulo by zero
####################################################
int():
>>> x=1234567890
>>> type(x)
<class 'int'> # type of x is int
 
Leading zeros in non-zero integers are not allowed e.g. 000123 is invalid number, 0000 is 0.
 
>>> x=01234567890
SyntaxError: invalid token
 
Python does not allow comma as number delimiter. Use underscore _ as a delimiter instead.
 
>>> x=1_234_567_890
>>> x
1234567890
####################################################
float():
Floats has the maximum size depends on your system. The float beyond its maximum size referred as "inf", "Inf", "INFINITY", or "infinity". Float 2e400 will be considered as infinity for most systems.
 
>>> f=2e400
>>> f
inf
 
Scientific notation is used as a short representation to express floats having many digits. For example: 345.56789 is represented as 3.4556789e2 or 3.4556789E2
 
>>> f=1e3
>>> f
1000.0
 
Use the float() function to convert string, int to float.
 
>>> float('5.5')
5.5
>>> float('5')
5.0
>>> float('     -5')
-5.0
>>> float('1e3')
1000.0
>>> float('-Infinity')
-inf
>>> float('inf')
inf
####################################################
	
Arithmetic Operators:
  
+ (Addition) 
 
>>> a=10; b=20
>>> a+b
30
 
- (Subtraction)
 
>>> a=10; b=20
>>> b-a
10
>>> a-b
-10
 
* (Multiplication)
 
>>> a=10; b=20
>>> a*b
200
 
/ (Division)
 
>>> a=10; b=20
>>> b/a
2
 
% (Modulus)
 
>>> a=10; b=22
>>> b%a
2
 
** (Exponent)
 
>>> a=3
>>> a**2
9
>>> a**3
27
 
// (Floor Division)
 
>>> a=9; b=2
>>> a//b
4