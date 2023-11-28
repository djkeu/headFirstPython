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


# List slices in action, p.77
print("\nLetters:")
phrase = "Don't panic!"
letters = list(phrase)

print(letters)
print(letters[0:10:3])
print(letters[3:])
print(letters[:10])
print(letters[::2])


# Starting and stopping with lists, p.78
print("\nStarting and stopping with lists")
book = "The Eternal Sunshine of the Spotless Mind"
booklist = list(book)
print(booklist)

print(booklist[0:3])
print(''.join(booklist[0:3]))
print(''.join(booklist[-4:]))


# Stepping with lists, p.79
print("\nStepping with lists")
backwards = booklist[::-1]
print(''.join(backwards))

every_other = booklist[::2]
print(''.join(every_other))

# Slices
