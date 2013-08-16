# Returns occurrences for any or all numbers in the loto archive.

import redis

r = redis.StrictRedis(host = "localhost", port = 6379, db = 0)

def get_occurences(number):
	comp_key = "bloto649:" + str(number)
	occurences = r.get(comp_key)

	return occurences

def get_all_occurences():
	numbers_dict = {}

	for i in range(1, 50):
		comp_key = "bloto649:" + str(i)

		number = i
		occurences = r.get(comp_key)

		numbers_dict[number] = occurences

	return numbers_dict
		
	
