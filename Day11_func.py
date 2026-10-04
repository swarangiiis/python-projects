#Q1
def add_two_numbers(a,b):
    total=a+b
    print("Sum:",total)
    return total
add_two_numbers(4,8)
add_two_numbers(5,3)

#Q2
def area_of_circle(r):
    pie=3.14
    A=pie*r*r
    print("Area of circle:",A)
    return A
area_of_circle(2)

#Q3
def add_all_nums(*nums):
    total=0
    for i in nums:
        total+=i
    print(total)
    return total
add_all_nums(4,8,2)    


#Q4
def convert_celsius_to_fahrenheit(C):
    F =(C * 9/5) + 32
    print(f"The Temperature is {F} Fahrenheit")
    return F
convert_celsius_to_fahrenheit(0)
convert_celsius_to_fahrenheit(32)

#Q5
def check_season(month):
    return month
print('The season:' , check_season('summer'))

#Q6
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

print("The slope :",calculate_slope(5,4,3,6))

#Q7
import math

def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c

    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)

    return x1, x2

print(solve_quadratic_eqn(1, -5, 6))

#Q8
def print_list(lst):
    for i in lst:
        print(i)
print(print_list(['apple','orange','kiwi']))


#Q9
def reverse_list(array):
    for i in range(len(array),-1,-1):
        print(i,end=" ")
    print() 
reverse_list([1,2,3,4])

#Q10
def capitalize_list_items(name):
    print(name.capitalize())
capitalize_list_items('swarangi')

#Q11
def add_item(list,item):
    list.append(item)
    return list


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff,'Thukpa'))
numbers = [2, 3, 7, 9]
print(add_item(numbers,8))

#Q12
def remove_item(list,item):
    list.remove(item)
    return list 
print(remove_item(food_stuff,'Tomato'))

#Q13
def sum_of_numbers(range_count):
    sum=0
    for i in range(range_count+1):
        sum+=i
    return sum 
print(sum_of_numbers(3))
print(sum_of_numbers(10))

#Q14
def sum_of_odds(range_count):
    sum=0
    for i in range(range_count+1):
        if i%2!=0:
            sum+=i
    return sum 
print(sum_of_odds(100))

#Q15
def sum_of_even(range_count):
    sum=0
    for i in range(range_count+1):
        if i%2==0:
            sum+=i
    return sum 
print(sum_of_even(100))

#LEVEL 2


#Q
def sum_evens_and_odds(range_count):

    sum1 = 0
    sum2 = 0

    for i in range(range_count + 1):

        if i % 2 == 0:
            sum1 += i
        else:
            sum2 += i

    return sum1, sum2
even_sum, odd_sum = sum_evens_and_odds(50)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Q1
def evens_and_odds(range_count):

    count1 = 0
    count2 = 0

    for i in range(range_count + 1):

        if i % 2 == 0:
            count1 += 1
        else:
            count2 += 1

    return count1, count2
even_count, odd_count = evens_and_odds(100)
print("No of even numbers:", even_count)
print("No of odd numbers:", odd_count)

#Q2
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print("The factorial of 3:",factorial(3))
print(f"The factorial of 5:",factorial(5))
print("The factorial of 4:",factorial(4))

#Q3
def is_empty(parameter):
    if parameter=="":
        return True
    else:
        return False
    
print(is_empty("swarangi"))
print(is_empty(""))

#Q4
def greet(name='guest'):
    message=f'Hello,{name}!'
    return message
print(greet())
print(greet("swarangi"))

#Q5
def show_args(**args):
    for i,j in args.items():
        print(i,j)
    return i
show_args(name="Alice", age=30, city="New York")

#Level 3

# 1. Check if a number is prime

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(8))


# 2. Check if all items are unique

def all_unique(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False

    return True


print(all_unique([1, 2, 3, 4]))
print(all_unique([1, 2, 2, 4]))


# 3. Check if all items have the same data type

def same_data_type(lst):
    for i in lst:
        if type(i) != type(lst[0]):
            return False

    return True


print(same_data_type([1, 2, 3, 4]))
print(same_data_type([1, 2, "3", 4]))


# 4. Check if a variable name is valid

def is_valid_variable(variable):
    return variable.isidentifier()


print(is_valid_variable("name"))
print(is_valid_variable("123name"))
print(is_valid_variable("my_name"))