def printprime(start,stop):
	primelist=[]
	for num in range(start,stop+1):
		if num > 1:
			for ii in range(2,num):
				if(num%i) == 0:
					break
				else:
					primelist.append(num)
					
	return primelist
	
	
	
print(printprime(0,980))
		
