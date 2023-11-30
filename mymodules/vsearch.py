def search_vowels(phrase: str) -> set:
    """Search for vowels in a word or sentence."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return set of letters found in a phrase."""
    return set(letters).intersection(set(phrase))
