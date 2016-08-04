def makeline(s,digit,i):
	if i==0:
		# top position
		if digit in [0,2,3,5,6,7,8,9]:
			return ' '+''.join(['-' for x in range(s)])+' '
		else:
			return ''.join([' ' for x in range(s+2)])
	elif i<=s:
		# middle bar
		if digit in [0,4,8,9]:
			return '|' +''.join([' ' for x in range(s)])+'|'
		elif digit in [1,2,3,7]:
			return ' ' + ''.join([' ' for x in range(s)])+ '|'
		else:
			return '|' + ''.join([' ' for x in range(s)])+ ' '
	elif i == s+1:
		# third position 
		if digit in [2,3,4,5,6,8,9]:
			return ' ' + ''.join(['-' for x in range(s)])+ ' '
		else:
			return ''.join([' ' for x in range(s+2)])
	elif i<=2*s+1:
		#fourth position
		if digit in [0,6,8]:
			return '|' + ''.join([' ' for x in range(s)]) + '|'
		elif digit in [1,3,4,5,7,9]:
			return ' ' + ''.join([' ' for x in range(s)]) + '|'
		else:
			return '|' + ''.join([' ' for x in range(s)]) + ' '
	else:
		# bottom position
		if digit in [0,2,3,5,6,8,9]:
			return ' ' + ''.join(['-' for x in range(s)]) + ' '
		else:
			return ''.join([' ' for x in range(s+2)])
def addigit(output,s,digit):
	for i in xrange(2*s+3):
		line = makeline(s,digit,i)
		output[i] += list(line)
def main():
	s,n = [int(x) for x in raw_input().split()]
	if s ==0:
		exit()
	result = [[] for x in xrange(2*s+3)]
	str_value = list(str(n))
	for digit in str_value:
		addigit(result,s, int(digit))
	
	for x in xrange(2*s+3):
		print ''.join(result[x])
	
	
if __name__ =="__main__":
	main()