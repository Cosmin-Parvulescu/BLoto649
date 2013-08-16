import re
import urllib2
import operator

from BeautifulSoup import BeautifulSoup

def read_loto_data():
	url = 'http://www.loto49.ro/arhiva-loto49.php'
	url_socket = urllib2.urlopen(url)
	data = url_socket.read()
	url_socket.close()

	return data

def get_numbers_dict():	
	data = read_loto_data()

	# Get all rows from the document
	loto_soup = BeautifulSoup(data)
	all_rows = loto_soup.findAll('tr')

	numbers_dict = {}

	for row in all_rows:
		# For each row, get all the columns
		columns = row.findAll('td')

		# Check if the row starts with a date column (that way we know 6 numbers follow)
		# Note: It only works with the current layout of the loto archive
		date = str(columns[0].contents[0])
		if re.match('([0-9]{4}\-[0-9]{2}\-[0-9]{2})', date) is not None:
			for column in columns[1:]:
				# Get the numbers and add or increment their value in the dictionary
				num = int(column.contents[0])
				if num in numbers_dict:
					numbers_dict[num] += 1
				else:
					numbers_dict[num] = 1

	return numbers_dict

def get_sorted_numbers_dict():
	numbers_dict = get_numbers_dict()
	sorted_numbers_dict = sorted(numbers_dict.iteritems(), key = operator.itemgetter(1), reverse = True)

	return sorted_numbers_dict
