#Q1
list=[]

#Q2
business_term=['mvp','cap table','churn','acquisition','bootstrap']

#Q3
print(len(business_term))

#Q4
print(business_term[0::2])

#Q5
mixed_data_types=['swarangi deshmukh',18,'156cm','unmarried','shivarpan colony']

#Q6
it_companies=['facebook','google','microsoft','apple','IBM','oracle','Amazon']

#Q7
print(it_companies)

#Q8
print(len(it_companies))

#Q9
print(it_companies[0::3])

#Q10
it_companies[-2]='Nvidia'
print(it_companies)

#Q11
it_companies.append('YC')
print(it_companies)

#Q12
it_companies.insert(4,'meta')
print(it_companies)

#Q13
it_companies[1] = it_companies[1].upper()
print(it_companies)


it_companies[-8]='Google'
print(it_companies)

#Q14
print('#;  '.join(it_companies))

#Q15
print('anthropic'in it_companies)

#Q16
it_companies.sort()
print(it_companies)

#Q17
it_companies.sort(reverse=True)
print(it_companies)

it_companies1 = it_companies.copy()
print(it_companies1)

#Q18
del it_companies[0:3]
print(it_companies)

#Q19
del it_companies[-3:]
print(it_companies)

#Q20
print(it_companies1.pop(4))

#Q21
it_companies1.remove('microsoft')
print(it_companies1)

#Q23
it_companies1.remove('Amazon')
print(it_companies1)

#Q24
it_companies.clear()
print(it_companies)

it_companies1.clear()
print(it_companies1)

#25
del it_companies
del it_companies1

#Q26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
web_dev= front_end + back_end
print(web_dev)

#Q27
full_stack= web_dev.copy()
full_stack.insert(5,'python')
full_stack.insert(6,'SQL')
print(full_stack)

#LEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

print('min age:',ages[0])
print('max age:',ages[9])

ages.append(min(ages))
ages.append(max(ages))
print(ages)



print('avg:', sum(ages)/len(ages))

print('range:',max(ages)-min(ages))

#countries

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

middle_country= len(countries)//2

print(countries[middle_country])

print(len(countries))

first_half= countries[:98]
print(first_half)

second_half= countries[98:]
print(second_half)


lst=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a,b,c,*scandic= lst 
print(a)
print(b)
print(c)
print(scandic)
