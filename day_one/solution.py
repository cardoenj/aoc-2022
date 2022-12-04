

def part_one_and_two():
	reindeer_with_most = 0
	most = 0
	totals = []
	with open("input.dat") as fp:
		reindeers = fp.readlines()
		curr_sum = 0
		reindeer = 0
		for rd in reindeers:
			if rd == "\n":
				if most < curr_sum:
					most = curr_sum
					reindeer_with_most = reindeer
				totals.append(curr_sum)
				reindeer += 1
				curr_sum = 0
			else:
				print(rd + " add to reindeer " + str(reindeer))
				curr_sum += int(rd)


	print(reindeer_with_most)
	print(most)
	print(sum(sorted(totals,reverse=True)[:3]))
	
part_one_and_two()
