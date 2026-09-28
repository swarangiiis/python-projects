# level 1

#Q1
t= tuple()

#Q2
cousins1=('sarvesh','srujana','swarangi','agraja','anavaya','shoumik')

#Q3
sisters=('srujana','swarangi','agraja','anvaya')
brothers=('shoumik','sarvesh')
cousins=sisters + brothers
print(cousins)

#Q4
print(len(cousins))

#Q5
cousins1=list(cousins1)
cousins1.append('Deepak')
cousins1.append('Prayukta')
family_members=cousins1.copy()
family_members=tuple(family_members)
print(family_members)

#level 2

#Q1
a,b,c,d,e,f,*family_members= family_members
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(family_members)

#Q2
fruits=('apple','banana','kiwi','mango',)
vegetables=('carrot','ladyfinger','potato','brinjal')
animal_products=('milk','meat','beef')
food_stuff_tp= fruits+vegetables+animal_products
print(food_stuff_tp)

#Q3
food_stuff_tp=list(food_stuff_tp)
food_stuff_lt=food_stuff_tp
print(food_stuff_lt)

#Q4
middle=len(food_stuff_lt)//2
print(food_stuff_lt[middle])

#Q5
print(food_stuff_lt[0:4])
print(food_stuff_tp[-3:])

#Q6
del food_stuff_tp

#Q7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
