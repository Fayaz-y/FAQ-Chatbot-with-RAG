from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2:3b")

template = """
You are an exeprt in answering questions about a credit, credit score and credit card related question 

🎯 TASK:
Answer the user's question strictly based on the FAQ content above.
And make normal conversation

❗ VERY IMPORTANT RULES:
- If the answer exists in the FAQ, respond with the exact meaning (you may rephrase).
- Do NOT add extra information not present in the FAQ.
- If the answer is NOT found in the FAQ, reply: 
  "This information is not available in the current FAQ."

Here are some answer: {answer}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"answer": reviews, "question": question})
    print(result)