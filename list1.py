details = []
details.append('sugavanam')
details.append(450)
details.append('4/5')
details.append(True)
details.append(['abcd',123,False])

print(details)
print(len(details))

RESULT:
	
['sugavanam', 450, '4/5', True, ['abcd', 123, False]]
5
###############################################################

details = ['abcd',123,False]
details.append('kumar')
print(details)
print(len(details))

#difference - insert and append

details.insert(1, 'bala')
print(details)
print(len(details))

print(details[0])
print(details[1])
print(details[2])
print(details[3])

#RESULT:

['abcd', 123, False, 'kumar']
4
['abcd', 'bala', 123, False, 'kumar']
5
abcd
bala
123
False
####################################################################

details = []

details.append('sugavanam')
details.append(450)
details.append('4/5')
details.append(True)

for i in range(len(details)):
	print(i)
	
RESULT:
0
1
2
3

####################################################################

s = 'bhargavi '
l = list(s)
print(l)

['b','h','a','r','g','a','v','i']

###################################################################
s = 'bhargavi sakthivel sugavanam'
l = s.split()
print(l)

['bhargavi','skathivel','sugavanam']

###################################################################

s = '28/03/2022'
l = s.split('/')
print(l)

['28','03','2022']

###################################################################

s = 'sugavanam'
l = s.split('a')
print(l)

['sug','v','n','m']

###################################################################

s = 'sugavanam'
l = s.split()
print(l)

print(l[::])
print(type(l[::]))
print(l[2:5])
print(l[2::])

['sugavanam']
['sugavanam']
<class 'list'>
[]
[]

#####################################################################

l = [10,20,30,40,50,60,70,80,90]
print(l)

print(l[::])
print(type(l[::]))
print(l[2:5])
print(l[2::])

[10, 20, 30, 40, 50, 60, 70, 80, 90]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
<class 'list'>
[30, 40, 50]
[30, 40, 50, 60, 70, 80, 90]

#####################################################################
