pwd            - present working directory
cd foldername/ - To open folder
cd --          - Back to home
cd~            - Back to home
ls             - (list) Open folder & files in folder
mkdir          - (make directory) Create new folder
rmdir          - (remove directory) Delete folder or files
rmdir          - It is delete only empty folders
clear          - To clear the terminal

rm -r (path)   - To delete folder and folder's file
Eg: 
	rm -r (/home/lando/Documents/vanam.txt)
	vanam.txt file deleted in Documents

touch file.txt - To Create new folder & files in folder
Eg: 
	(/home/lando/Documents/) touch vanam.txt
	vanam.txt created in Documents
	
cp sugav.txt(path)  -  copying file from one path to other path
Eg: 
	From copying Documents      to                   Desktop   
	/home/lando/Documents/ cp sugav.txt (/home/lando/Desktop/)

-----------------------------------------------------------------
Rename:
	(path) mv filename.txt filename.txt
	
Eg:
	/home/lando/Documents/ mv sugav.txt hello.txt
	File renamed as hello.txt
	
	/home/lando/Documents/ mv hello.txt sugav.txt
 	File renamed as sugav.txt
	
------------------------------------------------------------------
To read files:   -   path cat filename.txt 
Eg:     
    cat sugav.txt

	welcome to tamil linux user group
	I'm sugavanam
------------------------------------------------------------------
ECHO:
	(path) echo type anything
	
op:
	type anything
	
------------------------------------------------------------------
file overwrite:   -    (path) cat > filename.txt
	
Eg:
	/home/lando/Documents/ cat > sugav.txt
	this is sample file
	hello world 
	
To read file :
	/home/lando/Documents/ cat  sugav.txt
op: this is sample file
	
Again:
	/home/lando/Documents/ cat > sugav.txt
	sugav
	apple
	man
	blue
	red
	
output:
	/home/lando/Documents/ cat sugav.txt
	sugav
	apple
	man
	blue
	red
-------------------------------------------------------------------
Merge:    cat >> sugav.txt
	
	- merging text with existing text
INPUT:	 
lando@lando-Gateway-NE46Rs1:~/Documents$ cat >> sugav.txt
this is my yard now.. burn it down.. I am not a real person
^C

OUTPUT:
lando@lando-Gateway-NE46Rs1:~/Documents$ cat sugav.txt
sugav
apple
man
rin
red
this is my yard now.. burn it down.. I am not a real person
--------------------------------------------------------------------
Moving:   (path)  mv filename.extension (path)
	
~/Documents$ mv sugav.txt /home/lando/Desktop/
lando@lando-Gateway-NE46Rs1:~/Documents$ mv sugav.txt /home/lando/Desktop/
mv: cannot stat 'sugav.txt': No such file or directory
lando@lando-Gateway-NE46Rs1:~/Documents$ cd --
lando@lando-Gateway-NE46Rs1:~$ mv sugav.txt /home/lando/Documents/

--------------------------------------------------------------------

13:17