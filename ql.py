from typing import List
from inverted_index import document_information
from math import log

def ql(query: List[str], doc_id, inverted_index):
    if doc_id not in document_information:
        raise Exception("Document does not exist")