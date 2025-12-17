import re
from rank import BM25Ranker
from index import STOPWORDS

class SearchEngine:
    def __init__(self, index):
        self.index = index
        self.ranker = BM25Ranker(index)

    def tokenize_query(self, query):
        tokens = re.findall(r"\b[a-z0-9]+\b", query.lower())
        return [t for t in tokens if t not in STOPWORDS]

    def get_snippet(self, doc_text, query_tokens, window=30):
        words = doc_text.split()
        for i, word in enumerate(words):
            if word.lower().strip(".,") in query_tokens:
                start = max(0, i - window)
                end = min(len(words), i + window)
                return " ".join(words[start:end])
        return " ".join(words[:window])

    def highlight(self, text, query_tokens):
        for token in query_tokens:
            text = re.sub(
                rf"\b({token})\b",
                r"**\1**",
                text,
                flags=re.IGNORECASE
            )
        return text

    def phrase_match(self, phrase_tokens):
        candidate_docs = None
        for token in phrase_tokens:
            if token not in self.index.index:
                return []
            docs = set(self.index.index[token].keys())
            candidate_docs = docs if candidate_docs is None else candidate_docs & docs

        results = []
        for doc_id in candidate_docs:
            positions = [self.index.index[token][doc_id] for token in phrase_tokens]
            for start in positions[0]:
                if all(start + i in positions[i] for i in range(len(positions))):
                    results.append(doc_id)
                    break
        return results

    def search(self, query):
        query = query.strip()
        if query.startswith('"') and query.endswith('"'):
            phrase = query.strip('"')
            tokens = self.tokenize_query(phrase)
            doc_ids = self.phrase_match(tokens)
            results = []
            for doc_id in doc_ids:
                snippet = self.get_snippet(self.index.documents[doc_id], tokens)
                snippet = self.highlight(snippet, tokens)
                results.append((doc_id, 1.0, snippet))
            return results

        tokens = self.tokenize_query(query)
        ranked = self.ranker.rank(tokens)
        results = []
        for doc_id, score in ranked:
            snippet = self.get_snippet(self.index.documents[doc_id], tokens)
            snippet = self.highlight(snippet, tokens)
            results.append((doc_id, score, snippet))
        return results
