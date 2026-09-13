import json

# Python dictionary
employee = {
    "name": "Govind",
    "age": 28,
    "skills": ["Java", "Python", "Angular"],
    "is_active": True
}

# Python dictionary → JSON string
json_emp_data=json.dumps(employee,indent=2)
print(json_emp_data)

# Json (string) to Python (dic)
dic_emp_data=json.loads(json_emp_data )
print(dic_emp_data)

#age updated 
dic_emp_data['age']=26
print(dic_emp_data)

#print date of particular key
print(dic_emp_data['name'])

# Get value safely using get()
name=dic_emp_data.get('names',"not found !!")
print(name)

