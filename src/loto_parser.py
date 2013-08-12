import re
import urllib2
import operator

from BeautifulSoup import BeautifulSoup

url = 'https://gist.github.com/Cosmin-Parvulescu/0f4f07137a7344f15cc5/raw/40fc760379f2ea90e05dcca1a29c6426ff3afb24/ArhivaLoto.html'
url_socket = urllib2.urlopen(url)

data = url_socket.read()

url_socket.close()

soup = BeautifulSoup(data)
all_rows = soup.findAll('tr')

numbers_dict = {}

res = open('result', 'w')

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

		res.write(date + ' | ' + str(first) + ', ' + str(second) + ', ' + str(third) + ', ' + str(fourth) + ', ' + str(fifth) + ', ' + str(sixth) + '\n')
		res.write(str(numbers_dict) + '\n\n')

res.close()

sorted_numbers_dict = sorted(numbers_dict.iteritems(), key = operator.itemgetter(1), reverse = True)

ord_res = open('ordered_result', 'w')

for key, val in sorted_numbers_dict:
	ord_res.write(str(key) + ' : ' + str(val) + '\n')

ord_res.close()
