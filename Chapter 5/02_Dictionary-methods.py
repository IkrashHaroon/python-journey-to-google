employee = {
    "id": 101,
    "name": "Ali",
    "age": 32,
    "department": "IT",
    "skills": ["Python", "JavaScript", "SQL"],
    }

# dictionary methods

# employee.items()    Returns a view object that displays a list of a dictionary's key-value tuple pairs

# print(employee.items()) 
# employee.keys()     Returns a view object that displays a list of all the keys in the dictionary

# print(employee.keys())   

#employee.values()   Returns a view object that displays a list of all the values in the dictionary

# print(employee.items())

# employee.upadtes()  # Updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs
# employee.update({"age": 30, "location": "Pakistan"}) # Dictionary is mutable, so we can update it. 
# So the dictionary which I have passed in that the key value pair which are there in my marks they will be updated like Age 32 
# so it will be updated and the ones which are not there will be added like location Pakistan means the dictionary will be updated according to this the key value pair which are there will be updated
# it is Simple 😁
# print(employee)

# employee.get()     # Returns the value of the specified key if key is in dictionary. If not, returns default value None
print(employee.get("name")) # same as employee["name"]
print(employee["name"]) #same as employee.get("name")
# But as soon as I write this in this way 👇
print(employee.get("Location")) # it  will return None because there is no key called Location in the dictionary employee
print(employee["Location"]) # it will give an error because there is no key called Location in the dictionary employee
# So the difference is that if I use get method it will return None but if I use this way it will give an error
# employee.pop()      # Removes the element with the specified key
# employee.pop("age") # Removes the element with the specified key
# print(employee)

# employee.popitem()  # Removes the last inserted key-value pair
# employee.popitem() # Removes the last inserted key-value pair
# print(employee)

# 💡 📚 Now I will tell you to go the chatgpt 🤖 and go to chatgpt and ask Give me some python dictionary methods
