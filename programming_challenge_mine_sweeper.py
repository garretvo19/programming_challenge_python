# translate from a C's code solution not pythonic writing 

def readmine(m,n, minesweeper):
	#line = [None]*100
	for i in xrange(m):
		line = raw_input()
		for j in xrange(n):
			if line[j] == '*':
				minesweeper[i][j] = -1
			else:
				minesweeper[i][j] = 0
	return minesweeper

def resolvefield(i,j,m,n, minesweeper):
	dr = [1, 1, 0, -1, -1, -1, 0, 1] # create grid indices 
	dc = [0, 1, 1, 1, 0, -1, -1, -1]
	for k in range(8):
		if (i + dr[k] < 0 or i + dr[k] >= m or j + dc[k] < 0 or j + dc[k] >= n):
			continue
		if (minesweeper[i + dr[k]][j + dc[k]] != -1):
			minesweeper[i + dr[k]][j + dc[k]] += 1
	return minesweeper
	
def printminesweeper(m,n,tc, minesweeper):
	tc = tc+1
	#print tc
	for i in xrange(m):
		for j in xrange(n):
			if minesweeper[i][j] == -1:
				print '*'
			else:
				print '%d' %minesweeper[i][j]
		#print '\n'
def main():
	minesweep = [[0 for x in range(100)] for y in range(100)]
	tc = 1
	while 1:
		m,n= [int(x) for x in raw_input().split()]
		if m!=n:
			break
		minesweep = readmine(m,n, minesweep)
		for i in range(m):
			for j in range(n):
				if minesweep[i][j] == -1:
					minesweep = resolvefield(i,j,m,n, minesweep)
		if tc > 1:
			print '\n'
		tc = tc+1
		#print tc
		for i in xrange(m):
			for j in xrange(n):
				if minesweep[i][j] == -1:
					print '*',
				else:
					print '%d' %minesweep[i][j],
			print '\n'
	
	
if __name__ =="__main__":
	main()