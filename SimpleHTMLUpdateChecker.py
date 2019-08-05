import UpdateItem as ui
import UpdateChecker as uc
import UpdateFileReader as ufr
import tkinter
from tkinter import messagebox

is_verbose = True

root = tkinter.Tk()
root.withdraw()

userfile = "updateList.txt"
currentReader = ufr.UpdateFileReader(userfile, is_verbose)

while currentReader.getNextItem():
	currentItem = currentReader.getCurrentItemData()
	if currentItem:
		currentSoftware = uc.UpdateChecker(currentItem, is_verbose)
		
		if currentSoftware.status:
			currentVersion = currentSoftware.getCurrentVersion()
			if currentVersion.new_version:
				msg_result = messagebox.askyesno("Update available for " + currentVersion.name,"Version " + currentVersion.version_info + " available for " + currentVersion.name + " (current: " + currentVersion.installed_version + ") Have you updated yet?")
				
				if msg_result:
					currentItem.installed_version = currentVersion.version_info
					currentReader.updateCurrentItemData(currentItem)