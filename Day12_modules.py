#LEVEL 1

#Q1

import random,string

def random_user_id():
    characters=string.ascii_letters+string.digits
    user_id=""
    for i in range(6):
        user_id+=random.choice(characters)
        

    return user_id
print("The user id is:",random_user_id())

#Q2
no_char=int(input("number of characters:"))
no_ids=int(input("number of IDs:"))

def user_id_gen_by_user():

    characters=string.ascii_letters+string.digits
    user_id=""

    for i in range(no_ids):  
        user_id=""
        for j in range(no_char):
            user_id+=random.choice(characters)
        print(user_id)
user_id_gen_by_user()


#Q3

from random import randint

def rgb_color_gen():
    rgb=[]
    for i in range(3):
        rgb.append(randint(0,255))
    print(f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")

rgb_color_gen()  

#LEVEL 2

#Q2

from random import randint

def list_of_rgb_colors(number):

    colors = []

    for i in range(number):
        rgb = []

        for j in range(3):
            rgb.append(randint(0, 255))

        colors.append(rgb)

    print(colors)

list_of_rgb_colors(4)

#Q3

import random,string
from random import randint

def generate_colors(type,number):

    if type.lower()=='hexa':
        characters="0123456789abcdef"
        hexa_arr=[]

        for i in range(number):
            user_id=""
            for j in range(6):
                user_id+=random.choice(characters)
            hexa_arr.append("#"+ user_id)
        return hexa_arr
    
    elif type.lower()=='rgb':
        colors=[]

        for i in range(number):
            rgb = []
        
            for j in range(3):
                rgb.append(randint(0, 255))
        
            colors.append(f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")
        
        return colors

print(generate_colors("Hexa",3))
print(generate_colors("Rgb", 3))
print(generate_colors("Hexa",1))


#LEVEL 3

#Q1

import random

def shuffle_list(lst):
    new_list = []

    while len(lst) > 0:
        index = random.randint(0, len(lst) - 1)
        new_list.append(lst[index])
        lst.pop(index)

    return new_list

print(shuffle_list([5,6,7,8,9]))

#Q2
# WITH DUPLICATESSSSSSS

from random import randint

def arr_seven_rndm_no():
    arr=[]
    for i in range(7):
        arr.append(randint(0,9))

    return arr

print(arr_seven_rndm_no())

# WITHOUT DUPLICATESSSSSS

import random

def random_numbers():

    numbers = []

    while len(numbers) < 7:
        num = random.randint(0, 9)

        if num not in numbers:
            numbers.append(num)

    return numbers

print(random_numbers())

#ORRR

import random

def random_numbers():
    numbers = []

    while len(numbers) < 7:
        num = random.randint(0, 9)

        if num in numbers:
            continue

        numbers.append(num)

    return numbers

print(random_numbers())




            

