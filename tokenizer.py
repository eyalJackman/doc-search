import re


isVowel = lambda c: c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'
# vowels = 'aeiou'

def get_measure(word: str) -> int:
    """Returns measure, used in Porter"""
    count = 0
    vowel = False
    for char in str:
        if vowel == isVowel(char):
            vowel = not vowel
            if vowel is False:
                count += 1
        if count > 1:
            return count
    return count


def porter_stemmer():
    """ Porter Stemmer as defined in https://vijinimallawaarachchi.com/2017/05/09/porter-stemming-algorithm/ \n
        Used to get word stems
    """
    pass


def stopword_removal():
    pass


def punctuation_removal():
    pass






def tokenize(word: str) -> str:
    """ Runs tokenization -- Stemming, stopword removal, punctuation removal"""
    return porter_stemmer(stopword_removal(punctuation_removal(word)))