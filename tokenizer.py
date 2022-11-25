import re


isVowel = lambda c: c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

def hasVowel(w):
    for char in w:
        if isVowel(char):
            return True
    return False


step2_list = ("ational", "tional", "enci", "anci", "izer", "abli", "alli", "entli", "eli", "ousli", "ization", "ation", "ator", "alism", "iveness", "fulness", "ousness", "aliti", "iviti", "biliti")
step2_map = {"ational": "ate", "tional": "tion", "enci": "ence", "anci": "ance", "izer": "ize", "abli": "able", "alli": "al", "entli": "ent", "eli": "e", "ousli": "ous", "ization": "ize", "ation": "ate", "ator": "ate", "alism": "al", "iveness": "ive", "fulness": "ful", "ousness": "ous", "aliti": "al", "iviti": "ive", "biliti": "ble"}

step4_list = ('al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ion', 'ou', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize')

def get_measure(word: str) -> int:
    """Returns measure, used in Porter Stemmer"""
    count = 0
    vowel = False
    for char in word:
        if vowel != isVowel(char):
            vowel = not vowel
            if vowel is False:
                count += 1
        if count > 1:
            return count
    return count


def porter_stemmer(word: str):
    """ Porter Stemmer as defined in https://vijinimallawaarachchi.com/2017/05/09/porter-stemming-algorithm/ \n
        Used to get word stems
    """
    measure = get_measure(word)
    # print(measure)
    length = len(word)
    # Step 1a
    if length > 4 and word[-4:] == "sses":
        word = word[:-2]
    elif length > 3 and word[-3:] == "ies":
        word = word[:-2]
    elif length > 2 and word[-2:] == "ss":
        pass
    elif word[-1] == "s":
        word = word[:-1]
    
    # Step 1b
    if word[-3:] == "eed" and get_measure(word[:-3]) > 0:
        word = word[:-1]
    if (hasVowel(word[:-2]) and word[-2:] == "ed") or (hasVowel(word[:-3]) and word[-3:] == "ing"):
        word = word[:-2] if word[-2:] == "ed" else word[:-3]
        if word[-2:] in ("at", "bl", "iz"):
            word += "e"
        elif word[-1] == word[-2]:
            word = word[:-1]
        elif get_measure(word) == 1 and (not isVowel(word[-3]) and isVowel(word[-2]) and not isVowel(word[-1]) and word[-1] not in ('w', 'x', 'y')):
            word += "e"
    
    # Step 1c
    if hasVowel(word[:-1]) and word[-1] == "y":
        word = word[:-1] + "i"

    # Step 2
    if get_measure(word) > 0:
        for suff in step2_list:
            if word.endswith(suff):
                word = word[:-len(suff)] + step2_map[suff]
    
    # Step 3
    if get_measure(word) > 0:
        if word[-5:] == "ative":
            word = word[:-5]
        if word[-5:] == "icate" or word[-5:] == "alize" or word[-5:] == "iciti":
            word = word[:-3]
        if word[-4:] == "ical":
            word = word[:-2]
        if  word[-3:] == "ful":
            word = word[:-3]
        if word[-4:] == "ness":
            word = word[:-4]

    # Step 4
    for suff in step4_list:
        if get_measure(word[-len(suff):]) > 1:
            word = word[:-len(suff)]
    
    return word


# print(porter_stemmer("abdicate"))
# print(porter_stemmer("realize"))
# print(porter_stemmer("indicative"))
# print(porter_stemmer("feliciti"))
# print(porter_stemmer("mezical"))
# print(porter_stemmer("gallness"))

print(porter_stemmer("lawfulness"))






def stopword_removal():
    pass


def punctuation_removal():
    pass


# w = "de"
# print(w[:-3])


def tokenize(word: str) -> str:
    """ Runs tokenization -- Stemming, stopword removal, punctuation removal"""
    return porter_stemmer(stopword_removal(punctuation_removal(word)))