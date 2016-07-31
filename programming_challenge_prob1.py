def threenplus1(j,i):
	count = cycle = 1
	for n in xrange(i,j+1):
		count = 1 
		while (n !=1):
			if n % 2 ==0:
				n = n // 2
			else:
				n = n*3 + 1
			count = count + 1
		cycle = max(cycle,count)
	return cycle


def main():
	i, j = [int(x) for x in raw_input("Enter two numbers here: ").split()]
	n = threenplus1(j,i)
		
	print i,j,n
	
if __name__ =="__main__":
	main()