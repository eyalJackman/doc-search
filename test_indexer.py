import inverted_index

indexer = inverted_index.build_index


def test_indexer():
    basic_text = [{"text": "This is an example document"}]
    basic_index = {"example": [[0, 1, [3]]], "document": [[
        0, 1, [4]]], "_totallen": 5, "_avglen": 5.0}
    assert indexer(basic_text) == basic_index, f'Result: {indexer(basic_text)}'

    med_corpus = [{"text": "This is document one"},
                  {"text": "this Here is Document two!"}]
    med_index = {"document": [[0, 1, [2]], [1, 1, [3]]], "one": [
        [0, 1, [3]]], "two": [[1, 1, [4]]], "_totallen": 9, "_avglen": 4.5}
    assert indexer(med_corpus) == med_index, f'Result: {indexer(med_corpus)}'


if __name__ == "__main__":
    test_indexer()
