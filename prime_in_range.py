def prime(x,y):
	prime_list=[]
	for i in range(x,y+1):
		if i==0 or i==1:
			continue
		for n in range(2,int(i/2)+1):
			if i%n==0:
				break
			else:
				continue
		else:
			prime_list.append(i)
	return prime_list

print(prime(0,2))
