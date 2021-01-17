import json

data = '''{
    "name": "chuck",
    "phone":{
        "type": "home",
        "number": "+1 905 123 1234"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Attr: hide=', info["email"]["hide"])

print()

users = '''
    [
        {
            "id": "101",
            "name": "Adam",
            "phone":{
                "type": "home",
                "number": "+1 201-123-1234"
            }
        },
        {
            "id": "102",
            "name": "Betty",
            "phone":{
                "type": "home",
                "number": "+1 905-123-6789"
            }
        }
    ]
'''

userList = json.loads(users)
print('count(users): ', len(userList))
print('----------')
for user in userList:
    print('user.id: ', user['id'])
    print('user.name: ', user['name'])

    print('user.phone.type: ', user['phone']['type'])
    print('user.phone: ', user['phone']['number'])
    print()