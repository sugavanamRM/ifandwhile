#Reverse the Numbers:

rev = 0
no = int(input("enter the value  "))
while no>0:
	rev = rev + (no%10)
	no = no//10
else:
	print(rev)                     #Result:7

"""
rev = 0 + {[34%10] = 4} -->4
no = 34//10 = 3

nextloop

rev = 4 + {[3%10] = 3} -->7
no = 3//10 = 0

"""
rev = 0
no = int(input("enter the value  "))
while no>0:
	rev = (rev *10) + (no%10)
	no = no//10
else:
	print(rev)                    #Result:43

EXPLANTION:
rev = (rev*10) + (no%10)
rev = (0*10) + (34%10) = 0 + 4 = 4
no = 34//10 = 3

nextloop

rev = (rev*10) + (no%10)
rev = (4*10) + (3%10) = 40 + 3
no = 3//10 = 0
######################################################################
#Armstrong number
armstrong = 0
no = int(input("Enter no:"))
while no>0:
	rem = no%10
	armstrong = armstrong + (rem*rem*rem)
	no = no//10
else:
	if no==armstrong:
		print("Armstrong Number")
	else:
		print("Not a Armstrong Number")
Result:
Enter no:153
Not a Armstrong Number

EXPLANATION
armstrong = armstrong + (rem*rem*rem)
no = 153
rem = no%10 = 153%10 = 3 
armstrong = 0 + (3*3*3) = 27
no = no//10 = 153//10 = 15

next loop

no = 15
armstrong = 27
rem = no%10 = 15%10 = 5 
armstrong = 27 + (5*5*5) = 152
no = no//10 = 15//10 = 1

next loop

no = 1
armstrong = 152
rem = no%10 = 1%10 = 1 
armstrong = 152 + (1*1*1) = 152 + 1
no = no//10 = 1//10 = 0

loop ends

final no = 0
so no != armstrong number
it printed Not a Armstrong Number
############################################################################
#Armstrong number
armstrong = 0
no = int(input("Enter no:"))
no2 = no
while no>0:
	rem = no%10
	armstrong = armstrong + (rem*rem*rem)
	no = no//10
else:
	if no2==armstrong:
		print("Armstrong Number")
	else:
		print("Not a Armstrong Number")
Result:
Enter no:153
Armstrong Number

final
no = 153
armstrong = 153
so no = armstrong number
printed It is  Armstrong Number
##########################################################################
#Fibonacci Series
f = 0
s = 1
count = int(input("Enter Value:"))
while count>0:
	t=f+s
	print(t,end=" ")
	f = s
	s = t
	count-=1
	
Result:
Enter Value:6 
1 2 3 5 8 13
(But fibonacci series starts with '0' )
########################################################################
#Fibonacci Series
f = -1
s = 1
count = int(input("Enter Value:"))
while count>0:
	t=f+s
	print(t,end=" ")
	f = s
	s = t
	count-=1
"""	
Result:
Enter Value:6 
0 1 2 3 5 8
"""
########################################################################
FOR LOOP - for loop

name = "sakthivel"
for letter in name:
	print(letter,end = " ")
print()	
	
for letter in range(5):
	print(letter,end = " ")
print()

for letter in range(2,20, 2):
	print(letter,end = " ")
print()

for letter in range(20,2, -2):
	print(letter,end = " ")

Result:
s a k t h i v e l 
0 1 2 3 4 
2 4 6 8 10 12 14 16 18 
20 18 16 14 12 10 8 6 4
#########################################################################
for no in range(11):
	print(no)

for no in range(1,11):
	print(no,end=" ")
	
Results:	
1 2 3 4 5 6 7 8 9 10
###########################################################################
total = 0
for no in range(1,11):
	total = total  + no
else:
	print(total)	     #Results:55
	

total = 1
for no in range(1,6):
	total = total  * no
else:
	print(total)         #Results:120
	
EXPLANATION:
no = (1 to 5)
no = 1
total = 0 * 1 = 1
no = 2
total = 1 * 2 = 2
.......
no = 10
total = 24 * 5 = 120
