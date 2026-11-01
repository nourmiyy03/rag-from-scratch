#  RAG From Scratch — Understanding Retrieval-Augmented Generation

> Learning how to build AI systems by understanding what's happening under the hood, one project at a time.

##  About the Project

This project is my hands-on introduction to **Retrieval-Augmented Generation (RAG)**, built from scratch using Python and Ollama.

The idea behind RAG is simple: instead of asking an AI model to answer questions using only what it already knows, we give it access to an external knowledge base. It retrieves relevant information and uses that context to generate more grounded answers.

I wanted to understand how this process actually works rather than simply relying on ready-made frameworks.

So, I'm exploring the fundamental building blocks myself: embeddings, text chunking, similarity search, and language models.

##  How Does It Work?

The project follows a simple RAG pipeline:

```text
       
User asks a question -> Search (Look through every chunk of the docs) -> Returns the top 3 similar chunks -> augmented it tp  the prompt -> LLM answers

```

### The main components

| Component | Purpose |
|---|---|
| **Text Chunking** | Splits documents into smaller pieces of text. |
| **Embeddings** | Converts text into numerical vectors that capture semantic meaning. |
| **Vector Similarity** | Measures how semantically close two vectors are. |
| **Retrieval** | Finds the most relevant chunks for a question. |
| **Generation** | Sends the retrieved context to an LLM to generate an answer. |

##  Tech Stack

- **Python** — Main programming language.
- **Ollama** — Running language and embedding models locally.
- **Qwen3 (1.7B)** — Language model for generating answers.
- **Nomic Embed Text** — Embedding model for representing text as vectors.
- **NumPy** — Vector operations and cosine similarity calculations.
- **Requests** — Communicating with the Ollama API.


##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-from-scratch.git
cd rag-from-scratch
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama models

Make sure [Ollama](https://ollama.com/) is installed.

Pull the language model:

```bash
ollama pull qwen3:1.7b
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

### 5. Run the project

```bash
python rag.py
```

##  Knowledge Base

For experimentation, I created a fictional restaurant knowledge base called **The Cozy Corner**.

It contains information about:
- Restaurant details and opening hours.
- Menu items and prices.
- Allergens and dietary requirements.
- Reservations and delivery.
- Promotions and loyalty programs.
- Frequently asked questions.

This gives the RAG system a controlled source of information to retrieve from and answer questions about.

##  What I'm Learning

This project is helping me understand:

- How text embeddings represent semantic meaning.
- Why chunking matters in document retrieval.
- How cosine similarity works in vector search.
- How to connect local LLMs to Python applications.
- Why retrieval can improve the relevance and grounding of AI-generated answers.
- The limitations of LLMs, including hallucinations.

##  What's Next?

Some ideas I'd like to explore as I continue developing my understanding of RAG:

- [ ] Experiment with different chunking strategies.
- [ ] Improve retrieval accuracy.
- [ ] Explore vector databases.
- [ ] Add document upload support (PDF and TXT).
- [ ] Build a simple chat interface.
- [ ] Evaluate retrieval quality and answer accuracy.


##  About Me

Hi! I'm a **Data Engineering & AI student** interested in understanding how intelligent systems work and how technology can be used to solve real-world problems.

I'm particularly interested in:

- Artificial Intelligence & Machine Learning
- Generative AI and LLM applications
- Data Engineering
- Software Development
- Cybersecurity and Blockchain

I enjoy learning by experimenting, building projects, making mistakes, and documenting what I discover along the way.

This repository is part of that journey. It's not just about having a working RAG system; it's about understanding the concepts behind it.

**I'm learning, building, and sharing the process. One project at a time.**

### Let's Connect!

- GitHub: https://github.com/nourmiyy03
- LinkedIn: www.linkedin.com/in/nourmiyy03


---

If you find this project interesting, feel free to explore, fork, or share your thoughts!

*Built with curiosity, Python, and a lot of experimentation.*
