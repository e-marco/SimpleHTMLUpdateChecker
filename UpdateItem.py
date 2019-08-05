class UpdateItem:
	def __init__(self, name, url, re_pattern, installed_version, is_verbose):
		self.status = True
		self.is_verbose = is_verbose
		self.new_version = False
		warning_info = ""
		
		if len(name) > 0:
			self.name = name
		else:
			self.status = False
			warning_info += "Empty software name "
		
		if len(url) > 0:
			self.url = url
		else:
			self.status = False
			warning_info += "Empty URL "
			
		if len(re_pattern) > 0:
			self.re_pattern = re_pattern
		else:
			self.status = False
			warning_info += "Empty search pattern "
			
		if len(installed_version) > 0:
			self.installed_version = installed_version
			self.version_info = installed_version
		else:
			self.status = False
			warning_info += "Empty version "
		
		if self.status:
			self.message = "Info: UpdateItem initialization okay"
		else:
			self.message = "Warning: " + warning_info
			
		if self.is_verbose:
			print(self.message)