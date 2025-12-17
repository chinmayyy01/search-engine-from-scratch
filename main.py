from fastapi import FastAPI
from index import InvertedIndex
from query import SearchEngine

app = FastAPI()

index = InvertedIndex()
index.load_documents("data/docs")
index.build_index()

engine = SearchEngine(index)

@app.get("/search")
def search(q: str, k: int = 5):
    results = engine.search(q)[:k]

    return {
        "query": q,
        "results": [
            {
                "doc_id": doc_id,
                "doc_name": index.doc_names[doc_id],
                "score": round(score, 4),
                "snippet": snippet
            }
            for doc_id, score, snippet in results
        ]
    }
