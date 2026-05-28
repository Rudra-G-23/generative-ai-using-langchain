from pathlib import Path

import streamlit as st
from langchain_core.prompts import PromptTemplate
from transformers import pipeline

BASE_DIR = Path(__file__).resolve().parent

pipe = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small",
)

st.header("🔬 Research Tool")

paper_input = st.selectbox(
    label="Select the Paper Name",
    options=[
        "Attention all you need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
    ],
)

attention_file_path = BASE_DIR / "attention-all-you-need.txt"
bert_file_path = BASE_DIR / "bert.txt"

if paper_input == "Attention all you need":
    with open(attention_file_path, "r", encoding="utf-8") as file:
        paper_content = file.read()
else:
    with open(bert_file_path, "r", encoding="utf-8") as file:
        paper_content = file.read()

style_input = st.selectbox(
    label="Select the explaination style", options=["Beginner", "Technical"]
)

length_input = st.selectbox(
    label="Select the explanation length", options=["Short", "Medium"]
)

template = PromptTemplate(
    template="""
    You are a good explainer. You explain research papers clearly.

    Paper name: {paper_input}
    Paper content: {paper_content}t

    Style: {style_input}
    Length: {length_input}

    Provide a clear and simple summary.
    """,
    input_variables=["paper_input", "paper_content", "style_input", "length_input"],
    validate_template=True,
)

prompt = template.invoke(
    {
        "paper_input": paper_input,
        "paper_content": paper_content,
        "style_input": style_input,
        "length_input": length_input,
    }
)

if st.button("Summarize"):
    response = pipe(prompt.to_string())
    st.write(response)
