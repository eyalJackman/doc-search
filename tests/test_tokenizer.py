import tokenizer

porter = tokenizer.porter_stemmer


def test_stemmer():
    assert porter("lasses") == "lass", f"Step 1a: expected {porter('lasses')} to equal lass"
    assert porter("babies") == "babi", f"Step 1a: expected {porter('babies')} to equal babi"
    assert porter("russ") == "russ", f"Step 1a: expected {porter('russ')} to equal russ"
    assert porter("bras") == "bra", f"Step 1a: expected {porter('bras')} to equal bra"

    assert porter("feed") == "feed", f"Step 1b: expected {porter('feed')} to equal feed"
    assert porter("agreed") == "agree", f"Step 1b: expected {porter('agreed')} to equal agree"
    assert porter('rated') == "rate", f"Step 1b: expected {porter('rated')} to equal rate"
    assert porter("cabled") == "cable", f"Step 1b: expected {porter('cabled')} to equal cable"
    assert porter("brondizing") == "brondiz", f"Step 1b: expected {porter('brondizing')} to equal brondiz"
    assert porter("barred") == "bar"
    assert porter("galled") == "gall", f"Step 1b: expected {porter('galled')} to be gall"
    assert porter("rewed") == "rew", f"Step 1b: expected {porter('rewed')} equal to rew"
    assert porter("lened") == "lene"

    assert porter("ivy") == "ivi", f"Step 1c: expected {porter('ivy')} to be ivi"
    assert porter("ferryed") == "ferri"

    assert porter("motivate") == "motiv", f"Steps 2 and 4: expected {porter('motivate')} to be motiv"

    assert porter("abdicate") == "abdic", f"Step 3: expected {porter('abdicate')} to equal abdic"
    assert porter("realize") == "real", f"Step 3: expected {porter('realize')} to equal real"
    assert porter("indicative") == "indic", f"Step 3: expected {porter('indicative')} to equal indic"
    assert porter("feliciti") == "felic", f"Step 3: expected {porter('feliciti')} to equal felic"
    assert porter("mezical") == "mezic", f"Step 3: expected {porter('mezical')} to equal mezic"
    assert porter("gallness") == "gall", f"Step 3: expected {porter('gallness')} to equal gall"
    assert porter("lawfulness") == "law", f"Step 3: expected {porter('lawfulness')} to equal law"

    assert porter('unpedantical') == 'unped', f'Step 4: expected {porter("pedantical")} to be ped'
    assert porter("pedantical") == "pedant"
    assert porter("irreverence") == "irrev"
    assert porter("reverence") == "rever"
    assert porter("establishment") == "establish"
    assert porter("curious") == "curiou"
    assert porter("element") == "elem"

    assert porter("multidimensional") == "multidimension"
    assert porter("characterization") == "character"


if __name__ == "__main__":
    test_stemmer()
    # print(porter("abdicate"))
