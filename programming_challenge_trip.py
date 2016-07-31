def main():
	#m = int(raw_input())
	while 1:
		num_student = raw_input()
		num_student = int(num_student)
		amount_spend = [0]*num_student
		total = 0
		pos_sum = 0
		neg_sum = 0
		diff = 0
		for i in range(num_student):
			amount_spend[i] = float(raw_input())
			total += amount_spend[i]
			if amount_spend[i] == 0:
				break
		average = total/num_student
		for i in range(num_student):
			diff = ((amount_spend[i]-average)*100)/100
			diff = float(diff)
			if diff < 0:
				neg_sum += diff
			else:
				pos_sum += diff 
		if -neg_sum > pos_sum:
			exchange = -neg_sum
		else:
			exchange = pos_sum
		print exchange 
	
if __name__ =="__main__":
	main()