from utils.loaders import load_vector_store
from utils.helper import format_chunks
from models.deepseek_r3_1_5_api import ask_deepseek

class RAGLLMAgent:
    def __init__(self):
        self.db = load_vector_store("vectorstore")

    def run(self, symptoms, history):
        query = f"Symptoms: {', '.join(symptoms)}. History: {history}"
        docs = self.db.similarity_search(query, k=4)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"""
Use the following clinical context to provide a diagnostic summary.

Context:
{context}

Patient Info:
Symptoms: {', '.join(symptoms)}
History: {history}

Answer in markdown.
"""
        return ask_deepseek(prompt)
