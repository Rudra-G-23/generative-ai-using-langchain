from langchain_core.prompts import PromptTemplate

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

template.save("template.json")
