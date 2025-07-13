🏗️ Green Building Chatbot (Local RAG using Ollama)
This is a simple locally hosted RAG chatbot that answers questions from the IGBC Green New Buildings Rating System PDF — without using any paid APIs.

Built using:

🔍 LangChain for RAG pipeline

🧠 FAISS for local vector storage

🧩 HuggingFace sentence embeddings

🤖 Ollama with mistral or llama3 running locally

🚀 Features
✅ Load and process large green building PDFs

✅ Ask natural language questions about IGBC guidelines

✅ No API keys or cloud dependencies

✅ Runs completely offline with Ollama

🛠️ Requirements
Python 3.10+

Ollama installed and running with model like mistral or llama3

Install dependencies:

bash
Copy
Edit
pip install langchain langchain-community faiss-cpu sentence-transformers
📂 How to Run
Download the IGBC PDF
Update the path in pdf_path inside main() function of app.py

Make sure Ollama is running
Start a terminal and run:

bash
Copy
Edit
ollama run mistral
# or
ollama run llama3
Run the script

bash
Copy
Edit
python app.py
Ask Questions!

mathematica
Copy
Edit
✅ Ask your Green Building PDF questions!

Ask a question (or type 'exit'): What are the criteria for site selection?
📚 Example Questions
What is the intent of Energy Efficiency credit?

Which documents are needed for Water Efficiency?

How many points are required for Platinum rating?

📦 File Structure
graphql
Copy
Edit
├── app.py           # Main chatbot script
├── README.md        # Project instructions
└── IGBC_Green.pdf   # Place your PDF file here
🤝 Contributing
This is a starter template. Feel free to fork and extend it for other rating systems like LEED, GRIHA, or ECBC.

📣 Credits
IGBC for the original PDF content

LangChain, HuggingFace, FAISS, and Ollama — for enabling free, local AI