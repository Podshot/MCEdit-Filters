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
    try:
        os.mkdir(filterDir + "/updates")
    except OSError:
        pass
    filters = glob.glob("filters/*.py")
    # Search the "filters" folder for all files that have an extension of ".py"
    for filt in filters:
        filterUpdateURL = None
        try:
            # __import__() does not like file extensions, so I remove the .py extension from the file name
            pyfile = str(filt[8:])
            newName = pyfile.split(".")
            name = str(newName[0])
            py = __import__(name)
            # I use __import__() to import a filter from a string
            filterUpdateURL = str(py.UPDATE_URL)
            # Grabs the declared variable name "UPDATE_URL"                
            filterVersion = str(py.VERSION)
            # Grabs the declared variable name "VERSION"
            if includeWIPs:
                filterWIP = None 
                try:
                    filterWIPURL = str(py.WIP_URL)
                    # Grabs the declared variable name "WIP_URL"
                    filterWIP = str(py.WIP)
                    # Grabs the declared variable name "WIP"
                except:
                    pass
                try:
                    if filterWIP == "True" or includeWIPs:
                        filterUpdateURL = filterWIPURL
                except:
                    pass
            site = urllib2.urlopen(filterUpdateURL)
            # Opens up a site connection the the filter's update page or WIP update page
            response = site.read()
            # Converts the page into a string
            jsonRaw = json.loads(response)
            # Loads the page string into JSON format
            if filterVersion != jsonRaw["Version"]:
                # Checks to make sure the two versions don't match
                urllib.urlretrieve(jsonRaw["Download-URL"], filterDir + "/updates/" + jsonRaw["Name"])
                # Downloads the new filter to a file name determined by the update site (Used if the author like to version in the file name also)
                print '%s: Updated "%s" from version %s to version %s' % (METHOD, jsonRaw["Name"], py.VERSION, str(jsonRaw["Version"]))
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
                        print '%s: Filter "%s" did not have a Change Log' % (METHOD, jsonRaw["Name"])
            else:
                print '%s: %s\'s version matched update the site\'s version' % (METHOD, jsonRaw["Name"])
        except:
            pass
        
    files = glob.glob(filterDir + "/updates/*.py")
    for f in files:
        shutil.copy(f, filterDir)
    time.sleep(2)
    
    shutil.rmtree(filterDir + "/updates")
