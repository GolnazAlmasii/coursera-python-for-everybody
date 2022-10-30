import urllib.request, urllib.parse, urllib.error
import urllib
from urllib.request import urlopen
print(urllib)
import requests as requests
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter  ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = input('enter count: ')
count = int(count)
position = input('enter position: ')
position = int(position)
tags = soup('a')
# Retrieve all of the anchor tags
poscount = 0
timecount = 0
while count > timecount:
    timecount = timecount + 1
    print('TAG:', tags[position])
    print('URL:', tags[position].get('href', None))
    print('Contents:', tags[position].contents[0])
    print('Attrs:', tags[position].attrs)
    pos = (tags[position])
    url = pos.get('href', None)
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #print('counting', timecount, count)