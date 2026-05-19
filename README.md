# 🎬 Movie Recommendation System (Ollama + pgvector + FastAPI)

A simple content-based movie recommender system that uses **LLM embeddings (Ollama)** and **vector similarity search (pgvector)** to recommend movies based on a natural language query.

---

# 🚀 How it works

The system follows this pipeline:

User Query
↓
Ollama Embedding Model
↓
Query Vector
↓
PostgreSQL (pgvector similarity search)
↓
Top-K Similar Movies
↓
Response

Each movie is represented as a vector embedding generated from its text (title + description).

---

# 🧠 Core Idea

- Convert movie text → embedding vector
- Convert user query → embedding vector
- Compare vectors using cosine distance
- Return most similar movies

---

# 🛠 Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- pgvector
- SQLAlchemy 2.0
- Alembic
- Ollama (embeddings)
- Pydantic v2

---

# 🗄 Database

## Enable pgvector

```sql
CREATE EXTENSION IF NOT EXISTS vector;
