# Serve an HTML page with the loto numbers and their occurrences.

import web
from lotodata import *

render = web.template.render('templates/')
urls = ('/', 'index')

class index:
	def GET(self):
		numbers_dict = get_all_occurences()
		print numbers_dict
		return render.index(numbers_dict)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
