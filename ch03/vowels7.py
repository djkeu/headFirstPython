# vowels = {'a', 'e', 'i', 'o', 'u'}
vowels = set('aeoiu')
word = input("Noem eens woord of een zin, dat zeg ik welke klinkers er in zitten: ")

found_vowels = vowels.intersection(set(word))

for vowel in found_vowels:
    print(vowel)
