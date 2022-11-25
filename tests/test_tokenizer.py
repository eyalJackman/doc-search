import tokenizer

porter = tokenizer.porter_stemmer


def test_stemmer():
    assert porter("abdicate") == "abdic", f"expected {porter('abdicate')} to equal abdic"
    assert porter("realize") == "real", f"expected {porter('realize')} to equal real"
    assert porter("indicative") == "indic", f"expected {porter('indicative')} to equal indic"
    assert porter("feliciti") == "felic", f"expected {porter('feliciti')} to equal felic"
    assert porter("mezical") == "mezic", f"expected {porter('mezical')} to equal mezic"
    assert porter("gallness") == "gall", f"expected {porter('gallness')} to equal gall"
    assert porter("lawfulness") == "law", f"expected {porter('lawfulness')} to equal law"


if __name__ == "__main__":
    test_stemmer()
    # print(porter("abdicate"))
