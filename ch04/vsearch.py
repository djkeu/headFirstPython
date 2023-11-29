def search_vowels():
    """Search for vowlels in a word or sentence."""
    vowels = set('aeiou')
    word = input("Voer een woord of een zin in: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search_vowels()
