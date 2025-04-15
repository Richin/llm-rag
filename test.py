from langchain.document_loaders import DirectoryLoader, PyPDFLoader

# Verify if these modules load correctly
loader = DirectoryLoader("data", glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()
print(docs)
