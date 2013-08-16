import re
import urllib2
import operator

from BeautifulSoup import BeautifulSoup

def read_data():
	url = 'http://www.loto49.ro/arhiva-loto49.php'
	url_socket = urllib2.urlopen(url)

	data = url_socket.read()

	url_socket.close()

	return data

def get_numbers_dict(data):	
	soup = BeautifulSoup(data)
	all_rows = soup.findAll('tr')

	numbers_dict = {}

	for row in all_rows:
		columns = row.findAll('td')

		date = str(columns[0].contents[0])
		if re.match('([0-9]{4}\-[0-9]{2}\-[0-9]{2})', date) is not None:
			for column in columns[1:]:
				num = int(column.contents[0])
				if num in numbers_dict:
					numbers_dict[num] += 1
				else:
					numbers_dict[num] = 1

			first = int(columns[1].contents[0])
			second = int(columns[2].contents[0])
			third = int(columns[3].contents[0])
			fourth = int(columns[4].contents[0])
			fifth = int(columns[5].contents[0])
			sixth = int(columns[6].contents[0])

	return numbers_dict

def get_sorted_numbers_dict(data):
	numbers_dict = get_numbers_dict(data)

	sorted_numbers_dict = sorted(numbers_dict.iteritems(), key = operator.itemgetter(1), reverse = True)

	return sorted_numbers_dict
