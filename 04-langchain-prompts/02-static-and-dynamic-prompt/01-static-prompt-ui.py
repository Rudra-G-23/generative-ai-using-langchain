import streamlit as st
from transformers import pipeline

pipe = pipeline("text-generation", model="distilbert/distilgpt2", max_new_tokens=32)

st.header("🔬 Research Tool")

user_input = st.text_input("Enter your question")

if st.button("Generate"):
    if user_input:
        result = pipe(user_input)
        st.write(result[0]["generated_text"])
