src = input("Your name and lastname:")
src_li = []
for i in range(len(src)):
	if src[i]!=" ":
		src_li.append(src[i])
		
print(src_li)
