def getcandidate(voters,num_candidates):
# follow yubai lin's solution 
	lost_cand = set() # lost candidate vote value 
	current_votes = [0]*(num_candidates+1)
	for round in range(num_candidates):
		for vote in voters:
			if round == 0 or voters[round-1] in lost_cand:
				current_votes[voters[round]] +=1
		# get max and min value 
		max_val, maxP = -1, []
		min_val, minP = num_candidates, [] 
		for i in xrange(1,num_candidates+1):
			if i not in lost_cand:
				if current_votes[i] == max_val:
					maxP.append(i)
				elif current_votes[i] > max_val:
					max_val, maxP = current_votes[i], [i]
				if current_votes[i] == min_val:
						minP.append(i)
				elif current_votes[i] < min_val:
					min_val, minP = current_votes[i], [i]
					
		if max_val > num_candidates // 2 +1 :
			return maxP
		if min_val == max_val:
			return maxP
		for p in minP:
			lost_cand.append(p) 
			

def main():
	num_test = int(raw_input())
	for i in xrange(num_test):
		num_candidates = int(raw_input())
		names = []
		for j in xrange(num_candidates):
			names.append(raw_input().strip())
		votes = []
		while True:
			line = raw_input()
			if line == '':
				break
			votes.append([int(x) for x in line.split()])
		votes = [item for sublist in votes for item in sublist]
		winner = getcandidate(votes,num_candidates)
		print('\n'.join(names[e - 1] for e in winner)) 
if __name__ == "__main__":
	main()