import urllib.request, urllib.parse, urllib.error
import json

basepath = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = basepath + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'chars')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failed to retrieve ===')
        print(data)
        continue


