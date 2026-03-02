# Search Engine from Scratch (BM25 + Phrase Search)

A lightweight search engine implemented entirely in Python.  
This project builds a positional inverted index and BM25 ranking system from first principles, exposed through a FastAPI REST API.

No external search libraries are used. All core Information Retrieval logic is implemented manually.

---

## 1. Installation & Setup

### Clone the repository

```bash
git clone https://github.com/your-username/search-engine.git
cd search-engine
```

### Create virtual environment

```bash
python -m venv venv
```

Activate it:

Linux / macOS
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Running the Server

Start the FastAPI application using Uvicorn:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## 3. Example API Usage

### Basic search

```bash
curl "http://127.0.0.1:8000/search?q=machine learning"
```

### Exact phrase search

```bash
curl "http://127.0.0.1:8000/search?q=\"machine learning\""
```

### Top-k results

```bash
curl "http://127.0.0.1:8000/search?q=machine learning&k=3"
```

---

## 4. Technologies Used

### Python  
Core programming language used for implementing indexing, ranking, and API logic.

### FastAPI  
Used to expose the search engine through a RESTful interface.

### Uvicorn  
ASGI server used to run the FastAPI application.

No search frameworks such as Elasticsearch, Lucene, Whoosh, or similar libraries are used. All ranking and indexing logic is implemented manually.

---

## 5. System Architecture

### Inverted Index

A positional inverted index maps:

```
term → document → list of positions
```

This structure enables:
- Fast term-based retrieval
- Exact phrase matching via positional checks

### BM25 Ranking

Implements the Okapi BM25 scoring function with:

- Term Frequency (TF)
- Document Frequency (DF)
- Inverse Document Frequency (IDF)
- Document length normalization

This is a production-grade ranking approach used in modern retrieval systems.

### Query Processing

Query pipeline includes:

1. Tokenization
2. Stopword removal
3. Normalization
4. Phrase detection
5. Ranking and aggregation

---

## 6. Features

- Positional inverted index
- BM25 ranking algorithm
- Exact phrase search
- Stopword filtering
- Query normalization
- Contextual snippet generation
- REST API interface
- Swagger-based testing interface

---

## 7. Project Structure

```
search-engine/
│
├── main.py            # FastAPI application and routes
├── index.py           # Inverted index construction
├── rank.py            # BM25 scoring logic
├── query.py           # Search orchestration
├── data/docs/         # Sample documents
├── requirements.txt
└── README.md
```

---

