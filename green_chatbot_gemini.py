import streamlit as st
import google.generativeai as genai

# 🔐 Configure Gemini securely using Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 🏗️ App title and intro
st.set_page_config(page_title="Green Building Chatbot", page_icon="🏗️")
st.title("🏗️ Green Building Chatbot")
st.caption("Powered by Gemini Pro | Focused on ECBC, IGBC & Indian green codes")

# ✍️ Ask a question
question = st.text_input("🌿 Ask me anything about green buildings:")

# 📡 Generate response only if input is given
if question:
    with st.spinner("Thinking..."):
        try:
            # Prompt Gemini with a role and question
            prompt = (
                "You are an expert in Indian green building codes like ECBC and IGBC. "
                "Answer clearly and accurately.\n\n"
                f"Q: {question}\nA:"
            )

            # 🎯 Load Gemini Pro and get response
            model = genai.GenerativeModel(model_name="models/gemini-pro")
            response = model.generate_content(prompt)

            # ✅ Display result
            st.markdown("### 🧠 Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"❌ Something went wrong:\n\n{e}")
