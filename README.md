# ArxivIntelBot: AI-Powered Chatbot for Research Paper Classification and Expert Insights
🚀 ArxivIntelBot
AI-Powered Chatbot for Research Paper Classification and Expert Insights


📋 Table of Contents
About the Project

Key Features

Tech Stack

Setup Instructions

App Structure

Learning Outcomes

Acknowledgements

Contact

License

📖 About the Project
ArxivIntelBot is an intelligent chatbot designed to enhance research and learning experiences for computer science enthusiasts.
It combines the power of retrieval-augmented generation (RAG) and local large language models (LLMs) to:

Search academic papers from the arXiv database.

Generate expert answers with referenced context.

Summarize uploaded research papers.

Explain complex computer science concepts clearly and simply.

✨ Key Features
🔍 Ask Expert: Get AI-generated answers enriched with context from real research papers.

📚 Summarize Research: Upload text or papers and receive concise 150-word summaries.

🧠 Explain Concepts: Enter any CS topic and get an easy-to-understand explanation.

🛠 Model Selection: Choose between Llama3, Mistral, or Vicuna for response generation.

⚡ Fast Dataset Search: Multithreaded searching through millions of research papers.

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python, Multithreading, Asyncio

LLM Models: Ollama (Llama3, Mistral, Vicuna)

Libraries: LangChain, Streamlit, asyncio

Dataset: arXiv Metadata Snapshot

🚀 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/ArxivIntelBot.git
cd ArxivIntelBot
2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
3. Download the Dataset
📥 Download Dataset Here

Save it locally and update the path inside Backend.py if needed.

4. Run Ollama Locally
Make sure your Ollama server is running with models like Llama3, Mistral, or Vicuna.

5. Start the Application
bash
Copy
Edit
streamlit run Frontend.py
🗂️ App Structure

File/Folder	Description
Frontend.py	Streamlit frontend - user interactions, model selection, input handling
Backend.py	Backend logic - dataset search, context generation
requirements.txt	Python dependencies

📸 Screenshot
![image](https://github.com/user-attachments/assets/ab8fd1ad-0dfc-43ee-9b64-f74b086dbe5e)
![image](https://github.com/user-attachments/assets/6b0f2631-7d8a-481b-8c66-3357dd78dda2)
![image](https://github.com/user-attachments/assets/062ee07f-6fbe-4d57-96c5-2cc9c68f5bbd)
![image](https://github.com/user-attachments/assets/cccf343f-bfdd-46e9-9b62-3a8b70d07361)

📚 Learning Outcomes
Hands-on experience building RAG (Retrieval-Augmented Generation) systems.

Streamlit development with real-time AI responses.

Using multithreading for efficient large dataset search.

Deployment and integration of local LLMs using Ollama.

Advanced prompt engineering for expert-level AI answers.

🙏 Acknowledgements
LangChain

Ollama

arXiv Dataset - Computer Science Domain

📬 Contact
Name: Mohit Pathak

LinkedIn: Mohit Pathak LinkedIn

Email: pathakmohit3666@gmail.com







