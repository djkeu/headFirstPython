# Sharpen your pencil, p.67

phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

# Add list manipulation code here
letters_to_keep = "on tap"
found = []

for letter in phrase:
    if letter in letters_to_keep:
        if letter not in found:
            found.append(letter)
plist = found

plist.insert(2, plist.pop(3))
plist.insert(-1, plist.pop())

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


# Sharpen your pencil, p.81
print("\nSharpen your pencil, p.81")

phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

# Begin code to change
"""
for i in range(4):
    plist.pop()
    print(plist)
plist.pop(0)
plist.remove("'")


plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
"""
# End code to change

new_phrase = plist[1:-4]
new_phrase.remove(new_phrase[2])
new_phrase.insert(2, new_phrase.pop(3))
new_phrase.insert(-1, new_phrase.pop(-1))

print(plist)
print(new_phrase)
