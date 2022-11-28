import re

# import os
# print(os.getcwd())
# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)
# Helper functions

def is_vowel(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def has_vowel(w):
    for char in w:
        if is_vowel(char):
            return True
    return False


step2_list = (
    "ational", "tional", "enci", "anci", "izer", "abli", "alli", "entli", "eli", "ousli", "ization", "ation", "ator",
    "alism", "iveness", "fulness", "ousness", "aliti", "iviti", "biliti")
step2_map = {"ational": "ate", "tional": "tion", "enci": "ence", "anci": "ance", "izer": "ize", "abli": "able",
             "alli": "al", "entli": "ent", "eli": "e", "ousli": "ous", "ization": "ize", "ation": "ate", "ator": "ate",
             "alism": "al", "iveness": "ive", "fulness": "ful", "ousness": "ous", "aliti": "al", "iviti": "ive",
             "biliti": "ble"}

step4_list = (
    'al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ion', 'ou', 'ism', 'ate', 'iti',
    'ous', 'ive', 'ize')


with open("stopwords.txt", 'r') as rFile:
    stopwordStr = rFile.read()

stopwords = set()
for stopword in stopwordStr.split("\n"):
    stopwords.add(stopword)


def get_measure(word_m: str) -> int:
    """Returns measure, used in Porter Stemmer"""
    count = 0
    vowel = False
    for char in word_m:
        if vowel != is_vowel(char):
            vowel = not vowel
            if vowel is False:
                count += 1
        if count > 1:
            return count
    return count


# End Helpers


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
    if word[-3:] == "eed":
        if get_measure(word[:-3]) > 0:
            word = word[:-1]
    elif (has_vowel(word[:-2]) and word[-2:] == "ed") or (has_vowel(word[:-3]) and word[-3:] == "ing"):
        word = word[:-2] if word[-2:] == "ed" else word[:-3]
        if word[-2:] in ("at", "bl", "iz"):
            word += "e"
        elif word[-1] == word[-2] and word[-1] not in ('l', 's', 'z'):
            word = word[:-1]
        elif get_measure(word) == 1 and len(word) >= 3 and (not is_vowel(word[-3]) and is_vowel(word[-2]) and not
        is_vowel(word[-1]) and word[-1] not in ('w', 'x', 'y')):
            word += "e"

    # Step 1c
    if has_vowel(word[:-1]) and word[-1] == "y":
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
        if word[-3:] == "ful":
            word = word[:-3]
        if word[-4:] == "ness":
            word = word[:-4]

    # Step 4
    for suff in step4_list:
        if word[-len(suff):] == suff and get_measure(word[:-len(suff)]) > 1:

            if suff != "ion" or (word[-len(suff)] in ('s', 't')):
                word = word[:-len(suff)]

    # Step 5a
    measure = get_measure(word[:-1])
    if measure > 1 and word[-1] == "e":
        word = word[:-1]
    elif measure == 1 and word[-1] == "e" and (not is_vowel(word[-3]) and is_vowel(word[-2]) and not
    is_vowel(word[-1]) and word[-1] not in ('w', 'x', 'y')):
        word = word[:-1]

    # Step 5b
    if get_measure(word) > 1 and word[-1] == word[-2] and word[-1] == "l":
        word = word[:-1]

    return word


def stopword_removal(text: str):
    """Removes stopwords -- O(n) space/time"""
    words = re.split(r"\s", text)
    ret_list = [word for word in words if word not in stopwords]
    return ret_list



def punctuation_removal(text: str):
    def replacer(inp: str) -> str:
        return inp.replace('.', '')
    noAbbr = re.sub(r"([a-zA-z][.]){2,}",
                    lambda match: replacer(match.group()), text)
    noAppo = re.sub(r"[\'\’]", '', noAbbr)
    noPunc = re.sub(r"[^a-zA-Z0-9]", ' ', noAppo).lower()
    return noPunc
    # return re.sub(r"\s", r'\n', noPunc)




def tokenize(word: str) -> list[str]:
    """ Runs tokenization -- Stemming, stopword removal, punctuation removal"""
    return porter_stemmer(stopword_removal(punctuation_removal(word)))
