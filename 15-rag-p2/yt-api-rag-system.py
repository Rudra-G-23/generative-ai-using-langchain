from dotenv import load_dotenv
from langchain_classic.prompts import PromptTemplate
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_classic.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.runnables.passthrough import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi

load_dotenv()

# Step 1(a) - Indexing (Docs Ingestion)
video_id: str = "Gfr50f6ZBvo"  # only the ID, not full URL
yt_api_instance = YouTubeTranscriptApi()

try:
    transcript_list = yt_api_instance.fetch(video_id)

    transcript = " ".join(chunk.text for chunk in transcript_list)

    print(f"{'--' * 25} Transcript {'--' * 25}")
    print(transcript)
    print("---" * 100)

except TranscriptsDisabled:
    print("No captions available for this video.")

# Step - 1(b) - Text Splitting
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

print(f"{'--' * 25} Chunks {'--' * 25}")
print(len(chunks))
print(chunks)


# Step 1(c) - Embedding Generation & Vector Store

huggingface_embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vector_store = FAISS.from_documents(
    documents=chunks, embedding=huggingface_embedding_model
)

print(f"{'--' * 25} Vector Store {'--' * 25}")
print(vector_store.index_to_docstore_id)


vector_store.get_by_ids(["2436bdb8-3f5f-49c6-8915-0c654c888700"])
print("--" * 100)


# Step 2 - Retrieval
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

print(f"{'--' * 25} Retriever {'--' * 25}")
print(retriever)

print(f"{'--' * 25} 1st Questions answer {'--' * 25}")
print(retriever.invoke("what is deepmind"))

# Step 3 - Augmentation

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables=["context", "question"],
)

question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs = retriever.invoke(question)

print(f"{'--' * 25} 2nd Question Answer {'--' * 25}")
print(retrieved_docs)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

print(f"{'--' * 25} Context {'--' * 25}")
print(context_text)

final_prompt = prompt.invoke({"context": context_text, "question": question})

print(f"{'--' * 25} Final Prompt {'--' * 25}")
print(final_prompt)


answer = model.invoke(final_prompt)
print(f"{'--' * 25} 3rd Question Answer {'--' * 25}")
print(answer.content)
print("---" * 100)

# Building Chain


def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text


parallel_chain = RunnableParallel(
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
    }
)

print(f"{'--' * 25} 4th question answer {'--' * 25}")
print(parallel_chain.invoke("who is Demis"))

parser = StrOutputParser()

main_chain = parallel_chain | prompt | model | parser

print(f"{'--' * 25} Summary {'--' * 25}")
print(main_chain.invoke("summary of this video"))
print("--" * 100)
