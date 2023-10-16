 # libraries and Modules
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain import HuggingFacePipeline

#Document Loader and Splitter 
loader = UnstructuredFileLoader("./Master Projects/A.I. Sales Agent/Text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.9, "max_length": 512}
)

# Embeddings and Vectorstores
directory='db'
embeddings = HuggingFaceEmbeddings()
docsearch = Chroma(persist_directory=directory, embedding_function=embeddings)

#Chain
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

# Prompt
query = "What  module or topic you will need to learn in data science?"
response = qa.run(query)
print(response)