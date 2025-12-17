import math

class BM25Ranker:
    def __init__(self, index, k1=1.5, b=0.75):
        self.index = index
        self.k1 = k1
        self.b = b
        self.N = len(index.documents)
        self.avgdl = sum(index.doc_lengths.values()) / self.N

    def rank(self, query_tokens):
        scores = {}

        for token in query_tokens:
            if token not in self.index.index:
                continue

            df = len(self.index.index[token])
            idf = math.log(1 + (self.N - df + 0.5) / (df + 0.5))

            for doc_id, positions in self.index.index[token].items():
                tf = len(positions)               # 🔥 THIS IS THE KEY LINE
                dl = self.index.doc_lengths[doc_id]

                denom = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                score = idf * (tf * (self.k1 + 1)) / denom

                scores[doc_id] = scores.get(doc_id, 0) + score

        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
