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

new_phrase = ''.join(plist[1:3])
new_phrase += ''.join([plist[5], plist[4], plist[-5], plist[-6]])

print(plist)
print(new_phrase)
