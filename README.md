# 📄🤖 PDF Insight Agent

An agentic AI app that allows you to upload a PDF and ask intelligent questions about its content. Built using LangChain, OpenAI's API, and Streamlit.

---

##  Features

- Upload any PDF file  
- Automatically extracts and splits text  
- Ask natural-language questions  
- Uses FAISS for vector similarity search  
- Powered by OpenAI GPT via LangChain

---

##  Tech Stack

- Python  
- Streamlit  
- LangChain  
- OpenAI API  
- FAISS  
- PyMuPDF  

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-insight-agent.git
cd pdf-insight-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key

Create a file:

```
.streamlit/secrets.toml
```

Paste this inside:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

---

##  Running the App

```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

##  Project Structure

```
pdf-insight-agent/
├── app.py
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml
└── utils/
    └── pdf_helper.py
```

---

##  To-Do / Ideas

- [ ] Multi-PDF support  
- [ ] PDF summarization agent  
- [ ] Citation/reference extractor  
- [ ] Download Q&A history  
- [ ] Deploy to Streamlit Cloud  

---

## License

This project is licensed under the [MIT License](LICENSE).
