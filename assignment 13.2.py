import json
import urllib.request, urllib.parse, urllib.error

url = input("enter url ")
fh = urllib.request.urlopen(url)
data = fh.read()
data = data.decode()
dataa = json.loads(data)
sum = 0

for num in (dataa['comments']):
    sum = sum + num['count']

print(sum)