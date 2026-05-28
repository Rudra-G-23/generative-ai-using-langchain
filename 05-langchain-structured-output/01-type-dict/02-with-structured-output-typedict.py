import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OLLAMA_API_KEY")


class Review(TypedDict):
    summary: str
    sentiment: str


model = ChatOpenAI(
    model="cogito-2.1:671b",
    openai_api_base="https://ollama.com/v1",
    # timeout=30,
    # max_retries=3,
    max_completion_tokens=32,
)

review_from_user = """ 
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking,
or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W 
fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, 
though I don't use it often. What really blew me away is the 200MP camera—the 
night mode is stunning, capturing crisp, vibrant images even in low light. 
Zooming up to 100x actually works well for distant objects,
but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. 
Also, Samsung’s One UI still comes with bloatware—why do I need five different 
Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

"""
# Don't call the model call structure model
# model = model.with_structured_output(Review)
# response = model.invoke(review_from_user)

json_guard_prompt = f"""
You MUST respond with valid JSON ONLY.
No markdown. No explanation. No extra text.

The JSON schema is:
{{
  "summary": string,
  "sentiment": "positive" | "neutral" | "negative"
}}

Review:
{review_from_user}
"""

structured_model = model.with_structured_output(Review)

response = structured_model.invoke(json_guard_prompt)

print(response)
