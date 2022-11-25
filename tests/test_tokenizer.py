import tokenizer

porter = tokenizer.porter_stemmer


def test_stemmer():
    assert porter("lasses") == "lass", f"Step 1a: expected {porter('lasses')} to equal lass"
    assert porter("babies") == "babi", f"Step 1a: expected {porter('babies')} to equal babi"
    assert porter("russ") == "russ", f"Step 1a: expected {porter('russ')} to equal russ"
    assert porter("bras") == "bra", f"Step 1a: expected {porter('bras')} to equal bra"

    assert porter("feed") == "feed", f"Step 1b: expected {porter('feed')} to equal feed"
    assert porter("agreed") == "agree" , f"Step 1b: expected {porter('agreed')} to equal agree"
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
