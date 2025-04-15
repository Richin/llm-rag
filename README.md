# RAG Medical Diagnosis Assistant

A Retrieval-Augmented Generation (RAG) system for medical diagnosis assistance, combining vector search with LLM-based response generation.

## Workflow

1. **Initialization**
   - The system loads a pre-built vector store containing medical knowledge
   - Vector store is initialized using FAISS for efficient similarity search

2. **Query Processing**
   - User provides symptoms and medical history
   - System formats the input into a structured query
   - Performs similarity search against the vector store
   - Retrieves top 4 most relevant medical documents

3. **Response Generation**
   - System constructs a prompt combining:
     - Retrieved medical context
     - Patient symptoms
     - Medical history
   - Sends prompt to DeepSeek API
   - Returns formatted diagnostic summary in markdown

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Prepare vector store:
   - Place medical documents in appropriate format
   - Run vector store creation script
   - Store in "vectorstore" directory

3. Run the application:
```bash
python app.py
```

## Usage Example

```python
from main_agent import RAGLLMAgent

# Initialize agent
agent = RAGLLMAgent()

# Run diagnosis
result = agent.run(
    symptoms=["fever", "fatigue", "rash"],
    history="25-year-old male recently returned from tropical travel."
)

print(result)
```

## Dependencies

- langchain: For vector store and document handling
- sentence-transformers: For text embeddings
- faiss-cpu: For efficient similarity search
- pypdf: For PDF document processing
- ollama: For running DeepSeek model
- streamlit: For web interface (optional)

## Project Structure

```
.
├── app.py                 # Main application
├── main_agent.py          # RAG agent implementation
├── models/
│   └── deepseek_r3_1_5_api.py  # DeepSeek API integration
├── utils/
│   ├── loaders.py        # Vector store loading
│   └── helper.py         # Utility functions
└── vectorstore/          # Pre-built vector store
```

## Notes

- The system uses a pre-built vector store for efficiency
- Medical context is retrieved based on symptom similarity
- Responses are generated using DeepSeek API
- All responses are formatted in markdown for better readability

## Workflow Diagram

```
┌─────────────────┐
│  RAGLLMAgent   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Load Vector DB  │
└─────────────────┘
```