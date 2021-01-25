import json
import sqlite3
import urllib.parse
import urllib.request

conn = sqlite3.connect('weather.sqlite')
cur = conn.cursor()

load_city = input('Reload cities? [Y/N]: ')
if load_city == 'Y':
    cur.executescript('''
        DROP TABLE IF EXISTS city;
    
        CREATE TABLE city (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT,
            state TEXT,
            country TEXT,
            lon REAL,
            lat REAL
        )
    ''')

    fhandle = open('city.list.json', encoding='UTF8')
    cities = json.load(fhandle)
    # print(data)
    for city in cities:
        name = city['name']
        state = city['state']
        country = city['country']
        lon = city['coord']['lon']
        lat = city['coord']['lat']
        cur.execute('INSERT OR IGNORE INTO city(name, state, country, lon, lat) values (?, ?, ?, ?, ?)',
                    (name, state, country, lon, lat))
        conn.commit()

load_weather = input('Reload weather? [Y/N]: ')
if load_weather == 'Y':
    cur.executescript('''
        DROP TABLE IF EXISTS weather;
        
        CREATE TABLE weather(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            city_id INTEGER,
            temp REAL,
            feels_like REAL,
            temp_min REAL,
            temp_max REAL,
            pressure REAL,
            humidity REAL
        )
    ''')

country_cities = input('which country do you want to see? ')
appId = input('Enter key: ')

cur.execute('SELECT * FROM city where country = ?', (country_cities,))
city_list = cur.fetchmany(2)
print(city_list)

basepath = 'http://api.openweathermap.org/data/2.5/weather?'
for city in city_list:
    params = dict()

    params['lon'] = city[4]

    params['lat'] = city[5]

    params['appid'] = appId

    url = basepath + urllib.parse.urlencode(params)
    print('Invoke: ', url)

# urlhandle = urllib.request.urlopen(url)
