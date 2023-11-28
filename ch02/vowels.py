vowels = ['a', 'e', 'i', 'o', 'u']
word = "Marc Kooij"

#1
for letter in word:
    if letter in vowels:
        print(letter)

#2
print()
found_vowels = []
word = input("Noem eens woord of een zin, dat zeg ik welke klinkers er in zitten: ")

for letter in word:
    if letter in vowels:
        if letter not in found_vowels:
            found_vowels.append(letter)

for vowel in found_vowels:
    print(vowel)
