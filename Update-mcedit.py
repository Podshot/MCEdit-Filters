import httplib
import zipfile
import urllib
import os
from sys import platform as _platform
import subprocess
import time

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
    ("Cleanup", False),
    ("The option below is only needed for Windows","label"),
    ("Processor Type", tuple(sorted(bit.keys()))),
    ("Use cleanup after you have run the filter ONCE","label"),
    )

def createrestart(operation, path):
    contents = [""]
    if operation == "OS X":
        raise Exception("Not Completed")
    if operation == "Windows":
        contents.append("@ECHO OFF\n")
        contents.append("taskkill /f /im mcedit.exe\n")
        contents.append("timeout /t 10 /nobreak >nul\n")
        contents.append("xcopy " + '"' + str(path) + "\\temp" + '"' + " " + '"' + str(path) + '"' + " /E /V /Y\n")
        contents.append("start mcedit.exe\n")
        contents.append("EXIT\n")
        with open(str(path) + "/" + "restart.bat", "w") as f:
            f.writelines(contents)
        

def unzip(the_zipfile, the_path):
    with zipfile.ZipFile(the_zipfile, "r") as z:
        z.extractall(the_path + "\\temp")
        os.chdir(the_path)
        os.system("restart.bat")
        time.sleep(2.5)
        raise SystemExit()
                        
        
def perform(level, box, options):
    cleanup = options["Cleanup"]
    if not cleanup:
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
        try:
            os.mkdir("temp")
        except OSError:
            pass
        if _platform == "darwin":
            createrestart("OS X", str(mce_path2))
        if _platform == "win32":
            createrestart("Windows", str(mce_path2))
            
        if version == "Stable":
            if the_os == "Windows":
                if the_bit == "32-Bit":
                    name = "MCEdit-0.1.7.1.win32.zip"
                    url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.win32.zip"
                    urllib.urlretrieve(url, "MCEdit-0.1.7.1.win32.zip")
                    unzip(name, mce_path2)
                if the_bit == "64-Bit":
                    name = "MCEdit-0.1.7.1.win-amd64.zip"
                    url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.win-amd64.zip"
                    urllib.urlretrieve(url, "MCEdit-0.1.7.1.win-amd64.zip")
                    unzip(name, mce_path2)
            if the_os == "MacOSX":
                name = "MCEdit-0.1.7.1.macosx-10_6-x86_64.zip"
                url = "https://bitbucket.org/codewarrior0/mcedit/downloads/MCEdit-0.1.7.1.macosx-10_6-x86_64.zip"
                urllib.urlretrieve(url, "MCEdit-0.1.7.1.macosx-10_6-x86_64.zip")
                unzip(name, mce_path2)
            
        if version == "Development":
            if the_os == "Windows":
                if the_bit == "32-Bit":
                    url = lines.pop(0)
                    name = lines.pop(0)
                    urllib.urlretrieve(str(url))
                    unzip(name, mce_path2)
                if the_bit == "64-Bit":
                    url = lines.pop(2)
                    name = lines.pop(2)
                    print 'URL: %s' % (url)
                    print 'Name: %s' % (name)
                    urllib.urlretrieve(url, name)
                    unzip(name, mce_path2)
            if the_os == "MacOSX":
                url = lines.pop(4)
                name = lines.pop(4)
                urllib.urlretrieve(str(url), str(name))
                unzip(name, mce_path2)
    
    if cleanup:
        return
