def printprime(start,stop):
    primelist = []
    for num in range(start,stop+1):  
     if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            primelist.append(num)

    return primelist


list = printprime(0,1840)

for i in range(len(list)):
    print(list[i])
		
