import re
import json

data = [
    {"name": "john doe", "email": "JOHN@example.com", "phone_number": "123-456-7890", "address": "123 Main St, New York, NY 10001"},
    {"name": "jane smith", "email": "Jane.Smith@Email.com", "phone_number": "(123) 456 7890", "address": "456 Elm St, Los Angeles, CA 90001"},
    {"name": "john doe", "email": "john@example.com", "phone_number": "1234567890", "address": "123 Main St, New York, NY 10001"},
    {"name": "john cena","email": "johncena@gmail.com","phone_number":"1238459332","address": "221 New jersey,Newyork,NY 10023"},
    {"name": "rom cena","email": "ROMCENA@gmail.com","phone_number":"1276459332","address": "211 london,england,EG 10023"},
    {"name": "john cena","email": "johncena@gmail.com","phone_number":"1238459332","address": "221 New jersey,Newyork,NY 10023"},
    {"name": "randy ortan","email": "randyortan@gmail.com","phone_number":"5342159332","address": "321 Colombia,Newyork,NY 10323"},
    {"name": "seth rollins","email": "seth rollins@gmail.com","phone_number":"1238457232","address": "322 New jersey,Newyork,NY 10023"},
    {"name": "mett henry","email": "metthenry@gmail.com","phone_number":"1238999332","address": "111 main st,Newyork,NY 10223"},
    {"name": "jeff hardy","email": "jeffhardy@gmail.com","phone_number":"1238454442","address": "221 colm,clombia,CL 11023"},
]

with open('cleaned.json', 'w') as f:
    json.dump(data, f)
    

format_data = list({frozenset(i.items()) for i in data})
format_data = [dict(i) for i in format_data]

def clean_phone_number(phone):
    if len(phone) == 10:
        return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    return phone 

for i in format_data:
    i['phone_number'] = clean_phone_number(i['phone_number'])

for i in format_data:
    i['email'] = i['email'].lower()

for i in format_data:
    i['name'] = i['name'].title()

for i in format_data:
    add = i['address'].split(',')
    street = add[0].strip()
    city = add[1].strip()
    state_zip = add[2].strip().split(' ')
    state = state_zip[0]
    zip_code = state_zip[1]
    
    i['address'] = [street, city, state, zip_code]

for i in format_data:
    state_zip = add[2].strip().split(' ')
    state_abbreviation = state_zip[0]
    zip_code = state_zip[1]
    i['state_abbreviation'] = state_abbreviation

# Dump cleaned data into a new JSON file
with open('cleaned_data.json', 'w') as f:
    json.dump(format_data, f)

print("new json task saved in cleaned_data.json")


