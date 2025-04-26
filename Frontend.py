# Frontend.py

import streamlit as st
import asyncio
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from Backend import search_papers, generate_context_summary

# Load LLM model
@st.cache_resource(show_spinner=False)
def load_llm(model_name="llama3"):
    return OllamaLLM(model=model_name, base_url="https://e8a4-34-143-171-160.ngrok-free.app")  # Replace with Ollama's Ngrok URL
# Available LLMs
models = {
    "Llama3": "llama3",
    "Mistral": "mistral",
    "Vicuna": "vicuna",
}

# Setup Streamlit App
st.title("🧠 Expert Chatbot with RAG - Computer Science Domain")

# Model Selection
selected_model = st.selectbox("Select LLM Model", list(models.keys()), key="model_selector")
llm = load_llm(models[selected_model])

# Chat Prompt Template
system_instruction = """
You are an expert assistant specializing in computer science.
Use retrieved academic papers as context if available.
Otherwise, explain the concept clearly and concisely.
"""
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_instruction),
    ("user", "{question}")
])

# Async LLM Streaming
async def generate_response(full_prompt):
    response = ""
    async for chunk in llm.astream(prompt_template.format(question=full_prompt)):
        response += chunk
        yield response

# Async main runner
async def run_async_llm(full_prompt):
    with st.spinner("Generating response..."):
        response_placeholder = st.empty()
        async for response in generate_response(full_prompt):
            response_placeholder.write(response)

def run_async_query(prompt_text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_async_llm(prompt_text))

# Tabs for Different Features
tab1, tab2, tab3 = st.tabs(["🔎 Ask Expert", "📚 Summarize Papers", "🧠 Explain Concept"])

with tab1:
    st.header("🔎 Ask Expert (with Context)")
    user_query = st.text_input("Enter your query about Computer Science:")
    if st.button("Get Expert Answer"):
        if user_query.strip():
            # Search Papers
            papers = search_papers(user_query)
            context = generate_context_summary(papers)
            final_prompt = f"Context:\n{context}\n\nQuestion: {user_query}"
            run_async_query(final_prompt)
        else:
            st.warning("Please enter a question.")

with tab2:
    st.header("📚 Summarize Uploaded Paper or Text")
    uploaded_file = st.file_uploader("Upload a .txt file for summarization", type=["txt"])
    manual_text = st.text_area("Or paste your custom text here:")

    if st.button("Summarize Text"):
        text_to_summarize = ""
        if uploaded_file is not None:
            text_to_summarize = uploaded_file.read().decode("utf-8")
        elif manual_text.strip():
            text_to_summarize = manual_text.strip()

        if text_to_summarize:
            final_prompt = f"Summarize the following text in 150 words:\n\n{text_to_summarize}"
            run_async_query(final_prompt)
        else:
            st.warning("Please upload or paste some text first.")

with tab3:
    st.header("🧠 Explain Any Concept Clearly")
    concept_query = st.text_input("Enter the concept you want explained (e.g., Neural Networks):")
    if st.button("Explain Concept"):
        if concept_query.strip():
            final_prompt = f"Explain the following computer science concept simply:\n\n{concept_query}"
            run_async_query(final_prompt)
        else:
            st.warning("Please enter a concept.")

