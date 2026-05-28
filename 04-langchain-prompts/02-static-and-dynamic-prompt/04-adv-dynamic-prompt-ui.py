# Two update from the 03-prompt-generator.py
# 1. Remove the template
# 2. Rather than calling two time invoke we used chain

from pathlib import Path

import streamlit as st
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import load_prompt
from transformers import pipeline

BASE_DIR = Path(__file__).resolve().parent
template = load_prompt(BASE_DIR / "template.json")

hf_pipe = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small",
)
llm = HuggingFacePipeline(pipeline=hf_pipe)

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
    paper_content = attention_file_path.read_text(encoding="utf-8")
else:
    paper_content = bert_file_path.read_text(encoding="utf-8")

style_input = st.selectbox(
    label="Select the explaination style", options=["Beginner", "Technical"]
)

length_input = st.selectbox(
    label="Select the explanation length", options=["Short", "Medium"]
)

# Chain for the both template and the llm
chain = template | llm

if st.button("Summarize"):
    response = chain.invoke(
        {
            "paper_input": paper_input,
            "paper_content": paper_content,
            "style_input": style_input,
            "length_input": length_input,
        }
    )

    st.subheader("Summary")
    st.write(response)
