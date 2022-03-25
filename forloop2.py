#1  2  3  4  5
#2  3  4  5
#3  4  5
#4  5
#5

for no in range(1,6):
	print(no,end=' ')
print()

for no in range(2,6):
	print(no,end=' ')
print()
for no in range(3,6):
	print(no,end=' ')
print()
for no in range(4,6):
	print(no,end=' ')
print()
for no in range(5,6):
	print(no,end=' ')
print()



end=1
while end<7:
	for no in range(end,6):
		print(no,end=' ')
	print()
	end=end+1

for end in range(1,6):
	for no in range(end,6):
		print(no,end=' ')
	print()
	end=end+1
############################################################################
#1  2  3  4  5
#1  2  3  4
#1  2  3 
#1  2 
#1

for no in range(1,6):
	print(no,end=' ')
print()

for no in range(1,5):
	print(no,end=' ')
print()
for no in range(1,4):
	print(no,end=' ')
print()
for no in range(1,3):
	print(no,end=' ')
print()
for no in range(1,2):
	print(no,end=' ')
print()

for end in range(6,1,-1):
	for no in range(1,end):
		print(no,end=' ')
	print()
	end=end+1


for n in range(6,1,-1):
	for no in range(1,n):
		print(no,end=' ')
	print()
	n=n-1
	
###############################################################################
	
#1
#1  2
#1  2  3  
#1  2  3  4  
#1  2  3  4  5

for no in range(1,2):
	print(no,end=' ')
print()

for no in range(1,3):
	print(no,end=' ')
print()
for no in range(1,4):
	print(no,end=' ')
print()
for no in range(1,5):
	print(no,end=' ')
print()
for no in range(1,6):
	print(no,end=' ')
print()


n=2
while n<7:
	for no in range(1,n):
		print(no,end=' ')
	print()
	n=n+1

for n in range(2,7):
	for no in range(1,n):
		print(no,end=' ')
	print()

#################################################################################
	

no = int(input("Enter value:"))
for i in range (1,no+1):
	print(i,end=" ")
	print(i)
	
Enter value:5
1 1
2 2
3 3
4 4
5 5
#################################################################################

no=int(input("Enter thee value:"))
for i in range(1,no+1):
	print("* "*i)
	
Enter thee value:5
* 
* * 
* * * 
* * * * 
* * * * * 
##################################################################################

no = int(input("Enter value:"))
for i in range (1,no+1):
	print("* "*i,end=" ")
	print("H "*(5-i))

Enter value:5
*  H H H H 
* *  H H H 
* * *  H H 
* * * *  H 
* * * * *  
##################################################################################
no = int(input("Enter value:"))
for i in range (1,no+1):
	print("  "*i,end=" ")
	print("H "*(5-i))

Enter value:5
   H H H H 
     H H H 
       H H 
         H 
          
##################################################################################

no = int(input("Enter value:"))
for i in range (1,no+1):
	print(" "*i,end=" ")
	print("H "*(5-i))

Enter value:5
  H H H H 
   H H H 
    H H 
     H 

##################################################################################

no = int(input("Enter value:"))
for i in range (1,no+1):
	print(""*i,end=" ")
	print("H "*(5-i))

Enter value:5
 H H H H 
 H H H 
 H H 
 H 

#################################################################################	
end=6
for i in range(1,6):
	print("* "*i,end=" ")
	for i in range(1,end):
		print(i,end=" ")
	print()
	end-=1
	
*  1 2 3 4 5 
* *  1 2 3 4 
* * *  1 2 3 
* * * *  1 2 
* * * * *  1 
	
#############################################################################

end=6
for i in range(1,6):
	print(" "*i,end=" ")
	for i in range(1,end):
		print(i,end=" ")
	print()
	end-=1
	
  1 2 3 4 5 
   1 2 3 4 
    1 2 3 
     1 2 
      1 
##############################################################################

end=6
for i in range(1,6):
	print("  "*i,end=" ")
	for i in range(1,end):
		print(i,end=" ")
	print()
	end-=1
	
   1 2 3 4 5 
     1 2 3 4 
       1 2 3 
         1 2 
           1 

##############################################################################
		
for i in range(5,0,-1):
	print("* "*i)
		
* * * * * 
* * * * 
* * * 
* * 
* 

#############################################################################
for i in range(1,6):
	print("* "*i)
	
* 
* * 
* * * 
* * * * 
* * * * * 

############################################################################

for i in range(5,0,-1):
	print("* "*i,end=" ")
	for w in range(1,6):
		print(w,end=" ")
	print()
	
* * * * *  1 2 3 4 5 
* * * *  1 2 3 4 5 
* * *  1 2 3 4 5 
* *  1 2 3 4 5 
*  1 2 3 4 5 

###########################################################################

no=2
for i in range(5,0,-1):
	print("* "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no+=1
	
* * * * *  1 
* * * *  1 2 
* * *  1 2 3 
* *  1 2 3 4 
*  1 2 3 4 5 
###########################################################################

no=2
for i in range(5,0,-1):
	print("  "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no+=1

	
           1 
         1 2 
       1 2 3 
     1 2 3 4 
   1 2 3 4 5

#################################################################

no=2
for i in range(5,0,-1):
	print(" "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no+=1

      1 
     1 2 
    1 2 3 
   1 2 3 4 
  1 2 3 4 5 

##################################################################
##################################################################
for i in range(1,6):
	print(i,end=" ")
print()
for i in range(1,5):
	print(i,end=" ")
print()
for i in range(1,4):
	print(i,end=" ")
print()
for i in range(1,3):
	print(i,end=" ")
print()
for i in range(1,2):
	print(i,end=" ")
print()

no=6
while no>1:
	for i in range(1,no):
		print(i,end=" ")
	print()
	no-=1

for no in range(6,1,-1):
	for i in range(1,no):
		print(i,end=" ")
	print()

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
##########################################################################

for i in range(1,2):
	print(i,end=" ")
print()
for i in range(1,3):
	print(i,end=" ")
print()
for i in range(1,4):
	print(i,end=" ")
print()
for i in range(1,5):
	print(i,end=" ")
print()
for i in range(1,6):
	print(i,end=" ")
print()

no=2
while no<7:
    for i in range(1,no):
		print(i,end=" ")
	print()
	no+=1

for no in range(2,7):
	for i in range(1,no):
		print(i,end=" ")
	print()

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

################################################################

no=6
for i in range(0,6):
	print("  "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no-=1

	
 1 2 3 4 5 
   1 2 3 4 
     1 2 3 
       1 2 
         1 

#################################################################

no=2
for i in range(5,0,-1):
	print("  "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no+=1

           1 
         1 2 
       1 2 3 
     1 2 3 4 
   1 2 3 4 5 
##################################################################
no=2
for i in range(5,0,-1):
	print(" "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no+=1

      1 
     1 2 
    1 2 3 
   1 2 3 4 
  1 2 3 4 5 
#########################################################################

no=6
for i in range(0,6):
	print(" "*i,end=" ")
	for w in range(1,no):
		print(w,end=" ")
	print()
	no-=1
	
 1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1 
      
##########################################################################
