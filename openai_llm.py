# Libraries and Modules
import nltk
nltk.download('averaged_perceptron_tagger')


from langchain.llms import OpenAI
import os
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


# OpenAI key
os.environ['OPENAI_API_KEY'] = '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'

# OpenAI LLM 
llm = OpenAI(temperature=0.9, verbose=True)



#Document Loader and Splitter
loader = UnstructuredFileLoader("./Master Projects/A.I. Sales Agent/Text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embeddings and vectorstores
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

#Retrival
retriever=docsearch.as_retriever()

#Chain 
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

# Prompt
query = "what is data science?"
response = qa.run(query)
print(response)