sys    - (2 to 4  functions)
os     - (2 to 4  functions)
math   - (2 to 4  functions)
random - (2 to 4  functions)
time   - (2 to 4  functions)
-------------------------------------------------------------
what are the pre-defined modules you know?
how to find modules in python
-------------------------------------------------------------
Example for importing function from two files on same folder

def add(no1,no2):
	return no1+no2

def sub(no1,no2):
	return no1-no2

def mul(no1,no2):
	return no1*no2

def div(no1,no2):
	return no1//no2

import first
 
print(first.add(100,20))    --> op: 120

from first import add

print(add(100,20))    --> op: 120
print(sub(10,20))     --> op: name 'sub' is not defined
	
---------------------------------------------------------------------
************import sys**************
its a in-built python module it is used for files in diferent
location to access on our working  files

import sys
print(sys.path)    --> op: it shows your 
	    --   python file location in your in which stored inn your system
print(sys.version) --> op: version of python in your system

# list of directories that the intrepreter will search for the required modules
#same folderla thedum or system path la thedum

#ungaluku theva padra module vera folder or vera computer la 
#irunthalo use - import sys - sys.path.append(module or file path)

import sys
sys.path.append('/home/lando/Videos') #now first.py is in Vedios

import first
print(first.add(10,20))    --> op: 30

-------------------------------------------------------------------------
sys module used to get ouput in command line from user
****(user kitta irundhu command line output tharum )****

import sys
level = sys.stdin.readline()
print(level)         ---> op: after entering file.py in terminal
	                         click enter and type your input
		                     (giving input without using input function
							  in terminal)
import sys
level = sys.stdin.readline(2)
print(level)          ---> op: input  --  sugavanam
                               output --  su
-------------------------------------------------------------------------
import sys
no = len(sys.argv)
print(sys.argv[0])        --> op: first.py
	
import sys
sys.argv #- it means what are the data user passed in terminal
print(sys.argv[0]) # in terminal -- python3 first.py
 
--> op: first.py    (python3 is key and first.py is arguments)

#system ku yenna argument pass panirkinga aathula first (sys.argv[0])
#yenna argument pass panirkinga
---------------------------------------------------------------------
import sys
no = len(sys.argv)
for i in range(1, no):
	print(sys.argv[i])
	
command line input--python3 first.py prabhagaran the true leader 1

prabhagaran
the
true
leader
1
---------------------------------------------------------------------

import first as f 
f.add(10,20)

---------------------------------------------------------------------
how to find modules in python

print(help('modules'))

---------------------------------------------------------------------
# dir -- used to know about particular modules what files are there?
#dir -- yentha modules pathi therinchikanum nalaum use dir
import time, random
print(dir(time))
print(dir(random))
----------------------------------------------------------------------
import math
print(math.sqrt(100))     --> op: 10.0
print(math.__name__)      --> op: math
----------------------------------------------------------------------
first.py
*****{
def add(no1,no2):
	return no1+no2

print(add(10,2))
					}*****

import first
print(dir(first))
print(first.__name__)

RESULT:
12
['__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__spec__', 'add']
first

-----------------------------------------------------------------------
print(dir(second))
print(second.__name__)

RESULT for both lines:

name 'second' is not defined
-----------------------------------------------------------------------
special variable:
	
print(__name__)      --> op: __main__ 
	
-----------------------------------------------------------------------