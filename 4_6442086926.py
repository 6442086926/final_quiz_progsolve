def search_alp(list,alp):
	def search_recursive(lst,num):
		if lst[0] == num:
			return bool(1)
		return search_recursive(lst[1:],num)
	try: return search_recursive(list,alp)
	except IndexError: return bool(0)
	
	
	
list = ['p', 'o', 'o', 'r', 'i', 's', 'h', 'c', 'h', 'a', 'r', 'o', 'e', 'n', 'k', 'u', 'l']

print(search_alp(list,'a'))
