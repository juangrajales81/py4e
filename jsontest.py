import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

uh = urllib.request.urlopen(url)

print('Retreiving ', url)

data = uh.read().decode()

print('Retrieved: ', len(data), ' characters')

info = json.loads(data)

sum = 0
count = 0
for item in info['comments']:
    sum += int(item['count'])
    count += 1 
print('Count: ', count)
print('Sum: ', sum)
    