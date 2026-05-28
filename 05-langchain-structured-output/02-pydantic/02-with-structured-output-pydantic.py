import os
from typing import Literal, Optional

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OLLAMA_API_KEY")


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes in the review list"
    )
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return the sentiment of the review"
    )
    pros: Optional[list[str]] = Field(
        default=None, description="Write down 2 positive point mention in the review"
    )
    cons: Optional[list[str]] = Field(
        default=None, description="Write down 2 negative point mention in the review"
    )
    name: Optional[str] = Field(
        default=None, description="Write the name of the reviewer"
    )


model = ChatOpenAI(
    model="cogito-2.1:671b",
    openai_api_base="https://ollama.com/v1",
    max_completion_tokens=256,
    temperature=0,
)

user_review = """

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

prompt = f"""
You MUST return valid JSON ONLY.
No markdown.
No explanation.
No extra text.

JSON schema:
{{
  "key_themes": string[],
  "summary": string,
  "sentiment": "pos" | "neg",
  "pros": string[] | null,
  "cons": string[] | null,
  "name": string | null
}}

Review:
{user_review}
"""

response = model.invoke(prompt)
review = Review.model_validate_json(response.content)

print(review)
print("-" * 100)
print(review.model_dump())
