import UpdateItem as ui
import os.path
from shutil import copyfile

class UpdateFileReader:
	def __init__(self, filename, is_verbose):
		self.status = True
		self.is_verbose = is_verbose
		self.filename = filename
		self.currentlineindex = 0
		
		if len(filename) > 0:
			self.filename = filename
		else:
			self.status = False
			warning_info = "Empty filename"
		
		if self.status:
			if os.path.isfile(self.filename) == False:
				self.status = False
				warning_info = "File does not exist"
			
		if self.status:
			self.message = "Info: UpdateFileReader initialization okay"
		else:
			self.message = "Warning: " + warning_info
			
		if self.is_verbose:
			print(self.message)
	
	def getNextItem(self):
		if self.status != True:
			if self.is_verbose:
				print("Warning: UpdateFileReader not initialized")
			return None
		else:
			try:
				fileHandle = open(self.filename, 'r', encoding='utf-8')
				lines = fileHandle.readlines()
				fileHandle.close()
			except:
				self.status = False
				self.message = "File could not be read."
				if self.is_verbose:
					print(self.message)
				return None
				
			if self.currentlineindex < len(lines):
				current_line = lines[self.currentlineindex]
				current_line = current_line.strip()
				self.currentlineindex += 1
				return True
			else:
				return None
				
	def getCurrentItemData(self):
		if self.status != True:
			if self.is_verbose:
				print("Warning: UpdateFileReader not initialized")
			return None
		else:
			try:
				fileHandle = open(self.filename, 'r', encoding='utf-8')
				lines = fileHandle.readlines()
				fileHandle.close()
			except:
				self.status = False
				self.message = "File could not be read."
				if self.is_verbose:
					print(self.message)
				return None
				
			if self.currentlineindex <= len(lines):
				current_line = lines[self.currentlineindex-1]
				current_item = extractData(current_line, self.is_verbose)
				
				if current_item is None:
					self.status = False
					self.message = "Error: Reading info for " + current_line
				else:
					self.message = "Info: Reading info for " + current_item.name + " okay"
				
				if self.is_verbose:
					print(self.message)
				
				if self.status:
					return current_item
				else:
					return None
			else:
				return None
				
	def updateCurrentItemData(self, UpdateItem):
		if self.status != True:
			if self.is_verbose:
				print("Warning: UpdateFileReader not initialized")
			return None
		else:
			try:
				fileHandle = open(self.filename, 'r', encoding='utf-8')
				lines = fileHandle.readlines()				
				fileHandle.close()
			except:
				self.status = False
				self.message = "File could not be read."
				if self.is_verbose:
					print(self.message)
				return None
				
			if self.currentlineindex <= len(lines):
				if UpdateItem.status:
					# create backup
					copyfile(self.filename,"backup.tmp")
					try:
						lines[self.currentlineindex-1] = UpdateItem.name + ";" + UpdateItem.url + ";" + UpdateItem.re_pattern + ";" + UpdateItem.installed_version + "\n"
						fileHandle = open(self.filename, 'w', encoding='utf-8')
						fileHandle.writelines(lines)
						fileHandle.close()
						os.remove("backup.tmp")
						self.message = "Info: File updated successfully"
					except:
						self.status = False
						self.message = "Error: Writing file. Please use backup.tmp"
						
				else:
					self.status = False
					self.message = "Warning: UpdateItem invalid"
							
				if self.is_verbose:
					print(self.message)
				if self.status:
					return self
				else:
					return None
			else:
				return None
				
def extractData(line, is_verbose):
	try:
		line = line.strip()
		current_data = line.split(';')
		current_item = ui.UpdateItem(current_data[0], current_data[1], current_data[2], current_data[3], is_verbose)
		return current_item
	except:
		message = "Check file format."
		if is_verbose:
			print(message)
		return None