import web
from lotoparser import *

render = web.template.render('templates/')
urls = ('/', 'index')

class index:
	def GET(self):
		sorted_numbers_dict = get_sorted_numbers_dict()
		return render.index(sorted_numbers_dict)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
