def break_words(stuff):
    """se separa por espacios. """
    words=stuff.split(' ')
    return words

def sort_words(words):
    """acomoda en orden alfabetico"""
    return sorted(words)

def print_first_word(words):
    """imprime la primera palabra."""
    word=words.pop(0)
    print(word)

def print_last_word(words):
    """imprime la ultima palabra."""
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """agarra toda la oracion y la acomoda en orden alfabetico."""
    words=break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """imprime la primera y la ultima palabra de la oracion."""
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def sortprint_first_and_last_ed(sentence):
    """imprime la primera y la ultima palabra de la oracion en orden alfabetico."""
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)