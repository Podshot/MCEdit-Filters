import glob, urllib2, urllib, json, os

displayName = "Update Filters"

inputs = (
    ("Remove Old Filters?", True),
    )

def perform(level, box, options):
    doRemove = options["Remove Old Filters?"]
    filters = glob.glob("filters/*.py")
    for filt in filters:
        py = __import__(filt)
        filterUpdateURL = str(py.UPDATE_URL)
        filterVersion = str(py.VERSION)
        site = urllib2.urlopen(filterUpdateURL)
        response = site.read()
        jsonRaw = json.loads(response)
        if filterVersion != str(jsonRaw["Version"]):
            urllib.urlretrieve(str(jsonRaw["Download-Url"]), str(jsonRaw["Name"]))
            if doRemove:
                os.remove(filt)
            
