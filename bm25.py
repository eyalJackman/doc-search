from typing import List
from inverted_index import document_information
from math import log

# Typical TREC Values:
k1 = 1.2
k2 = 100
b = 0.75


def bm25(query: List[str], doc_id):
    total = 0
    query_freq = {}
    for q_term in query:
        query_freq[q_term] = 1 if q_term not in query_freq else query_freq[q_term] + 1

    for term in set(query):
        ni =  0 # number of docs containing i
        N = 0 # total number of docs
        fi = 0 # frequency of term i in document
        qfi = query_freq[term] # frequency of term in query
        K = 0 # tf-normalizing factor

        bmval1 = 1 / (ni + 0.5) / (N - ni + 0.5)
        bmval2 = ((k1 + 1) * fi) / (K + fi)
        bmval3 = ((k2 + 1) * qfi) / (k2 + qfi)
