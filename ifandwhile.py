
IF - it works one time
 
num=1
if num==1:
         print("hello")
O/P:hello
########################################################################
num=1
while num==1:
          print("hello")
O/P:
hello
hello
hello
hello
hello
hello
hello................................n times 
#######################################################################
EXAMPLES:
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")
 
O/P:3 is  a positive number.&this is always printed
 
num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
 
O/P:
this is also always printed
####################################################################
n = 10
sum = 0                                                    # initialize sum and counter
i = 1
while i <= n:
        sum = sum + i
        i = i+1                                               # update counter
print("The sum is", sum)                       # print the sum
 
O/P:
The sum is 55