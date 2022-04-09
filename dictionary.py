
Dictionary(key - value : pair)
          (key - unique, value - Dupliate)
	      Example : hotel menu

*) Dictionaries are used to store data values in 
   key:value pairs.
*) A dictionary is a collection which is ordered*,
   changeable and do not allow duplicates.
*) Dictionaries are written with curly brackets, 
   and have keys and values.
*) Dictionary items are ordered 
*) Changeable 
*) Does not allow duplicates.
*) Dictionary items are presented in key:value pairs,
   and can be referred to by using the key name.
*) Length
*) When we say that dictionaries are ordered, it 
   means that the items have a defined order, and
   that order will not change.
*) Unordered means that the items does not have a
   defined order, you cannot refer to an item by 
   using an index.

d = {}
s = dict()
 #  key       value
d['pongal'] = 60
d['poori']  = 60
d['idli']   = 40
d['dosai']  = 50

print(d)     
           -->op: {'pongal': 60, 'poori': 60, 'idli': 40, 'dosai': 50}
   
print(d['pongal'])     -->op: 60

-------------------------------------------------------

bills = {}

no_of_months = int(input("Enter no. of Month:"))

i = 1
while i<=no_of_months:
	month = input("Enter Month Name: ")
	amount = int(input('Enter Amount: '))
	bills[month] = amount
	i+=1
else:
	print('bills',bills)

RESULT:

Enter no. of Month:3
Enter Month Name: jan 
Enter Amount: 200
Enter Month Name: feb
Enter Amount: 250
Enter Month Name: mar
Enter Amount: 300
bills {'jan': 200, 'feb': 250, 'mar': 300}

	
for bill in bills:
	print('bill',bill)
	print('each value:',bills[bill])
	
RESULT:

bill jan
each value: 200
bill feb
each value: 250
bill mar
each value: 300

print(bills.keys())    --> op: dict_keys(['jan', 'feb', 'mar'])
print(type(bills.keys()))       --> op: <class 'dict_keys'>

print(bills.values())   --> op: dict_values([200, 250, 300])
print(type(bills.values()))     --> op: <class 'dict_values'>

print(bills.items()) -->op:dict_items([('jan', 200), ('feb', 250), ('mar', 300)])   
print(type(bills.items()))       -->op: <class 'dict_items'>

print(bills.keys())      -->op: dict_keys(['jan', 'feb', 'mar'])
for month in bills.keys():
	print(month)                

RESULT:
jan
feb
mar

print(bills.values())     --> op: dict_values([200, 250, 300])
for amount in bills.values():
	print(amount)

RESULT:
200
250
300
	
print(bills.items()) -->op:dict_items([('jan', 200), ('feb', 250), ('mar', 300)])
for month, amount in bills.items():
	print('I Paid',amount,'for',month)

RESULT:
	
I Paid 200 for jan
I Paid 250 for feb
I Paid 300 for mar

--------------------------------------------------------

d = {'name': 'sugavanam', 'age':24}
print(d.get('name'))
print(d['name'])
print(d.get('Degree','Not mentioned'))
print(d['degree'])

RESULT:

sugavanam
sugavanam
Not mentioned
KeyError: 'degree'

---------------------------------------------------------