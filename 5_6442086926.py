src = input("Your name and lastname:")
src_li = []
for i in range(len(src)):
	if src[i]!=" ":
		src_li.append(src[i])
		
		
for i in range(len(src_li)):
	src_li[i] = ord(src_li[i])
	
a = 0
for i in range(len(src_li)):
	a+=src_li[i]
	

