# Create an empty dictionary called dog
Dog={}

# Add name, color, breed, legs, age to the dog dictionary
Dog={
    'Name':'Nico',
    'Color':'White',
    'Breed':'Labrodog',
    'legs':'4',
    'Age':'5yrs'
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'Swarangi',
    'last_name':'Deshmukh',
    'gender':'female',
    'age':19,
    'marital_status':'unmarried',
    'skills':['next entrepreneur','curious researcher','reader'],
    'country':'India',
    'city':'Bangaluru',
    'address':'5,next avenue'
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))

# Modify the skills values by adding one or two skills
student['skills'].append('journaling')
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student['address']
print(student)

# Delete one of the dictionaries
del student
