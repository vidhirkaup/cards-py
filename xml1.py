import xml.etree.ElementTree as ET

data = '''
    <person>
        <name>chuck</name>
        <phone type="home">
            +1 905 123 1234
        </phone>
        <email hide="yes"/>
    </person>'''

tree = ET.fromstringlist(data)
print('Name:', tree.find('name').text)
print('Attr: hide=', tree.find('email').get('hide'))

users = '''
    <dir>
        <users>
            <user id="101">
                <name>Adam</name>
                <phone type="home">
                    +1 201-123-1234
                </phone>
            </user>
            <user id="102">
                <name>Betty</name>
                <phone type="home">
                    +1 905-999-6789
                </phone>
            </user>
        </users>
    </dir>
'''

dir = ET.fromstring(users)
userList = dir.findall('users/user')
print('count(users): ', len(userList))

print()

for user in userList:
    print('user.id: ', user.get('id'))
    print('user.name: ', user.find('name').text)

    print('user.phone.type: ', user.find('phone').get('type'))
    print('user.phone: ', user.find('phone').text.strip())
    print()
