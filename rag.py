import requests
import numpy as np
from pathlib import Path


OLLAMA = "http://localhost:11434" #endpoint
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3:1.7b"


# this function sends a request to embed model
def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed", json={"model": EMBED_MODEL, "input": texts})

    return np.array(r.json()["embeddings"]) #we convert the response (the embeddings field from the response more specifically) to an numpy array (more efficient version of py lists that allows us to do some mathematical operations)


# sends request to our LLM
def ask_llm(prompt):
    r = requests.post(f"{OLLAMA}/api/chat", json={
        "model": CHAT_MODEL, "stream" : False, "messages":[{"role": "user", "content" : prompt}],
    })
    # "stream" : False = means we get the entire response at once 

    return r.json()["message"]["content"]


#we create a new list for the chunks
chunks = []
# this will go through every file in docs that ends with ".md"
for file in Path("docs").glob("*.md"):
    chunks += [p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]


chunk_vectors = embed(chunks)
print(f"Indexed {len(chunks)} chunks \n")


# k here for defining how many chunks we retrieve. so here if we don't specify k we retrieve 3 (by default) similar chunks to the asked question
def retrieve(question, k=3):
    q = embed([question])[0] #to embed the asked question

    # In Python's NumPy, @ means matrix multiplication.
    # np.linalg.norm()? calculates the length of a vector (sqrt(x^2 + y^2))
    scores = chunk_vectors @ q / (np.linalg.norm(chunk_vectors, axis=1) * np.linalg.norm(q))


    # argsort() returns the indices that would sort the scores in ascending order. 
    # [::-1] : Python slicing syntax. It reverses the order of a list or array.
    #[:k] : selects the first k elements.

    return [chunks[i] for i in np.argsort(scores)[::-1][:k]]
# For every index i in the selected indices, retrieve chunks[i] and put it into a new list.


while True :
    question = input("Ask: ")
    context = "\n\n".join(retrieve(question))
    prompt = f"""Answer the question using ONLY the context below. 
    If the answer isn't in the context, say "I don't know".

    Context :
    {context}

    Question : {question} """

    print("\n" + ask_llm(prompt) + "\n")