# Found vowels
found = []
print(len(found))

found.append('a')
print(len(found))
print(found)

found.append('e')
found.append('i')
found.append('o')
print(len(found))
print(found)

if 'u' not in found:
    found.append('u')
print(found)


# List slices in action
print("\nLetters:")
phrase = "Don't panic!"
letters = list(phrase)

print(letters)
print(letters[0:10:3])
print(letters[3:])
print(letters[:10])
print(letters[::2])

