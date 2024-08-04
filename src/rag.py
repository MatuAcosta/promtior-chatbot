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



apikey = "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"
url = "https://www.promtior.ai/"
llm = ChatOpenAI(api_key=apikey)

def load_extra_info():
    data_path = os.path.join(os.path.dirname(__file__), '.' , 'about_promtior.txt')
    file = open(data_path, 'r')
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

def set_embeddings(): 
    documents = load_page()
    embeddings = OpenAIEmbeddings(openai_api_key=apikey)
    vector = FAISS.from_documents(documents, embeddings)
    return vector


def set_prompt():
    prompt = ChatPromptTemplate.from_template("""The company is Promtior:
    <context>
    {context}
    </context>
    
    Question: {input}""")
    return prompt

def chat_with_rag(input):
    #print(input)
    extra_info = load_extra_info()
    print("extra_info", extra_info)
    prompt = set_prompt()
    vector = set_embeddings()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": input, "context": [Document(page_content="Promtior was founded in May 2023")]})
    return response["answer"]

