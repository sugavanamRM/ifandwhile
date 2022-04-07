l = [10,12,15,25,28,46,67,89,90,92,100]
    #0  1  2  3  4  5  6  7  8  9  10
min = 0
max = len(l)-1
key = int(input('Enter key to search:'))
while min<=max:
	mid = (min+max)//2
	if key==l[mid]:
		print('your key of index value:',mid)
		break
	elif key<l[mid]:
		max = mid - 1
	else:
		min = mid + 1
else:
	print('key not found')


l = [10,12,15,25,28,46,67,89,90,92,100]
    #0  1  2  3  4  5  6  7  8  9  10
min = 0
max = len(l)-1
key = int(input('Enter value:'))
while min<=max:
	mid = (min+max)//2
	if key==l[mid]:
		print('your key of index value:',mid)
		break
	elif key>l[mid]:
		min = mid + 1
	else:
		max = mid - 1
else:
	print('key not found')
	