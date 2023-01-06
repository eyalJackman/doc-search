from typing import Dict
import re
from tokenizer import tokenize, tokenize_word


# type document = Dict[str, "str | int"]
def build_index(collection: "list[Dict[str, str]]") -> "Dict[str, str]":
    """
    Creates inverted index from a list of documents
    """
    inv_index = dict()
    inv_index["_numdocs"] = 0
    inv_index["_collection_cnt"] = 0
    for document in collection:
        doc_dict = dict()
        text = document["text"]
        doc_id = document["id"]
        split_text = re.split(r"\s+", text)
        inv_index["_collection_cnt"] += len(text)
        # doc_dict = {index_term : (doc_num, count, [positions])}
        #      i.e.,  index_term -> posting_list

        for index, word in enumerate(split_text):
            if word in doc_dict:
                doc_dict[word][1] += 1
                doc_dict[word][2].append(index)
            else:
                doc_dict[word] = [doc_id, 1, [index]]
        for term in doc_dict:
            document_info = doc_dict[term] # [docid, count, [positions]]
            term_cnt = document_info[1]
            inv_index["_collection_cnt"] += term_cnt
            if term not in inv_index:
                inv_index[term]= {"_list": [document_info]}
                inv_index[term]["_count"] = term_cnt
            else:
                inv_index[term]["_list"].append(document_info)
                inv_index[term]["_count"] += term_cnt
        inv_index["_numdocs"] += 1
    return inv_index


dict1 = {"id": 1203421, "text": "here we go jesus"}
dict2 = {"id": 123125125, "text": "another document for the books we have"}
# print(dict1['text'])
# print(type(dict1))
print(build_index([dict1, dict2]))





