# from langchain.document_loaders import DirectoryLoader, PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
# from langchain.vectorstores import FAISS

# def create_vector_store(data_dir="data", save_path="vectorstore"):
#     try:
#         # Load documents from the specified directory
#         loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
#         docs = loader.load()

#         # Split documents into smaller chunks
#         splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
#         chunks = splitter.split_documents(docs)

#         # Use HuggingFace embeddings for vectorization
#         embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#         # Create FAISS index from documents
#         db = FAISS.from_documents(chunks, embedding)

#         # Save the FAISS index to the specified directory
#         db.save_local(save_path)
#         print(f"Vector store created and saved to {save_path}")

#     except Exception as e:
#         print(f"Error while creating vector store: {e}")

# # Regenerate the FAISS index
# create_vector_store(data_dir="data", save_path="vectorstore")


from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(data_dir="data", save_path="vectorstore"):
    loader = DirectoryLoader(data_dir, glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embedding)
    db.save_local(save_path)

def load_vector_store(path="vectorstore"):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(path, embedding, allow_dangerous_deserialization=True)
