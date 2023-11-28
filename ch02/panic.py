# Sharpen your pencil, p.67

phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

# Add list manipulation code here
plist.remove("'")  # alt: plist.pop(3)
plist.pop(0)

for i in range(4):
    plist.pop()
    print(plist)

plist.extend(plist.pop(-2))
print(plist)
plist.insert(2, plist.pop(3))
print(plist)
print()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
