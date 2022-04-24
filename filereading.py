f = open("one.txt", 'w')
-------------------------------------------------------------------
f = open("one.txt", 'w')
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print('Is file closed?',f.closed)
f.close()
print('Is file closed?',f.closed)

RESULT:
	
one.txt
w
False
True
Is file closed? False
Is file closed? True
------------------------------------------------------------------
f = open("one.txt", 'a') #a - APPEND, write - over write
name = ['python','linux','java']
f.writelines(name)
f.close()

RESULT:
sugavanamsakthivelmurugapandipythonlinuxjava

--------------------------------------------------------------