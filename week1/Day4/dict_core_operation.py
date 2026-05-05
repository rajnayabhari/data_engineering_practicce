student={"name":"raj","age":22,"course":"python"}

# to print the value of key
print(student["name"])

# to add or update key value pair
student["score"]=90 #this adds a new key value pair to dict
student["age"]=23 #this updates the value of existing key

del student["course"] #this deletes the key value pair from dict

if "score" in student:
    print("there is score in dict")
#this check if there is key or not

for key,value in student.items():
    print(key,value)
#this is to print all key value pair in dict



# useful dict methods
d = {"name": "Raj", "score": 92}
d.keys() #this returns all the keys in dict
d.values() #this returns all the values in dict
d.items() #this returns all the key value pair in dict as tuple
print(d.get("grade","N/A")) #this returns the value of key if exist otherwise it returns default value