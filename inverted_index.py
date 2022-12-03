from typing import Dict
import re
from tokenizer import tokenize, tokenize_word


# type document = Dict[str, "str | int"]
def build_index(collection: "list[dict[str]]"):  # -> Dict[str]:
    inv_index = dict()
    doc_num = 0
    total_length = 0
    for document in collection:
        doc_dict: "dict[str, list]" = {}
        text = document["text"]
        split_text = re.split(r"\s+", text)
        total_length += len(split_text)
        for index, word in enumerate(split_text):
            term = tokenize_word(word)
            if term == None:
                continue
            if term in doc_dict:
                doc_dict[term][1] += 1
                doc_dict[term][2].append(index - 1)
            else:
                doc_dict[term] = [doc_num, 1, [index]]
        for posting in doc_dict:
            if posting in inv_index:
                inv_index[posting].append(doc_dict[posting])
            else:
                inv_index[posting] = [doc_dict[posting]]
        doc_num += 1
    inv_index["_totallen"] = total_length
    inv_index["_avglen"] = total_length / doc_num
    return inv_index
