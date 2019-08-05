import requests # required for checking http response code
import ssl # required for accepting unverified ssl certificates
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request # require for requesting html source
import chardet # required to determine encoding
import re # regular expressions required for parsing source code

import UpdateItem

class UpdateChecker:
	def __init__(self, UpdateItem, is_verbose):
		self.status = True
		self.is_verbose = is_verbose
		self.new_version = False
		warning_info = ""
		
		try:
			self.name = UpdateItem.name
			self.url = UpdateItem.url
			self.re_pattern = UpdateItem.re_pattern
			self.installed_version = UpdateItem.installed_version
			self.version_info = self.installed_version
		except:
			self.message = "Error: Undefined input"
			self.status = False
			if self.is_verbose:
				print(self.message)
			
			return None
			
		if len(self.name) == 0:
			self.status = False
			warning_info += "Empty software name "
		
		if len(self.url) == 0:
			self.status = False
			warning_info += "Empty URL "
			
		if len(self.re_pattern) == 0:
			self.status = False
			warning_info += "Empty search pattern "
			
		if len(self.installed_version) == 0:
			self.status = False
			warning_info += "Empty version "
		
		# if all parameters non-empty, some more validity checking
		if self.status:
			if "(.*?)" not in self.re_pattern: 
				self.status = False
				warning_info += "Incorrect search pattern "
				
			try:
				r = requests.head(self.url)
				if r.status_code >= 400:
					self.status = False
					warning_info += "HTTP status: " + str(r.status_code)
			except requests.ConnectionError:
				self.status = False
				warning_info += "Failed to connect"
		
		if self.status:
			self.message = "Info: UpdateChecker initialization okay"
		else:
			self.message = "Warning: " + warning_info
			
		if self.is_verbose:
			print(self.message)
			
	def getCurrentVersion(self):
		if self.status != True:
			if self.is_verbose:
				print("Warning: UpdateChecker not initialized")
			return self
		else:
			# accept unverified ssl certificates
			ssl._create_default_https_context = ssl._create_unverified_context

			# headers to improving response
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
					 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
					 'Connection': 'keep-alive'}
			
			try:
				request=urllib.request.Request(self.url,None,headers) # assembled request
				fp = urllib.request.urlopen(request)
				mybytes = fp.read()
				
				# detect encoding
				result = chardet.detect(mybytes)
				charenc = result['encoding']
				
				# decode response
				html_source = mybytes.decode(charenc)
				
				fp.close()
			except:
				self.status = False
				self.message = "Error: Could not read from URL " + url
				if self.is_verbose:
					print(self.message)
				return self
			
			if self.status:
				try:
					search_result = re.search(self.re_pattern, html_source)
				except:
					search_result = None
					self.status = False
					self.message = "Error: Check search pattern or HTML source"
					if self.is_verbose:
						print(self.message)
					return self
			
				if search_result:
					installed_version = self.installed_version.strip()
					current_version = search_result.group(1)
					current_version = current_version.strip()
					
					if current_version!=installed_version:
						self.new_version = True
						self.version_info = current_version
						self.message = "Info: New version " + current_version + " for " + self.name
						if self.is_verbose:
							print(self.message)
						return self						
					else:
						self.message = "Info: No new version for " + self.name
						if self.is_verbose:
							print(self.message)
						return self
						
				else:
					self.status = False
					self.message = "Warning: Source code for " + self.name + " may have changed"
					if self.is_verbose:
						print(self.message)
					return self
			else:
				if self.is_verbose:
					print("Error: Unknown error")
				return self