Set-{flower bracers} - mathematical set

No duplicate elements are allowed
No order means No indexing means No slicing
 

s = {10,20,30,40}
print(s)                     --> op: {40, 10, 30, 20}
print(type(s))               --> op: <class 'set'>

	
****changing str to list to set****
	
s='AAAABBBBCCCDDD'      # actual op in loop: ABCD 
l = list(s)
print(l)    -->op:['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D']
s = set(l)
print(s)                     --> op: {'A', 'D', 'B', 'C'}
	
s = set(range(5))
print(s)                     --> op: {1, 2, 3, 0, 4}
	
s.add(10)
s.add(20)
print("add used for single value:",s)

    --> op: add use for single value: {0, 1, 2, 3, 4, 10, 20}                     
			
l = [100,200,300]
s.update(l)           # update used for adding multi elements
print(s)           -->op:{0, 1, 2, 3, 4, 100, 200, 10, 300, 20}
s.update(123)
print(s)           -->op:TypeError: 'int' object is not iterable
		
s1 = s.copy()
print("s1=s.copy() = ",s1) -->op:{0, 1, 2, 3, 4, 100, 200, 10, 300, 20}

print(s1.pop())          -->op: 0 (it pops first digit doubt)
	
s1.remove(10)     
print(s1)         -->op: {1, 2, 3, 4, 100, 200, 300, 20}

s1.remove(10)     *** it shows error coz already removed ***
print(s1)         -->op: KeyError: 10
		
s1.discard(10)
print(s1)         -->op: {1, 2, 3, 4, 100, 200, 300, 20}
#*** discard doesn't show the error***

s1.clear()
print(s1)          -->op : set()
	
# what is the difference between remove and discard

s1 = {10,20,30,40}
s2 = {20,30,40,50}

print(s1.union(s2))           op:{40, 10, 50, 20, 30}
print("union",s1 | s2)        op:union {40, 10, 50, 20, 30}
print()

print(s1.intersection(s2))    op:{40, 20, 30}
print("intersection",s1 & s2) op:intersection {40, 20, 30}
print()

print(s1.difference(s2))      op:{10}
print("difference:s1-s2",s1 - s2)       op:difference:s1-s2 {10}
print("difference:s2-s1",s2 - s1)       op:difference:s2-s1 {50}
print()

 difference & sym diff -- unique value
	
print(s1.symmetric_difference(s2))      op:{10, 50}
print("symmetric_difference:",s1 ^ s2) # ^ - capsilan
                                        op:symmetric_difference: {10, 50}
			
# in not in
s = set('sugavanam')
print(s)               op:{'m', 'g', 'u', 's', 'n', 'a', 'v'}

#To remove repeated value

word = 'murugapandi'
s = {}              --> this empty bracers consider as dictionary
print(s.add("m"))   op:AttributeError: 'dict' object has no attribute 'add'

word = 'murugapandi'
s = set()              
print(s.add("m"))   op:None
print(s)            op:{'m'}
	

word = 'murugapandi'
s = set(word)              
print("m" in s)         op:True
print('m' not in s)     op:False
	
s3 = set()
for no in range(5):
	s3.add(no)
	
print(s3)        #op:{0, 1, 2, 3, 4}

s4 = {no for no in range(5)}
print(s4)       
                 #op:{0, 1, 2, 3, 4}
	

student = {'rahim', 56, 56.5, True, 'chennai'}
for value in student:
	if type(value) is str:
		print(value)
		
op:
chennai
rahim


frozenset(student)
