from typing import Dict
import re
from tokenizer import tokenize, tokenize_word


# type document = Dict[str, "str | int"]
def build_index(collection: "list[dict[str]]") -> Dict[str]:
    inv_index = dict()
    doc_num = 0
    total_length = 0
    for document in collection:
        doc_dict = {}
        text = document["text"]
        split_text = re.split(r"\s+", text)
        total_length += len(text)
        for index, word in enumerate(split_text):
            if word in doc_dict:
                doc_dict[word][1] += 1
                doc_dict[word][2].append(index)
            else:
                doc_dict[word] = [doc_num, 1, [index]]

