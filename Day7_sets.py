# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia','Meta','Goldman sachs'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Meta')
print(it_companies)

# What is the difference between remove and discard
it_companies.discard('hyrox')
print(it_companies)

"""it_companies.remove('hyrox')
print(it_companies)"""


#Level 2

#Join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))
print(A.union(B),B.union(A))

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))


#Delete the sets completely
del A
del B


# LEVEL 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age1=age.copy()
age=set(age)
print(age)
print(len(age1))
print(len(age))
print(len(age1)>len(age))


#or

if len(age)>len(age1):
    print("The set is bigger")

elif len(age1)>len(age):
    print("The list is bigger")

else:
    print('Both are equal')


sentence='I am a teacher and I love to inspire and teach people.'
lst=sentence.split()
print('len list',len(lst))
set1=set(sentence.split())
print('len set',len(set1))
print(set1)
