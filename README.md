# FAQ-Chatbot-with-RAG

A production-ready FAQ chatbot built with Retrieval-Augmented Generation (RAG) that answers questions from a CSV dataset without hallucination. The chatbot uses local LLM (Ollama) for enhanced privacy and customization.

## Technologies Used

- **Python 3.x** - Core programming language
- **LangChain** - Framework for building LLM applications
- **Ollama** - Local LLM inference engine
  - Model: `llama3.2:3b` (Main language model)
  - Embeddings: `mxbai-embed-large` (For vector embeddings)
- **ChromaDB** - Vector database for semantic search
- **Pandas** - CSV data processing and manipulation

## Features

- Zero hallucination - Answers strictly from FAQ dataset
- Local LLM deployment for privacy
- RAG architecture for accurate retrieval
- CSV-based knowledge base
- Conversational interface
- Persistent vector storage

## Prerequisites

Before running this project, ensure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
   - Install from: https://ollama.ai
   - Pull required models:
     ```bash
     ollama pull llama3.2:3b
     ollama pull mxbai-embed-large
     ```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Fayaz-y/FAQ-Chatbot-with-RAG.git
cd FAQ-Chatbot-with-RAG
```

### 2. Create Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Project Structure

```
FAQ-Chatbot-with-RAG/
│
├── main.py                              # Main application entry point
├── vector.py                            # Vector store and retriever setup
├── requirements.txt                     # Python dependencies
├── Experian_FAQ_chatbot_dataset.csv    # FAQ dataset (CSV format)
├── chroma_langchain_db/                # Vector database storage (auto-generated)
└── README.md                            # Project documentation
```

### CSV Data File Setup

**Important:** Place your FAQ dataset CSV file in the root directory of the project.

- **Filename:** `Experian_FAQ_chatbot_dataset.csv`
- **Required CSV Format:**
  - Column 1: `question` - FAQ questions
  - Column 2: `answer` - Corresponding answers

**Example CSV structure:**
```csv
question,answer
"What is a credit score?","A credit score is a numerical representation of your creditworthiness..."
"How do I improve my credit score?","You can improve your credit score by paying bills on time..."
```

**Note:** If you want to use a different CSV file:
1. Update the filename in `vector.py` (line 7)
2. Ensure your CSV has `question` and `answer` columns

## Usage

### Running the Chatbot

1. Ensure Ollama is running in the background
2. Activate your virtual environment
3. Run the main script:

```bash
python main.py
```

4. Start asking questions! Type `q` to quit.

### Example Interaction

```
------------------------------------
Ask your question (q to quit): What is a credit score?

A credit score is a numerical representation...

------------------------------------
Ask your question (q to quit): q
```

## How It Works

1. **Data Loading:** FAQ data is loaded from CSV using pandas
2. **Vectorization:** Questions and answers are embedded using `mxbai-embed-large`
3. **Storage:** Embeddings are stored in ChromaDB for fast retrieval
4. **Query Processing:** User questions are vectorized and matched against stored FAQs
5. **Response Generation:** Llama 3.2 generates responses based on retrieved context
6. **Guardrails:** Strict prompting ensures answers stay within FAQ boundaries

## Configuration

### Changing the LLM Model

Edit `main.py` line 5:
```python
model = OllamaLLM(model="llama3.2:3b")  # Change to your preferred model
```

### Adjusting Retrieval Settings

Edit `vector.py` line 35:
```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Number of documents to retrieve
)
```

## Troubleshooting

**Issue:** `Ollama model not found`
- **Solution:** Run `ollama pull llama3.2:3b` and `ollama pull mxbai-embed-large`

**Issue:** `CSV file not found`
- **Solution:** Ensure `Experian_FAQ_chatbot_dataset.csv` is in the project root directory

**Issue:** `ChromaDB errors`
- **Solution:** Delete the `chroma_langchain_db` folder and restart to rebuild the vector store

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Fayaz-y

## Acknowledgments

- LangChain for the RAG framework
- Ollama for local LLM deployment
- ChromaDB for vector storage
