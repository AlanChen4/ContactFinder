import httplib2
import json
import requests

from bs4 import BeautifulSoup, SoupStrainer

class email_scraper():
	'''finds emails on given webpage'''

	def __init__(self):
		self.session = requests.Session()
		self.http = httplib2.Http()
		# self.status, self.response = self.http.request('https://gobblerconnect.vt.edu/')

		self._website_links = ['https://gobblerconnect.vt.edu/', 'https://gatech.campuslabs.com/engage/', 'https://wcu.campuslabs.com/engage/']
		self._website_links = ['https://gobblerconnect.vt.edu/'] # delete this later
		
		self._keywords = ['earth', 'engineer']
		self._master_list = []
	
	def begin_search(self):
		'''starts the scraper, assumes that keywords and links are loaded properly'''
		self._organization_list = []	

		# obtains all organization links from url
		for link in self._website_links:
			self._organization_list.append(self.get_organizations(link))

		# obtains all matched keyword organizations
		for organizations in self._organization_list:
			self.match_keywords(organizations)

		# debug stuff
		for i in self._master_list:
			print(i)

	def get_colleges(self):
		''' return list of ~7000 colleges to scrape'''
		colleges = []
        with open('data/colleges.txt', 'r') as c:
        	unfiltered_colleges = c.readlines()

        for i in unfiltered_colleges:
            colleges.append(i.rstrip('\n'))

		return colleges
		
	def get_organizations(self, link):
		''' finds links within the website using requests made to the api'''
		try:
			api_exists = self.session.get(link + 'api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=2000&filter=&query=&skip=0')
		except requests.exceptions.ConnectionError:
			print('[ERROR]', link, 'could not be reached')
			return

		if 199 < api_exists.status_code < 300:
			organization_list = json.loads(api_exists.text)['value']
			print('[SUCCESS]', '{} links found for {}.'.format(len(organization_list), link))
			return organization_list
		else:
			print('[DNE]', link)


	def match_keywords(self, organizations):
		'''goes through organization list and returns those that match the keyword search'''
		
		# TODO: add keyword feature
		for o in organizations:
			organization_name = o['Name'].lower()
			for k in self._keywords:
				if k in organization_name:
					self._master_list.append(organization_name)
					continue
		

if __name__ == '__main__':
	e_s = email_scraper()
	e_s.begin_search()