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
    print(f"Found: {found}")
plist = found
print(f"plist: {plist}")

plist.insert(2, plist.pop(3))
plist.insert(-1, plist.pop())

print()
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
