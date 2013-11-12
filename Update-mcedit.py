import httplib
import zipfile
import urllib
import os

typer = {
    "Stable": 1,
    "Development": 2,
    }

oss = {
    "Windows": 1,
    "MacOSX": 2,
    }

bit = {
    "32-Bit": 1,
    "64-Bit": 2,
    }

inputs = (
    ("Version Type", tuple(sorted(typer.keys()))),
    ("Operating System", tuple(sorted(oss.keys()))),
    ("The option below is only needed for Windows","label"),
    ("Processor Type", tuple(sorted(bit.keys()))),
    )

def unzip(the_zipfile, the_path):
    with zipfile.ZipFile(the_zipfile, "r") as z:
        z.extractall(the_path)
        
def perform(level, box, options):
    version = options["Version Type"]
    the_os = options["Operating System"]
    the_bit = options["Processor Type"]
    dev_url_file = "http://dl.dropboxusercontent.com/s/uqyglkcjg3wmsk8/urls.txt"
    urllib.urlretrieve(dev_url_file, "urls.txt")
    lines = [line.rstrip('\n') for line in open('urls.txt')]
    print lines
    mce_path1 = str(os.getcwd())
    os.chdir('..')
    mce_path2 = str(os.getcwd())
    print mce_path2
    if version == "Stable":
        if the_os == "Windows":
            if the_bit == "32-Bit":
                name = "MCEdit-0.1.7.1.win32.zip"
                url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.win32.zip"
                new_mcedit = urllib.urlretrieve(url, "MCEdit-0.1.7.1.win32.zip")
                unzip(name, mce_path1)
                raise Exception("Downloaded the " + version + " MCEdit build for " + the_os)
            if the_bit == "64-Bit":
                name = "MCEdit-0.1.7.1.win-amd64.zip"
                url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.win-amd64.zip"
                new_mcedit = urllib.urlretrieve(url, "MCEdit-0.1.7.1.win-amd64.zip")
                unzip(name, mce_path1)
                raise Exception("Downloaded the " + version + " MCEdit build for " + the_os)
        if the_os == "MacOSX":
            name = "MCEdit-0.1.7.1.macosx-10_6-x86_64.zip"
            url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.macosx-10_6-x86_64.zip"
            new_mcedit = urllib.urlretrieve(url, "MCEdit-0.1.7.1.macosx-10_6-x86_64.zip")
            unzip(name, mce_path1)
            raise Exception("Downloaded the " + version + " MCEdit build for " + the_os)
            
    if version == "Development":
        if the_os == "Windows":
            if the_bit == "32-Bit":
                url = lines.pop(0)
                name = lines.pop(1)
                new_mcedit = urllib.urlretrieve(url, name)
                unzip(name, mce_path1)
                raise Exception("Downloaded the " + version + " MCEdit build for " + the_os)
            if the_bit == "64-Bit":
                url = lines.pop(2)
                name = lines.pop(3)
                new_mcedit = urllib.urlretrieve(url, name)
                unzip(name, mce_path1)
                raise Exception("Downloaded the " + version + " MCEdit build for " + the_os)
        if the_os == "MacOSX":
            url = lines.pop(4)
            name = lines.pop(5)
            new_mcedit = urllib.urlretrieve(url, name)
            unzip(name, mce_path1)
            raise Exception("Downloaded the " + version + " MCEdit build for " + the_os) 
            
            
