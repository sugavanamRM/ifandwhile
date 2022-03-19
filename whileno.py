
day=1
n=1
while day<=30:
    n=n*2
    day=day+1
    print(n)
 
 o/p: (up to down)
1
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
32768
65536
131072
262144
524288
1048576
2097152
4194304
8388608
16777216
33554432
67108864
134217728
268435456
536870912
####################################################################################
	
#Write a program to print n natural number in descending order using a while loop.
# N natural number                                              website:pythonlobby.com
n=int(input("enter the value:",))
while  n!=0:
    print(n,end=" ")                                                 INPUT:10
    n=n-1                                                                  RESULT:10 9 8 7 6 5 4 3 2 1
####################################################
REVERSE A NUMBER:
n = int(input("Enter number: "))
rev = 0
while(n != 0):
   rem = n % 10
   rev = rev * 10 + rem
   n = n // 10                                                         INPUT:54321
print(rev)                                                              RESULT:12345
#################################################### FACTORIAL OF NUMBER:
n = int(input("Enter number: ")) # 5
if(n == 0 or n < 0):
    print("Value of n should be greater than 1")
else:
    fact = 1
    while(n):
        fact *= n
        n = n-1                                                            INPUT:5
    print(f"Factorial is {fact} ")                              RESULT: Factorial is 120
####################################################
i = 1
while i < 6:
  print(i)
  i += 1
####################################################
BREAK STATEMENT:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
####################################################
CONTINUE STATEMENT:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
####################################################
ELSE CONDITION:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
###################################################
count = 0
while (count < 9):
         print ('The count is:', count)
         count = count + 1
print ("Good bye!")
RESULT:
The count is: 0
The count is: 1
The count is: 2
The count is: 3
The count is: 4
The count is: 5
The count is: 6
The count is: 7
The count is: 8
Good bye!
####################################################
WHILE ELSE:
count = 0
while count < 5:
        print (count, " is less than 5")
        count = count + 1
else:
       print (count, " is not less than 5")
RESULT:
0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
####################################################
# THIS CONSTRUCTS AN INFINITE  LOOP
var = 1
while var == 1 :                         
       num = input("Enter a number :")
       print ("You entered: ", num)
print ("Good bye!")
RESULT:
Enter a number :20
You entered: 20
Enter a number :29
You entered: 29
Enter a number :3
You entered: 3
Enter a number between :Traceback (most recent call last):
        File "test.py", line 5, in <module>
              num = raw_input("Enter a number :")
KeyboardInterrupt
Above example go
 
sum=0
count=1
while count<10:
          sum=sum+count
          count=count+1
print(count)
print(sum)