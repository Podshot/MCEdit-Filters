# Update Filters by Podshot
# This updates all filters that declare an UPDATE_URL and VERSION
import glob, urllib2, urllib, json, os, webbrowser

displayName = "Update Filters"
METHOD = "[Update Filters]"

inputs = (
    ("Remove Old Filters?", True),
    ("View Change Logs", False),
    )

def perform(level, box, options):
    doRemove = options["Remove Old Filters?"]
    changeLog = options["View Change Logs"]
    filters = glob.glob("*.py")
    # Search the "filters" folder for all files that have an extension of ".py"
    for filt in filters:
        try:
            fileName = filt.split(".")
            # __import__() does not like file extensions, so I remove the .py extension from the file name
            name = fileName[0]
            py = __import__(name)
            # I use __import__() to import a filter from a string
            filterUpdateURL = str(py.UPDATE_URL)
            # Grabs the declared variable name "UPDATE_URL"
            filterVersion = str(py.VERSION)
            # Grabs the declared variable name "VERSION"
            site = urllib2.urlopen(filterUpdateURL)
            # Opens up a site connection the the filter's update page
            response = site.read()
            # Converts the page into a string
            jsonRaw = json.loads(response)
            # Loads the page string into JSON format
            if filterVersion != str(jsonRaw["Version"]):
                # Checks to make sure the two versions don't match
                urllib.urlretrieve(str(jsonRaw["Download-URL"]), str(jsonRaw["Name"]))
                # Downloads the new filter to a file name determined by the update site (Used if the author like to version in the file name also)
                print '%s: Updated "%s" from version %s to version %s' % (METHOD, py.displayName, py.VERSION, str(jsonRaw["Version"]))
                if doRemove:
                    # Removes the old filter if the user wants to
                    os.remove(filt)
                if changeLog:
                    # If the user wants to open the Change Log and the author has included one
                    if "ChangeLog" in jsonRaw:
                        log = str(jsonRaw["ChangeLog"])
                        webbrowser.open_new_tab(log)
                        # Opens a new tab in the default webbrowser
                    else:
                        print '%s: Filter "%s" did not have a Change Log' % (METHOD, py.displayName)
            else:
                print '%s: %s\'s version matched update the site\'s version' % (METHOD, py.displayName)
        except:
            pass
