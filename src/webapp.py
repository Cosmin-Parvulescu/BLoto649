import re
import urllib2
import operator

from BeautifulSoup import BeautifulSoup

import web

render = web.template.render('templates/')
urls = ('/', 'index')

def get_sorted_numbers_list():
	url = 'https://gist.github.com/Cosmin-Parvulescu/0f4f07137a7344f15cc5/raw/40fc760379f2ea90e05dcca1a29c6426ff3afb24/ArhivaLoto.html'
	url_socket = urllib2.urlopen(url)
	data = url_socket.read()
	url_socket.close()

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


	sorted_numbers_dict = sorted(numbers_dict.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sorted_numbers_dict

class index:
	def GET(self):
		sorted_numbers_dict = get_sorted_numbers_list()
		return render.index(sorted_numbers_dict)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
