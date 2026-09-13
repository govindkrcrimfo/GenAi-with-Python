import json

#json file read and write

with open ('students.json','r') as file:   
    user_data=json.load(file)

print(user_data)

user_data['students'][0]['name']="Govind"
print(user_data)

# Write updated data back to JSON file
with open('students.json','w') as file:
    json.dump(user_data,file,indent=2)
print(user_data)
