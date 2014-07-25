# Update Filters by Podshot
# WIP Filter Updating ability by jgierer12
# This updates all filters that declare an UPDATE_URL and VERSION
import glob, urllib2, urllib, json, os, webbrowser, time, shutil

displayName = "Update Filters"
METHOD = "[Update Filters]"

inputs = (
	("Remove Old Filters?", True),
	("View Change Logs", False),
	("Include WIP versions", False),
	)

def perform(level, box, options):	 
	doRemove = options["Remove Old Filters?"]
	changeLog = options["View Change Logs"]
	includeWIPs = options["Include WIP versions"]
	filterDir = str(os.path.dirname(os.path.abspath(__file__)))
	# Gets the directory of where the "filters" is located
	try:
		os.mkdir("filters/updates")
	except OSError:
		pass
	filters = glob.glob("filters/*.py")
	# Search the "filters" folder for all files that have an extension of ".py"
	for filt in filters:
		filterUpdateURL = ""
		try:
			pyfile = filt[8:]
			# Removes the "filters/" from the filter path
			newName = pyfile.split(".")
			# __import__() does not like file extensions, so I remove the .py extension from the file name
			name = newName[0]
			update = __import__(name)
			# I use __import__() to import a filter from a string
			filterUpdateURL = update.UPDATE_URL
			# Grabs the declared variable name "UPDATE_URL"				   
			filterVersion = update.VERSION
			print '%s: %s:%s' % (METHOD, name, update.VERSION)
			# Grabs the declared variable name "VERSION"
			if includeWIPs:
				filterWIP = None 
				try:
					filterWIPURL = str(update.WIP_URL)
					# Grabs the declared variable name "WIP_URL"
					filterWIP = str(update.WIP)
					# Grabs the declared variable name "WIP"
				except:
					pass
				if filterWIP == "True" or includeWIPs:
					filterUpdateURL = filterWIPURL
			site = urllib2.urlopen(filterUpdateURL)
			# Opens up a site connection the the filter's update page or WIP update page
			response = site.read()
			# Converts the page into a string
			jsonRaw = json.loads(response)
			# Loads the page string into JSON format
			if str(filterVersion) != str(jsonRaw["Version"]):
				print "Should be updated"
				# Checks to make sure the two versions don't match
				urllib.urlretrieve(jsonRaw["Download-URL"], "filters/updates/" + jsonRaw["Name"])
				# Downloads the new filter to a file name determined by the update site (Used if the author like to version in the file name also)
				print '%s: Updated "%s" from version %s to version %s' % (METHOD, jsonRaw["Name"], update.VERSION, str(jsonRaw["Version"]))
				if changeLog:
					# If the user wants to open the Change Log and the author has included one
					if "ChangeLog" in jsonRaw:
						log = str(jsonRaw["ChangeLog"])
						webbrowser.open_new_tab(log)
						# Opens a new tab in the default webbrowser
					else:
						print '%s: Filter "%s" did not have a Change Log' % (METHOD, jsonRaw["Name"])
			else:
				print '%s: %s\'s version matched update the site\'s version' % (METHOD, jsonRaw["Name"])
		except:
			print "Exception Occurred"
			continue
		
	files = glob.glob("filters/updates/*.py")
	# Finds all .py like before, but in the "updates" subfolder
	for f in files:
		shutil.copy(f, filterDir)
		# Copies all the new filters from the "updates" folder to the parent("filters") folder
	time.sleep(2)
	# I want to wait just in case the disk is a little slow
	shutil.rmtree(filterDir + "/updates")
	# Removes the directory tree of the "updates" folder
