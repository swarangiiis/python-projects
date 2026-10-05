#Q1

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero=[i for i in numbers if i<=0]
print(negative_zero)

#Q2

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list=[number for row in list_of_lists for number in row]
print(flattened_list)

#Q4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output=[[country.upper(),country[:3].upper(),capital.upper()] for item in countries for country,capital in item]
print(output)

#Q5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output=[{"country": country.upper(),'capital': capital.upper(),}
        for item in countries 
        for country,capital in item ]
print(output)


#Q6

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output=[name + " "+last_name
        for i in names  
        for name,last_name in i ]
print(output)

#Q7
#Slope
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print('Slope=',slope(5,4,2,1))

#Y-intercept

y_intercept = lambda x, y, m: y - m * x
print("y intercept=",y_intercept(2,4,8))