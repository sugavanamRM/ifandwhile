coconut=100
day=0
while cocount>0:
       coconut=coconut//2
       day=day+1
print("its takes",day,"days")
 
ALGORITHM:
*)Day zero,Man had 100 coconut he gave half of the coconut to his son on each day respectively
*)Find when the man have zero coconut
*)condition is untill it becomes zero
*)divide coconut by 2(coconut//2) each day (in python we use // floor division to eliminate factional number )
*)And add each day  plus one respectively (day=day+1)
*)When it becomes zero print(anwser)
stop the program
#############################################################################
amount=1
hour=10
while amount<=1024:
       amount=amount*2
       hour=hour+1
       print("it takes",hour)
if hour>12:
       print("times",hour-12,"pm")
else:
       print("times",hour,"am")
 
ALGORITHMS:
#HOUR 10=1 , AMT=2
#HOUR 11=2 , AMT=4
#HOUR 11=3 , AMT=8
#HOUR 11=4 , AMT=16
#HOUR 11=5 , AMT=32
#HOUR 11=7 , AMT=62
#HOUR 11=8 , AMT=128
#HOUR 11=9 , AMT=256
#HOUR 11=10 ,AMT=512
#HOUR 11=11 ,AMT=1024
#######################################################################
total=0
purse=2
day=1
while day<=10:
       total=total+purse
       purse=purse*2
       day=day+1
print("total amount",total)
 
ALGORITHMS:
#DAY = 0 , AMT = 0
#DAY = 1 , AMT = 1
#DAY = 2 , AMT = 2
#DAY = 3 , AMT = 4
#DAY = 4 , AMT = 8
#DAY = 5 , AMT = 16
#DAY = 6 , AMT = 32
#DAY = 7 , AMT = 62
#DAY = 8 , AMT = 128
#DAY = 9 , AMT = 256
#DAY = 10, AMT = 512
#DAY = 11, AMT = 1024
#DAY = 12, AMT = 2048