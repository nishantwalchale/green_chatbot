import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

def split_text(pages, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(pages)

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    return vectorstore

def create_qa_chain(vectorstore):
    llm = Ollama(model="mistral")  # Use 'llama3' if you pulled that
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def query_pdf(qa_chain):
    print("\n✅ Ask your Green Building PDF questions!")
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() in ['exit', 'quit']:
            break
        answer = qa_chain.invoke({"query": question})
        print(f"\nAnswer:\n{answer}")

def main():
    pdf_path = r"C:\NISHANT DATA\rag\IGBC_Green_New_Buildings_Rating_System_(Version_3.0_with_Fifth_Addendum).pdf"
    print("📄 Loading PDF...")
    pages = load_pdf(pdf_path)

    print("✂️ Splitting text...")
    chunks = split_text(pages)

    print("🧠 Creating vector store...")
    vectorstore = create_vectorstore(chunks)

    print("🔗 Creating QA system...")
    qa_chain = create_qa_chain(vectorstore)

    query_pdf(qa_chain)

if __name__ == "__main__":
    main()
