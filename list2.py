#list is mutable
l = [10,20,30,40]

l[1] = 222
print(l)

i=0
while i<len(l):
	print(l[i])
	i+=1
	
for no in l:
	print(no)
############################################################	
#Multiple of twenty

l=[10,20,30,40,50,60,70,80,90]
count = 0
for no in l:
	if no%20==0:
		print(no)
		count+=1
print(count)

RESULT:
20
40
60
80
4

##############################################################	
#Multiple of twenty in reverse

l=[10,20,30,40,50,60,70,80,90]

le = len(l)-1
while le>0:
	if l[le]%20==0:
		print(l[le])
	le-=1

for no in l[::-1]:
	if no%20==0:
		print(no)
		
RESULT:
80
60
40
20

#############################################################

q = [78,67,76,89,90]
h = [65,45,35,93,97]
a = q+h
print(len(a))
print(a)

q[0]+h[0]
q[1]+h[1]
q[2]+h[2]
q[3]+h[3]
q[4]+h[4]

a=[]
i=0
while i<len(q):
	a.append(q[i]+h[i])
	i+=1
print(a)

a=[]
for i in range(len(q)):
	a.append(q[i]+h[i])
print(a)

RESULT:
10
[78, 67, 76, 89, 90, 65, 45, 35, 93, 97]
[143, 112, 111, 182, 187]
[143, 112, 111, 182, 187]
####################################################################
q = [78,67,76,89,90,76,49]
h = [65,45,35,93,97]

small = len(q) if len(q)<len(h) else len(h)

a=[]
i=0
while i<small:
	a.append(q[i]+h[i])
	i+=1
print(a)

a=[]
for i in range(small):
	a.append(q[i]+h[i]) 
print(a)

RESULT:
[143, 112, 111, 182, 187]
[143, 112, 111, 182, 187]

#####################################################################

l=[10,20,30,True]
print(l*3)

RESULT:
[10, 20, 30, True, 10, 20, 30, True, 10, 20, 30, True]


########################################################################
q=[45,50,66,76,57]
h=[67,87,56,45,58]
a=[82,73,76,77,54]
student = [q,h,a]
print(len(student))
print(student)


for marks in student:
	print(marks)

RESULT:
3
[[45, 50, 66, 76, 57], [67, 87, 56, 45, 58], [82, 73, 76, 77, 54]]
[45, 50, 66, 76, 57]
[67, 87, 56, 45, 58]
[82, 73, 76, 77, 54]

for marks in student:
	for mark in marks:
		print(mark,end=' ')
	print()
print(type(marks))

RESULT:
45 50 66 76 57
67 87 56 45 58
82 73 76 77 54
<class 'list'>

########################################################################
q=[45,50,66,76,57,87,56,45,58]
h=[67,87,56,45,58]

a=[]
for i in range(len(h)):
	a.append(q[i]+h[i])
ter=len(q) if len(q)>len(h) else len(h)
i=len(q)-len(h)+1
while i<ter:
	a.append(q[i])
	i+=1
print(a)


q=[45,50,66,76,57,87,56,45,58]
h=[67,87,56,45,58]

a=[]
for i in range(len(h)):
	a.append(q[i]+h[i])
ter=len(q) if len(q)>len(h) else len(h)
i=len(q)-len(h)+1
for no in range(i,ter):
	a.append(q[no])
print(a)

RESULT:
[112, 137, 122, 121, 115, 87, 56, 45, 58]

########################################################################
q=[45,50,66,76,57]
h=[67,87,56,45,50]
a=[67,87,56,45,58]

total=0
i=0
while i<len(q):
	total=total+q[i]
	i+=1
print(total)

total1 = 0
for i in range(len(q)):
	total1 = total1 + q[i]
	total2 = 0
	for i in range(len(h)):
		total2 = total2 + h[i]
	total3 = 0
	for i in range(len(a)):
		total3 = total3 + a[i]
print(total1)


print(total2)

total3 = 0
for i in range(len(a)):
	total3 = total3 + a[i]
print(total3)

total = total1 + total2 + total3
print(total)
print(total//3)

RESULT:
294
294
305
313
912
304

############################################################################

