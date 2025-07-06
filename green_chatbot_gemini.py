import streamlit as st
import google.generativeai as genai

# Gemini API Key (Hardcoded for demo – replace 'xxxx' with your key)
genai.configure(api_key="AIzaSyBsuvHj_M9mXZFN-zPDLCapwYryC0WzYJE")

st.title("🏗️ Green Building Chatbot (Gemini Version)")

model = genai.GenerativeModel('gemini-pro')

question = st.text_input("Ask me anything about green buildings:")

if question:
    prompt = f"You are an expert in Indian green building codes like ECBC and IGBC. Answer clearly and accurately.\n\nQ: {question}\nA:"
    response = model.generate_content(prompt)
    st.write("🧠", response.text)
