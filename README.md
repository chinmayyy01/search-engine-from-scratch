## 🔍 Search Engine from Scratch (BM25 + Phrase Search)

A lightweight **search engine built entirely from scratch** using Python, implementing a **positional inverted index**, **BM25 ranking**, and **exact phrase search**, exposed via a **FastAPI REST API**.

This project demonstrates core **Information Retrieval (IR)** concepts without relying on external search libraries.


## 🚀 Features

- **Positional Inverted Index** (term → document → positions)
- **BM25 ranking algorithm** (production-grade scoring)
- **Exact phrase search** using positional matching
- **Stopword removal** and query normalization
- **Contextual snippet generation** with keyword highlighting
- **REST API** built with FastAPI
- Fully testable via browser or **Swagger UI**


## 🧠 Core Concepts Implemented

- Inverted index construction
- Term Frequency (TF) & Document Frequency (DF)
- BM25 scoring with document length normalization
- Positional indexing for phrase queries
- Query tokenization and preprocessing
- Ranking and result aggregation


## 🗂️ Project Structure

search-engine/
├── main.py          # FastAPI app and API routes
├── index.py         # Inverted index + document loader
├── rank.py          # BM25 ranking logic
├── query.py         # Search engine orchestration
├── data/docs/       # Sample text documents
├── requirements.txt
├── README.md


## ⚙️ Setup & Run

### Install dependencies

pip install -r requirements.txt


### Start the server

python -m uvicorn main:app --reload


### Open API docs

http://127.0.0.1:8000/docs


## 🔍 Example Queries

### Normal search

/search?q=machine learning


### Phrase search

/search?q="machine learning"


### Top-k results

/search?q=machine learning&k=3


## 📌 Why This Project Matters

This project focuses on **fundamental search system design**, mirroring concepts used in real-world systems like **Elasticsearch** and **Lucene**, but implemented manually to demonstrate **deep understanding rather than library usage**.


## 📈 Possible Extensions

* Query expansion
* Field-based search
* Ranking evaluation (MAP, NDCG)
* Index persistence to disk
* Frontend UI
