q=[80,90,100,70,60]
h=[90,80,80,70,60]
a=[100,100,90,70,60]

total = []
for sub in range(len(q)):
	#total[sub]=q[0]+h[0]+a[0]
	total.append(q[0]+h[0]+a[0])
#print(total[sub])
print(total)

RESULT:
[270, 270, 270, 210, 180]
############################################################################
q=[80,90,100,70,60]
h=[90,80,80,70,60]
a=[100,100,90,70,60]

marks = [q,h,a]
for m in marks:
	total = 0
	print("Before Inner Loop",m)
	for each_mark in m:
		total = total + each_mark
	print(total)
	print(total//5)

RESULT:
Before Inner Loop [80, 90, 100, 70, 60]
400
80
Before Inner Loop [90, 80, 80, 70, 60]
380
76
Before Inner Loop [100, 100, 90, 70, 60]
420
84

###########################################################################
q=[80,90,100,70,60]
h=[90,80,80,70,60]
a=[100,100,90,70,60]
marks = [q,h,a]
total = 0
for m in marks:
	print("Before Inner Loop",m)
	for each_mark in m:
		total = total + each_mark
	print(total)
	print(total//5)

RESULT:
Before Inner Loop [80, 90, 100, 70, 60]
400
80
Before Inner Loop [90, 80, 80, 70, 60]
780
156
Before Inner Loop [100, 100, 90, 70, 60]
1200
240

############################################################################

l1=[1,2,3]
l2=['a','b','c']

l3=[]
for i in range(len(l1)):
	l3.append(l1[i])
	l3.append(l2[i])
print(l3)

result = []
i=0
while i<len(l1):
	result.append(l1[i])
	result.append(l2[i])
	i+=1
print(result)

RESULT:
[1, 'a', 2, 'b', 3, 'c']

result=[l1[0],l1[1],l1[2],l2[0],l2[1],l2[2]]

l3=l1+l2
print(l3)

l3 = []

for i in l1:
	l3.append(i)

for i in l2:
	l3.append(i)

print(l3)

RESULT:
[1, 2, 3, 'a', 'b', 'c']

############################################################################

l1 = [10,20,30]
l2 = [40,50,60]
l3 = [70,80,90]

result=[l1,l2,l3]

for no in range(len(result)):
	#print(no)
	#print(result[no])
	for item in range(len(result[no])):
		print(result[no][item],end=' ')
	print()
	
RESULT:
10 20 30 
40 50 60 
70 80 90 

#############################################################################
l1 = [10,30,60]
l2 = [20,40,70]
l3 = [30,50,80]

result = [l1,l2,l3] 

result1=result[0][0]+result[1][0]+result[2][0]
result2=result[0][1]+result[1][1]+result[2][1]
result3=result[0][2]+result[1][2]+result[2][2]


no=0
total=0
for i in range(len(result)):
	#print(result[i][no])
	total=total+(result[i][no])
print("column 1",total)
print()

no=1
total=0
for i in range(len(result)):
	#print(result[i][no])
	total=total+(result[i][no])
print("column 2",total)
print()

no=2
total=0
for i in range(len(result)):
	#print(result[i][no])
	total=total+(result[i][no])
print("column 3",total)
print()



no=0
while no<len(result):
	i=0
	total=0
	while i<len(result):
		total=total+(result[i][no])
		i+=1
	print(total)
	no+=1

for no in range(len(result)):
	total=0
	for i in range(len(result)):
		total = total + (result[i][no])
	print(total)
	
RESULT:
column 1 60
column 2 120
column 3 210
60
120
210

################################################################################

(HOME WORK)

l1 = [10,30,60]
l2 = [20,40,70]
l3 = [30,50,80]

result = [l1,l2,l3] 

result1=result[0][0]+result[0][1]+result[0][2]
result2=result[1][0]+result[1][1]+result[1][2]
result3=result[2][0]+result[2][1]+result[2][2]

print("row 1",result1)
print("row 2",result2)
print("row 3",result3)

for no in range(len(result)):
	total = 0
	for i in range(len(result)):
		total = total + result[no][i]
	print(total)
print()

RESULT:
row 1 100
row 2 130
row 3 160
100
130
160


#################################################################################

l1 = [10,30,60]
l2 = [20,40,70]
l3 = [30,50,80]

result = [l1,l2,l3] 
result1=result[2][0]+result[1][1]+result[0][2]


i=2
no=0
total=0
while no<len(result):
	total = total + result[i][no]
	no+=1
	i-=1
else:
	print("diagonal R-L",total)

no=2
total = 0
for i in range(len(result)):
	total = total + result[i][no]
	no-=1
print("diagonal R-L",total)
	
	
RESULT:
	
Diagonal R-L 130
Diagonal R-L 130
#######################################################################################

l1 = [10,30,60]
l2 = [20,40,70]
l3 = [30,50,80]

result = [l1,l2,l3] 
result2=result[0][0]+result[1][1]+result[2][2]


i=0
no=0
total=0
while no<len(result):
	total = total + result[i][no]
	no+=1
	i+=1
else:
	print("diagonal L-R",total)

no=0
total = 0
for i in range(len(result)):
	total = total + result[i][no]
	no+=1
print("diagonal L-R",total)


RESULT:
	
Diagonal L-R 130
Diagonal L-R 130
################################################################################
