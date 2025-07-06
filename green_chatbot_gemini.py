import streamlit as st
import google.generativeai as genai

# Securely load Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# App UI setup
st.set_page_config(page_title="Green Building Chatbot", page_icon="🏗️")
st.title("🏗️ Green Building Chatbot")
st.caption("Ask questions about ECBC, IGBC, and Indian green building codes.")

# User input
question = st.text_input("🌿 Ask me anything about green buildings:")

# Run model when question is entered
if question:
    with st.spinner("Thinking..."):
        try:
            prompt = (
                "You are an expert in Indian green building codes like ECBC and IGBC. "
                "Answer clearly and accurately.\n\n"
                f"Q: {question}\nA:"
            )

            # ✅ Use correct Gemini model
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
            response = model.generate_content(prompt)

            st.markdown("### 🧠 Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Something went wrong:\n\n{e}")
