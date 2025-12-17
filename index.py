import os
import re
from collections import defaultdict

STOPWORDS = {
    "is", "the", "a", "an", "of", "to", "in", "and", "by", "with", "for"
}

class InvertedIndex:
    def __init__(self):
        self.doc_names = {}
        self.documents = {}
        self.index = defaultdict(dict)
        self.doc_lengths = {}

    def load_documents(self, docs_path):
        for doc_id, filename in enumerate(os.listdir(docs_path)):
            file_path = os.path.join(docs_path, filename)
            with open(file_path, encoding="utf-8") as f:
                text = f.read()
                self.documents[doc_id] = text
                self.doc_names[doc_id] = filename

    def tokenize(self, text):
        tokens = re.findall(r"\b[a-z0-9]+\b", text.lower())
        return [t for t in tokens if t not in STOPWORDS]

    def build_index(self):
        for doc_id, text in self.documents.items():
            tokens = self.tokenize(text)
            self.doc_lengths[doc_id] = len(tokens)

            for position, token in enumerate(tokens):
                if doc_id not in self.index[token]:
                    self.index[token][doc_id] = []
                self.index[token][doc_id].append(position)
