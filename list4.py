"""
append - it print the given object or data in in single item at end 
		 eg:'sakthi' -- op: 'sakthi'
			
extend - it print the value after the existing value or at end of existing value
         it also print the given string or object or value separate individual items.
	    eg:"sakthi" -- op: 's','a','k','t','h','i'
				
Insert - it print the given value which place we choose or assisgn by index a=(2,34)

none   - is data type

pop    - it print or cut the last value  of index
         if you want to (pop/cut) specific value means index
	     eg:a=[1,2,3] --> a.pop(1) --> op:a=[1,3]
				
remove - remove just remove the value returns none and pop remove and gives back

indexerror - index out of range
valueerror - the value out of the data


"""		 

l = [10,20,30]
print(l)
l.insert(2,222)
print(l)

l2 = ['a','b','c']
l2.extend(l)
print(l2)

l2.extend("skathivel")
print(l2)
print(len(l2))

print(l2.remove("a"))
print(l2.pop())


print(l2.remove("w"))
print(l2.pop(20))

RESULT:
	
[10, 20, 30]
[10, 20, 222, 30]
['a', 'b', 'c', 10, 20, 222, 30]
['a', 'b', 'c', 10, 20, 222, 30, 's', 'k', 'a', 't', 'h', 'i', 'v', 'e', 'l']
16
None
30

x not in list
pop index out of range
##################################################################################
l = [10,20,30]
l.reverse()
print(l)            -->o/p:[30,20,10]

l = [10,20,30]
l = l.reverse()
print(l)            -->o/p:None
	
l = [10,20,30]
l.reverse()
print(l.reverse())  -->o/p:None
	
l = [20,10,30]
l.sort()             #-->Homogenous elements
print(l)              -->[10,20,30](categories)

print(max(l))         -->30

print(min(l))         -->10

print(sum(l))         -->60
##################################################################################
l1 = [10,20,30]
l2 = l1                 #Deep copy
print(id(l1))        --> op: 140586005212288 
print(id(l2))        --> op: 140586005212288

 #shallow copy(memboku)

l1 = [10,20,30]      
l2 = l1[:]            #slice operator
print(id(l1))        --> op: 140586004855744
print(id(l2))        --> op: 140586004856384
l2[0] = 111
print(l2)            --> op: [111,20,30] 
print(l1)            --> op: [10,20,30]

#List cloning

l1 = [10,20,30]
l2 = l1.copy()
print(id(l1))          --> op: 140647816756416
print(id(l2))          --> op: 140647816400000

#################################################################################
intake = 'sugavanam'
l = []
for letter in intake:
	print(letter)
	if letter not in l:
		l.append(letter)
else:
	for i in l:
		print(i,end=' ')

RESULT:
s
u
g
a
v
a
n
a
m
s u g a v n m

intake = "AAAABBBBCCCCDD"
l = []
for letter in intake:
	print(letter)
	if letter not in l:
		l.append(letter)
else:
	for i in l:
		print(i,end=' ')
		
intake = 'AAAABBBBCCCCDD'	
l = []
for i in range(len(intake)):
	print(intake[i])
	if intake[i] not in l:
		l.append(intake[i])
else:
	for no in l:
		print(no,end=' ')
		
RESULT:
A
B
B
B
B
C
C
C
C
D
D
A B C D
##############################################################################

#(HOMEWORK)

a = 'A1B2C3'
l = []
for i in range(len(a)):
	if a[i].isalpha():
		l.append(a[i])	
for i in range(len(a)):
	if a[i].isdigit():
		l.append(a[i])
print(l)

for letter in l:
	print(letter,end='')
print()


a = 'A1B2C3'
l = []
for i in a:
	if i.isalpha():
		l.append(i)
		
for i in a:
	if i.isdigit():
		l.append(i)
print(l)

for letter in l:
	print(letter,end='')
print()

#RESULT:

['A', 'B', 'C', '1', '2', '3']
ABC123
['A', 'B', 'C', '1', '2', '3']
ABC123

########################################################################
a='A1B2C3'
s=''
i=0
while i<len(a):
	if a[i].isalpha():
		s=s+a[i]
	i+=1
i=0
while i<len(a):
	if a[i].isdigit():
		s=s+a[i]
	i+=1
else:
	print(s)
	
RESULT:
ABC123
#########################################################################