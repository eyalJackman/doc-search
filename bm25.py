from typing import List
from inverted_index import document_information
from math import log

# Typical TREC Values:
k1 = 1.2
k2 = 100
b = 0.75


def bm25(query: List[str], doc_id: "str | int", inverted_index):
    if doc_id not in document_information:
        raise Exception("Document does not exist")
    else:
        doc_length = document_information[doc_id]["len"]

    result = 0
    N = inverted_index["_totaldocs"]  # total number of docs
    dl = doc_length
    avdl = inverted_index["_collection_cnt"]

    query_freq = {}
    for q_term in query:
        query_freq[q_term] = 1 if q_term not in query_freq else query_freq[q_term] + 1

    for term in set(query):
        ni = inverted_index[term]["_numdocs"]  # number of docs containing i
        fi = inverted_index[term][doc_id] if doc_id in inverted_index[term] else 0  # frequency of term i in document
        qfi = query_freq[term]  # frequency of term in query
        K = k1 * ((1-b) + b * avdl)  # tf-normalizing factor

        bm_val1 = 1 / (ni + 0.5) / (N - ni + 0.5)
        bm_val2 = ((k1 + 1) * fi) / (K + fi)
        bm_val3 = ((k2 + 1) * qfi) / (k2 + qfi)

        result += log(bm_val1) + bm_val2 + bm_val3

    return result
