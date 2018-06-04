from utils.letter_value import letter_value

def word_value(word):
    return sum([letter_value(letter) for letter in word])
