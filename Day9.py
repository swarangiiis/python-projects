#Q1
age=int(input("Enter your Age:"))
if age>=18:
    print(' You are old enough to drive')
else:
    n=18-age
    print('you need',n,'more years to drive')

#Q2
my_age=18
your_age=int(input("Enter your Age:"))

if your_age>my_age:
    a=your_age-my_age
    if a==1:
         print('you are 1 year older than me')
    else:
          print('you are',a,'years older than me ')
elif your_age<my_age:
    b=my_age-your_age
    if b==1:
              print('you are 1 year younger than me')
    else:
             print('you are',b,'years younger than me ')
else:
    print("we both are of same age")


#Q3
a=int(input("enter a:"))
b=int(input("enter b:"))

if a>b:
      print('a is greater than b')

elif b>a:
       print('b is greater than a')

else:
      print('both are equal')


#LEVEL 2

#Q1

marks=int(input('Enter the marks of student'))
if marks>=90 and marks<100:
      print('student secured grade A')
elif marks>=80 and marks<90:
      print('student secured grade B')
elif marks>=70 and marks<80:
      print('student secured grade C')
elif marks>=60 and marks<70:
      print('student secured grade D')
elif marks>=0 and marks<60:
      print('student secured grade F')


#Q2

Autumn = ['September', 'October', 'November']
Winter= ['December', 'January' , 'February']
Spring= ['March', 'April',' May']
Summer=['June', 'July','August']
month=input('enter the month:')

if  month in Autumn:
      print(" the month is of autumn")
elif month in Winter:
      print(" the month is of winter")
elif month in Spring:
      print(" the month is of spring")
elif month in Summer:
      print(" the month is of summer")
else:
      print('error')

#Q3
fruit=input('Enter the fruit :')
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits:
      print('That fruit already exist in the list')
else:
      fruits.append(fruit)
      print(fruits)


#LEVEL 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print('skills' in person)
print(person['skills'][2])

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print('skills'in person)

if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill")
    else:
        print("The person does not have Python skill")

#
if 'skills' in person:
      if 'Javascript'and 'React' in person['skills']:
            print('He is a frontend developer')
      if ['Node','Python', 'MongoDB'] in person['skills']:
            print('He is a backend developer')
      if ['React' ,'Node' ,'MongoDB'] in person['skills']:
            print('He is a fullstack developer')
else:
      print('unknown title')

