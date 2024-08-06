import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ.get("OPEN_AI_KEY") 
url = "https://www.promtior.ai/"
llm = ChatOpenAI(api_key=apikey)

def load_extra_info():
    path = os.path.join(os.path.dirname(__file__), '.' , 'about_promtior.txt')
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content


# load the document to help with retrieval
def load_page(): 
    loader = WebBaseLoader(url) 
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    return documents

# page doesnt have all necessary info so I use about_promtior.txt to complement
def set_embeddings(): 
    documents = load_page()
    text_extra_info = load_extra_info()
    documents.append(Document(page_content=text_extra_info))
    embeddings = OpenAIEmbeddings(openai_api_key=apikey)
    vector = FAISS.from_documents(documents, embeddings)
    return vector


def set_prompt():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the user's questions based on the below context:\n\n{context}"),
        ("user", "{input}"),
    ])
    return prompt

def chat_with_rag(input):
    prompt = set_prompt()
    vector = set_embeddings()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": input, })
    return response["answer"]

