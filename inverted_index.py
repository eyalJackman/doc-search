from typing import Dict
import re
from tokenizer import tokenize, tokenize_word


# Inverted Index: Dict {
#   _numdocs: int
#   _collection_cnt: int --- Total words in collection (For QL)
#   ...(term): {
#                  _list: [..., [doc_id, cnt, [...positions] ]
#                  _count: int --- Total word count in document (For QL/BM25)
#               }
#   }

# type document = Dict[str, "str | int"]
def build_index(collection: "List[Dict[str, str]]") -> "Dict[str, str]":
    """
    Creates inverted index from a list of documents --- InvertedIndex structure above
    """
    inv_index = dict()
    inv_index["_numdocs"] = 0
    inv_index["_collection_cnt"] = 0
    for document in collection:
        assert "id" in document and "text" in document
        text = document["text"]
        doc_id = document["id"]

        # doc_dict = {index_term : (doc_num, count, [positions])}
        #      i.e.,  index_term -> posting_list
        doc_dict = dict()

        split_text = re.split(r"\s+", text)
        inv_index["_collection_cnt"] += len(text)

        # Put terms/counts/positions into doc_dict, which will be transferred to inverted index
        for index, word in enumerate(split_text):
            # Skip if stopword
            tok_word = tokenize_word(word)
            if tok_word is None:
                continue
            if word in doc_dict:
                doc_dict[word][1] += 1
                doc_dict[word][2].append(index)
            else:
                doc_dict[word] = [doc_id, 1, [index]]

        # Transfer to inverted index
        for term in doc_dict:
            document_info = doc_dict[term] # [docid, count, [positions]]
            term_cnt = document_info[1]
            inv_index["_collection_cnt"] += term_cnt
            if term not in inv_index:
                inv_index[term] = {"_list": [document_info]}
                inv_index[term]["_count"] = term_cnt
            else:
                # Implement binary search to put these in order
                inv_index[term]["_list"].append(document_info)
                inv_index[term]["_count"] += term_cnt
        inv_index["_numdocs"] += 1

    return inv_index


def merge_index(index: "InvertedIndex", sub_index: "InvertedIndex"):
    """
    Merges the sub_index into index:
    """
    # Utilize either binary sort or using a Heap of id#s to allow for easy search
    pass




dict1 = {"id": 1203421, "text": "here we go jesus"}
dict2 = {"id": 123125125, "text": "another document for the books we have"}
# print(dict1['text'])
# print(type(dict1))
print(build_index([dict1, dict2]))





