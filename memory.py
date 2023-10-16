#Modules and Libraries
from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from transformers import pipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import transformers

#Loading the document
loader = UnstructuredFileLoader("./Master Projects/A.I. Sales Agent/Text.txt")
documents = loader.load()

#Text splitting
r_split = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
    separator="\n\n",
    length_function=len
)
text = r_split.split_documents(documents)

#Huggingface Embeddings and vectorstore 
embedding = HuggingFaceEmbeddings()
vectordb = Chroma.from_documents(text, embedding=embedding)

#Model and Huggingface pipeline
model_name = 'declare-lab/flan-alpaca-base'
generate_text = transformers.pipeline(
    model=model_name,
    task='text2text-generation',
    max_length=1100,
    temperature=0.9, 
    repetition_penalty=1.1 
)
llm = HuggingFacePipeline(pipeline=generate_text)

#Memory and conversational chain
memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)

qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectordb.as_retriever(),memory=memory)

#loop
def loop():
    global response
    x = True
    while x==True:
        prompt = input('Input your prompt here')
        if prompt=='exit':
            return x==False
        else:
            response = qa.run(prompt)
            print("Poorva Said: ")
            print(response)

    print("You have exited")   

loop()


