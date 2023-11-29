# p.96
person3 = {
    'Name': 'Ford Perfect',
    'Gender': "Male",
    'Occupation': 'Researcher',
    'Home Planet': 'Betelgeuze Seven',
}

print(person3)
print(person3['Home Planet'])
print(person3['Name'])

person3['Age'] = 33
print(person3)

# p.104
# Shell stuff


# p.136
people = {}
people['Ford'] = {
    'Name': 'Ford Perfect',
    'Gender': "Male",
    'Occupation': "Researcher",
    'Home Planet': "Betelgeuze Seven",
}

print()
print(people)

people["Arthur"] = {
    'Name': 'Arthur Dent',
    'Gender': 'Male',
    'Occupation': 'Sandwich-Maker',
    'Home Planet': 'Earth',
}
people["Trillian"] = {
    'Name': 'Tricia McMillian',
    'Gender': 'Female',
    'Occupation': 'Mathematician',
    'Home Planet': 'Earth',
}
people["Robot"] = {
    'Name': 'Marvin',
    'Gender': 'Unknown',
    'Occupation': 'Paranoid Android',
    'Home Planet': 'Unknown',
}

print(people)

# Pretty-printing, p.139
import pprint

pprint.pprint(people)
