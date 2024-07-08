users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
          "street": "Kulas Light",
          "suite": "Apt. 556",
          "city": "Gwenborough",
          "zipcode": "92998-3874",
          "geo": {
                "lat": "-37.3159",
                "lng": "81.1496",
                }
    }
}

print(users)
print(users["id"],users["name"])
print(users["address"]["street"])
print(users["address"]["geo"]["lat"])

print(type(users))
import json
result = json.dumps(users)
print(result)
print(type(result))

with open('result.json','w') as file:
    json.dump(users,file)