import json
import urllib.parse
import urllib.request

basepath = 'http://api.openweathermap.org/data/2.5/weather?'

while True:
    params = dict()
    print()
    print('Lets find the weather... Type x to go back home')

    city = input('Enter city eg.(Brampton):')
    if len(city) < 1:
        print('OK - lets try with zip code...')
        zipcode = input('Enter zip,country eg.(94040,us): ')
        if len(zipcode) < 1:
            continue
        else:
            if zipcode == 'x':
                break
            params['zip'] = zipcode
    else:
        if city == 'x':
            break
        params['q'] = city

    appId = input('Enter key: ')
    if len(appId) < 1:
        continue
    else:
        if appId == 'x':
            break
        params['appid'] = appId

    url = basepath + urllib.parse.urlencode(params)
    print('Retrieving', url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'chars')

    try:
        js = json.loads(data)
    except:
        js = None

    print(js['cod'])
    if not js or 'cod' not in js or js['cod'] != 200:
        print('=== Failed to retrieve ===')
        continue

    print(js['name'], '[', js['coord']['lon'], ',', js['coord']['lat'], ']')
