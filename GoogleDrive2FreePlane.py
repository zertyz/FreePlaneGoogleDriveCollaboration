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
contents = r.read()
#print(contents)
##with open(outfile, 'wb') as f:
##        shutil.copyfileobj(r, f)

import re
#m=re.search(b"<li [^>]*>([^<]*)", contents)
#print("SEARCH:")
#print(m)
m=re.findall(b"<li [^>]*>([^<]*)|(</li>)", contents)
print("FINDALL:")
#print(m)

isFirst = True
ident=0
for entry in m:
    isClosing = (entry[1] == b'</li>')
    if (isClosing):
        print(entry[1])
        ident-=1
    else:
        if (entry[0] != b''):
            isFirst = False
        if (~isFirst):
            print(str(ident)+":"+str(entry[0]))
            ident+=1