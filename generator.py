Generator:

return - it stores all values and return 
yield  - it gives one value at a time (next())
Advantage of generator is memory consumption

def generator():
	yield "One"
	yield "Two"
	yield "Three"
	
results = generator()
print(type(results))  --> <class 'generator'>
print(results)        --> <generator object generator at 0x7f5af44b7740>
print(next(results))  --> one   
print(next(results))  --> two
print(next(results))  --> three

--------------------------------------------------------------------------
def countdown(num):
	while num>0:
		print(num)
		num-=1

countdown(5)

RESULT:
5
4
3
2
1
-------------------------------------------------------------------
#yield - giving (kudukarathu)
def countdown(num):
	while num>0:
		yield num
		num-=1

values = countdown(5)
print(type(values))  --> <class 'generator'>
print(values)        --> <generator object countdown at 0x7f4c1af0d740>
print(next(values))  --> 5
print(next(values))  --> 4
print(next(values))  --> 3

------------------------------------------------------------------------
l = [no*no for no in range(1,10000000000)]
print(l[0])
print(l[1])
print(l[2])

RESULT:
	
system hangs

-------------------------------------------------------------------------
gen = (no*no for no in range(1,10000000000))
print(next(gen))   -->1
print(next(gen))   -->4
print(next(gen))   -->9
print(next(gen))   -->16
print(next(gen))   -->25

-------------------------------------------------------------------------