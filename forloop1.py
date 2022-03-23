total = 1
for no in range(1,6):
	total = total * no
else:
	print(total)
"""
explanation:

total = 1 * 1 = 1
total = 1 * 2 = 2
total = 2 * 3 = 6
total = 6 * 4 = 24
total = 24 * 5 = 120
"""
RESULT:
120

############################
for end in range(5,2,-1):#6 5 
	total = 1
	for no in range(1,end+1):#(1,6) -->1 2 3 4 5 
		total = total * no
	else:
		print(total)
explanation:

For range(1,6)

total = 1 * 1 = 1
total = 1 * 2 = 2
total = 2 * 3 = 6
total = 6 * 4 = 24
total = 24 * 5 = 120

For range(1,4)

total = 1 * 1 = 1
total = 1 * 2 = 2
total = 2 * 3 = 6
total = 6 * 4 = 24

For range(1,3)

total = 1 * 1 = 1
total = 1 * 2 = 2
total = 2 * 3 = 6

RESULT:
120
24
6

IN WHILE LOOP:
end=5
while end>2:
	total = 1
	for no in range(1,end+1):
		total = total * no
	else:
		print(total)
	end-=1
###########################################################################################
def factorial(end):
	total = 1
	for no in range(1,end+1):
		total = total * no
	else:
		print(total)

factorial(5)
factorial(4)
factorial(3)

RESULT:
120
24
6
##########################################
sentence = 'sugavanam how era tou'
noOfwords = 1
for alpha in sentence:
	if alpha==' ':
		noOfwords+=1
else:
	print(noOfwords)
	
RESULT:
4
###################################################################################
sentence = input("enter the paragraph:")
alpha = digit = specialchar = 0
for letter in sentence:
	if letter.isalpha():
		alpha+=1
	elif letter.isdigit():
		digit+=1
	else:
		if letter != ' ':
			specialchar+=1
else:
	print("No of alpha is:",alpha)
	print("No of digit is",digit)
	print("No of special",specialchar)
##################################################################################
#step:1
for no in range(5,0,-1):
	for value in range(1,no+1):
		print(value,end=' ')
	print()

#step:2
	
for no in range(0,6):
	for value in range(1,no+1):
		print(value,end=' ')
	print()
	
RESULT:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
#####################################################################################
end = 6
value = 1
while end>3:
	for no in range(1,end):
		print(value,end=' ')
	print()
	end-=1
	value+=1  
	
value = 1
for end in range(6,2,-1):
	for no in range(1,end):
		print(value,end=' ')
	print()
	value+=1  
	
	
RESULT:
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4
#######################################################################################
HOME WORK:
#step:1
for no in range(5,0,-1):
	print(no,end=' ')
print()

for no in range(5,1,-1):
	print(no,end=' ')
print()

for no in range(5,2,-1):
	print(no,end=' ')
print()

for no in range(5,3,-1):
	print(no,end=' ')
print()

for no in range(5,4,-1):
	print(no,end=' ')
print()

#step:2

end=0
while end<5:
	for no in range(5,end,-1):
		print(no,end=' ')
	print()
	end+=1
	
#step:3
	
for end in range(0,5):
	for no in range(5,end,-1):
		print(no,end=' ')
	print()
	
RESULT:
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
##########################################################################
#step:1
for no in range(1,10,2):
	print(no,end=" ")
print()

for no in range(1,8,2):
	print(no,end=" ")
print()

for no in range(1,6,2):
	print(no,end=" ")
print()

for no in range(1,4,2):
	print(no,end=" ")
print()

for no in range(1,2,2):
	print(no,end=" ")
print()

#step:2

end=10
while end>0:
	for no in range(1,end,2):
		print(no,end=" ")
	print()
	end-=2
	
#step:3

for end in range(10,0,-2):
	for no in range(1,end,2):
		print(no,end=" ")
	print()
	end-=2
	
RESULT:
1 3 5 7 9 
1 3 5 7 
1 3 5 
1 3 
1 
##############################################################################
