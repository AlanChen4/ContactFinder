import googlesearch
import json
import requests

from bs4 import BeautifulSoup, SoupStrainer

from college_helper import college
from output import output as csv_helper


class contact_scraper():
	'''finds emails on given webpage'''

	def __init__(self):
		self.session = requests.Session()
		self._website_links = []
		self._organization_list = []	
		self._keywords = ['engineer', 'environment', 'society']
		self._master_list = []


	def start_scraping(self):
		'''starts scraping process for each uni in the uni list'''
		uni_list = college.COLLEGES

		for uni_index, uni in enumerate(uni_list):
			if uni_index < 6:
				print('[SEARCHING][{}]'.format(uni_index+1))
				self.find_root_site(uni)

		self.begin_search()


	def find_root_site(self, uni_name):
		'''tries to find if uni is involved in campuslabs'''
		query = uni_name + 'campus labs'
		search_results = googlesearch.search(query, num=3, stop=1, pause=1)
		for result in search_results:
			if "campuslabs" in result:
				result = result.replace('organizations', '')
				self._website_links.append(result)
				print('\t|\n\t-->[ROOT SITE FOUND]', uni_name)


	def begin_search(self):
		'''starts the scraper, assumes that keywords and links are loaded properly'''
		self._website_links = list(set(self._website_links))

		# obtains all organization links from url
		for link in self._website_links:
			self._organization_list.append(self.get_organizations(link))

		# save all info to output.json for future data access
		self.output_to_json(self._organization_list)

		# obtains all matched keyword organizations
		for site_index, organizations in enumerate(self._organization_list):
			self.match_keywords(organizations=organizations, root_site=self._website_links[site_index])
		
		# prints all addresses
		for index, org_info in enumerate(self._master_list):
			print('[{}] {}'.format(index+1, org_info))

		# convert to .csv for easier viewing
		self.output_to_csv(self._master_list)
		

	def get_organizations(self, link):
		''' finds links within the website using requests made to the api'''
		try:
			api_exists = self.session.get(link + 'api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=2000&filter=&query=&skip=0')
		except requests.exceptions.ConnectionError:
			print('[ERROR]', link, 'could not be reached')
			return

		if 199 < api_exists.status_code < 300:
			try:
				organization_list = json.loads(api_exists.text)['value']
					
				print('[SUCCESS]', '{} links found for {}.'.format(len(organization_list), link))
				return organization_list
			except json.decoder.JSONDecodeError:
				# TODO: figure out why this happens
				print('[OKAY] JSON error')
		else:
			print('[DNE]', link)


	def match_keywords(self, organizations, root_site):
		'''goes through organization list and returns those that match the keyword search'''
		try:
			for club in organizations:
				k_counter = 0
				organization_name = club['Name'].lower()
				for k in self._keywords:
					if k in organization_name:
						k_counter+=1
						organization_contact = club['WebsiteKey']
						organization_contact = root_site + 'organization/{}/contact'.format(organization_contact)
						organization_info = {'name':organization_name, 'contact':organization_contact, 'keyword_matches': k_counter}
						self._master_list.append(organization_info)
		except TypeError:
			print('[OKAY] json error continuation')


	def output_to_json(self, data_value):
		'''output file to json format'''
		with open('college_helper/output.json', 'r+') as output_file:
			json.dump(data_value, output_file)


	def output_to_csv(self, data):
		'''converts to dictionaries and then updates to .csv'''
		c = csv_helper(data)
		c.to_csv('output.csv')

		

if __name__ == '__main__':
	e_s = contact_scraper()
	e_s.start_scraping()