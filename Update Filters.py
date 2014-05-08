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
    for filt in filters:
        try:
            fileName = filt.split(".")
            name = fileName[0]
            py = __import__(name)
            filterUpdateURL = str(py.UPDATE_URL)
            filterVersion = str(py.VERSION)
            site = urllib2.urlopen(filterUpdateURL)
            response = site.read()
            jsonRaw = json.loads(response)
            if filterVersion != str(jsonRaw["Version"]):
                urllib.urlretrieve(str(jsonRaw["Download-URL"]), str(jsonRaw["Name"]))
                print '%s: Updated "%s" from version %s to version %s' % (METHOD, py.displayName, py.VERSION, str(jsonRaw["Version"]))
                if doRemove:
                    os.remove(filt)
                if changeLog:
                    log = str(jsonRaw["ChangeLog"])
                    webbrowser.open_new_tab(log)
            else:
                print '%s: %s\'s version matched update the site\'s version' % (METHOD, py.displayName)
        except:
                pass
