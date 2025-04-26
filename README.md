#ArxivIntelBot: AI-Powered Chatbot for Research Paper Classification and Expert Insights
🚀 An intelligent chatbot designed to:

Search Computer Science research papers from arXiv.

Summarize papers for quick understanding.

Explain complex CS concepts clearly using advanced LLM models.

✨ Features
🔍 Ask Expert: Get AI-powered answers with references from academic research papers.

📚 Summarize Papers: Upload your research papers or custom text and get concise summaries.

🧠 Explain Concepts: Learn computer science topics explained simply.

🧩 Flexible Models: Choose from Llama3, Mistral, or Vicuna models (via Ollama).

🛠️ Tech Stack
Python 3.11

Streamlit

LangChain

Ollama LLM (Local models)

Multithreading for fast search

arXiv metadata JSON dataset

🚀 How to Run Locally
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/ArxivIntelBot.git
cd ArxivIntelBot
Install Required Packages:

bash
Copy
Edit
pip install -r requirements.txt
Download the Dataset:

📥 Download arXiv Metadata Dataset Here :https://drive.google.com/file/d/17_TAzEQimPfmsDoExFoRd--3XGf666IH/view?usp=drive_link

Save it to your machine.

Update the dataset path in Backend.py if needed.

Make sure Ollama is installed locally and running with models like Llama3, Mistral, or Vicuna.

Run the Streamlit App:

bash
Copy
Edit
streamlit run Frontend.py
🧩 App Structure

File	Description
Frontend.py	Main Streamlit app with 3 tabs: Ask Expert, Summarize Papers, Explain Concept
Backend.py	Functions for searching the dataset and generating context summaries
📸 Screenshot
![image](https://github.com/user-attachments/assets/ab8fd1ad-0dfc-43ee-9b64-f74b086dbe5e)
![image](https://github.com/user-attachments/assets/6b0f2631-7d8a-481b-8c66-3357dd78dda2)
![image](https://github.com/user-attachments/assets/062ee07f-6fbe-4d57-96c5-2cc9c68f5bbd)
![image](https://github.com/user-attachments/assets/cccf343f-bfdd-46e9-9b62-3a8b70d07361)


(You can add screenshots here once you take them.)

📚 Learning Outcomes
Building a real-world Retrieval-Augmented Generation (RAG) application.

Connecting local LLMs (via Ollama) into a Streamlit app.

Implementing efficient multithreaded search.

Practicing prompt engineering and streaming responses.

Developing a professional AI chatbot experience.

🙌 Acknowledgements
LangChain

Ollama

arXiv Dataset

📬 Contact
LinkedIn: Mohit Pathak

Email: your.email@example.com

