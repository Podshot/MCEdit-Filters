import glob, urllib2, urllib, json

displayName = "Update Filters"

def perform(level, box, options):
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
            
