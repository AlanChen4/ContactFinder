import httplib2

from bs4 import BeautifulSoup, SoupStrainer

class email_scraper():
	'''finds emails on given webpage'''

	def __init__(self):
		self.http = httplib2.Http()
		self.status, self.response = self.http.request('https://wcu.campuslabs.com')

		self._contact_links = []


	def find_link(self):
		'''finds all href tags on a webpage and appends to self._contact_links'''
		for link in BeautifulSoup(self.response, features='html.parser', parse_only=SoupStrainer('a')):
		    if link.has_attr('href'):
		        self._contact_links.append(link['href'])

		if self._contact_links:
			for link in self._contact_links:
				print(link)
		else:
			print('-no links found')

if __name__ == '__main__':
	e_s = email_scraper()
	e_s.find_link()