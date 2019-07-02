msg = "HELLO WORLD"
print(msg)
print(msg+"|"+str(1)+"|"+msg)
MSG=msg.capitalize()
print(MSG)

url="https://blog.ogrerobot.com/innovative-algo-trading-models/how-hard-is-to-do-proper-backtests-in-algorithmic-trading/backtests-draft"
outfile="out.html"
print("Downloading Google Drive's URL '"+url+"' and saving it to '"+outfile+"'")
import requests
import urllib
import shutil
r = urllib.request.urlopen(url)
bContents = r.read()
contents = bContents.decode("utf-8")
#print(contents)
##with open(outfile, 'wb') as f:
##        shutil.copyfileobj(r, f)

import re
#m=re.search("<li [^>]*>([^<]*)", contents)
#print("SEARCH:")
#print(m)
m=re.findall("<li [^>]*>([^<]*)|(</li>)", contents)
print("FINDALL:")
#print(m)

isFirst = True
ident=0
for entry in m:
    isClosing = (entry[1] == '</li>')
    if (isClosing):
        if (not isFirst):
            ident-=1
    else:
        if (entry[0] != ''):
            isFirst = False
        if (not isFirst):
            ident+=1
            print(str(ident)+":"+entry[0])

# you might want to export the map to .adoc (or .txt) and then move from there on into producing a pastable object to google drive...
# or simply use .svg, putting it on the site's resource section...