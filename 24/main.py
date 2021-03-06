# Advent of code day 24 part 1 challenge
# http://adventofcode.com/day/24
# Tiago Almeida, 2015


items = [1,2,3,5,7,13,17,19,23,29,31,37,
		41,43,53,59,61,67,71,73,79,83,89,
		97,101,103,107,109,113]


def part1():
	"""
	Solution approach:
	 - calculate compartment weight (cw) for each compartment (cw)
	 - generate combinations of N items for all N from 1
	 	to N that have correct weight. 
	 	Stop when you find at least one combination of items
	 	as this will give at least one combination with minimum 
	 	number of items and correct weight. 
	 - Mnimize the entanglement and return the value
	"""
	# get compartment weight (cw) for each compartment
	cw = sum(items) / 3
	# brute force approach. get combinations of N items that match cw
	# start with 2 items, then increase number of items until 1 or more 
	# combinations with weight cw are found
	from itertools import combinations
	for n in range(1, len(items)+1):
		combos = [ x for x in combinations(items,n) if sum(x) == cw ] 
		# combos -> combinations of n items with weight cw
		if combos:
			break
	# minimize entanglement
	min_combo = min(combos, key=entanglement)
	return entanglement(min_combo)


def entanglement(combination):
	"""
	Returns product of items' weights
	combination is a list of items
	"""
	from functools import reduce
	return reduce(lambda x,y: x*y, combination)


if __name__ == '__main__':
	print(part1())