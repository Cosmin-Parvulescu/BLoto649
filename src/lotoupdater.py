# Update the key, val pairs for loto numbers on the local Redis server.

import redis
from lotoparser import *

r = redis.StrictRedis(host = "localhost", port = 6379, db = 0)

# Fetch loto numbers from the loto archive page
# and add them to a Redis instance
loto_numbers = get_sorted_numbers_dict()
for key, val in loto_numbers:
	# Redis will keep the keys as 'bloto649:<number>'
	comp_key = "bloto649:" + str(key)

	current_val = r.get(comp_key)
	if val == current_val:
		continue
	else:
		r.set(comp_key, val)
