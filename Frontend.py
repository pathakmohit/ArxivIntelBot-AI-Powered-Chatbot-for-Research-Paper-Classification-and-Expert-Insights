import streamlit as st
import asyncio
import logging
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from Backend import search_papers, generate_context_summary
import PyPDF2
from io import BytesIO

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load LLM model with timeout
@st.cache_resource(show_spinner=False)
def load_llm(model_name="llama3"):
    try:
        return OllamaLLM(model=model_name, timeout=30)
    except Exception as e:
        logger.error(f"Failed to load LLM {model_name}: {e}")
        st.error(f"Failed to load model {model_name}. Please ensure Ollama is running.")
        raise

# Available LLMs
models = {
    "Llama3": "llama3",
    "Mistral": "mistral",
    "Vicuna": "vicuna",
}

# Setup Streamlit App
st.title("🧠 ArxivIntelBot: AI-Powered Chatbot for Research Paper Classification and Expert Insights")

# Model Selection
selected_model = st.selectbox("Select LLM Model", list(models.keys()), key="model_selector")
try:
    llm = load_llm(models[selected_model])
except Exception:
    st.stop()

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
    try:
        response = ""
        async for chunk in llm.astream(prompt_template.format(question=full_prompt)):
            response += chunk
            yield response
    except Exception as e:
        logger.error(f"Error in LLM streaming: {e}")
        st.error("Failed to generate response. Please check if the Ollama server is running.")
        yield f"Error: {e}"

# Async main runner
async def run_async_llm(full_prompt):
    with st.spinner("Generating response..."):
        response_placeholder = st.empty()
        async for response in generate_response(full_prompt):
            response_placeholder.write(response)

def run_async_query(prompt_text):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_async_llm(prompt_text))
    except Exception as e:
        logger.error(f"Error running async query: {e}")
        st.error("An error occurred while processing your request.")
    finally:
        loop.close()

# Tabs for Different Features
tab1, tab2, tab3 = st.tabs(["🔎 Ask Expert", "📚 Summarize Papers", "🧠 Explain Concept"])

with tab1:
    st.header("🔎 Ask Expert (with Context)")
    user_query = st.text_input("Enter your query about Computer Science:", key="expert_query")
    if st.button("Get Expert Answer", key="expert_button"):
        if user_query.strip():
            try:
                papers = search_papers(user_query)
                context = generate_context_summary(papers)
                final_prompt = f"Context:\n{context}\n\nQuestion: {user_query}"
                run_async_query(final_prompt)
            except Exception as e:
                logger.error(f"Error processing expert query: {e}")
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a question.")

with tab2:
    st.header("📚 Summarize Uploaded Paper or Text")
    uploaded_file = st.file_uploader("Upload a .txt or .pdf file for summarization", type=["txt", "pdf"])
    manual_text = st.text_area("Or paste your custom text here:", key="manual_text")

    if st.button("Summarize Text", key="summarize_button"):
        text_to_summarize = ""
        if uploaded_file is not None:
            try:
                if uploaded_file.type == "text/plain":
                    text_to_summarize = uploaded_file.read().decode("utf-8")
                elif uploaded_file.type == "application/pdf":
                    pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
                    for page in pdf_reader.pages:
                        text_to_summarize += page.extract_text() or ""
                    if not text_to_summarize.strip():
                        st.warning("No text could be extracted from the PDF.")
                logger.info("Successfully extracted text from uploaded file")
            except Exception as e:
                logger.error(f"Error processing uploaded file: {e}")
                st.error(f"Error processing file: {e}")
        elif manual_text.strip():
            text_to_summarize = manual_text.strip()

        if text_to_summarize:
            final_prompt = f"Summarize the following text in 150 words:\n\n{text_to_summarize}"
            run_async_query(final_prompt)
        else:
            st.warning("Please upload a file or paste some text first.")

with tab3:
    st.header("🧠 Explain Any Concept Clearly")
    concept_query = st.text_input("Enter the concept you want explained (e.g., Neural Networks):", key="concept_query")
    if st.button("Explain Concept", key="explain_button"):
        if concept_query.strip():
            final_prompt = f"Explain the following computer science concept simply:\n\n{concept_query}"
            run_async_query(final_prompt)
        else:
            st.warning("Please enter a concept.")
