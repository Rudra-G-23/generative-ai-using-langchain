import os

from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
os.getenv("GROQ_API_KEY")

model1 = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)
model2 = ChatGroq(model="llama-3.1-8b-instant", max_tokens=100)

prompt1 = PromptTemplate(
    template="User will provide you the text you give me the summary \n {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 3 Questions & Answer \n {text}", input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge this provided and quiz into a single docs \n notes -> {note} \n quiz -> {quiz}",
    input_variables=["note", "quiz"],
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {"note": prompt1 | model1 | parser, "quiz": prompt2 | model2 | parser}
)

# Prompt 3 we can send to any of two model because it merge already
merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
"Vivekananda" redirects here. For other uses, see Swami Vivekananda (disambiguation).
"Narendranath Dutta" redirects here. For Indian physician, see Narendra Nath Dutta.
Swami
Vivekananda
Svāmī Vivekānanda
Black and white image of Vivekananda, facing left with his arms folded and wearing a turban
Vivekananda in Chicago, September 1893. In note on the left Vivekananda wrote: "One infinite pure and holy – beyond thought beyond qualities I bow down to thee".[1]
Personal life
Born	Narendranath Datta 
12 January 1863
Calcutta, Bengal Presidency, British India
(present-day Kolkata, West Bengal, India)
Died	4 July 1902 (aged 39)
Belur Math, Bengal Presidency, British India
(present-day West Bengal, India)
Citizenship	British subject
Era	Modern philosophy
19th-century philosophy
Region	Eastern philosophy
Indian philosophy
Alma mater	University of Calcutta (BA)
Signature	
Religious life
Religion	Hinduism
Founder of	
Ramakrishna Mission (1897)
Ramakrishna Math
Philosophy	Advaita Vedanta[2][3]
Rāja Yoga[3]
School	
VedantaYoga
Lineage	Daśanāmi Sampradaya
Religious career
Guru	Ramakrishna
Disciples
Influenced by
Quotation
"Arise, awake, and stop not till the goal is reached"
(more on Wikiquote)

Swami Vivekananda (/ˈswɑːmi ˌvɪveɪˈkɑːnəndə/)[a] (12 January 1863 – 4 July 1902), born Narendranath Datta,[b] was an Indian Hindu monk, philosopher, author, religious teacher, and the chief disciple of the Indian mystic Ramakrishna.[4][5] Vivekananda was a major figure in the introduction of Vedanta and Yoga to the Western world,[6][7][8] and is credited with raising interfaith awareness and elevating Hinduism to the status of a major world religion.[9]

Vivekananda showed an early inclination towards religion and spirituality. At the age of 18, he met Ramakrishna and became his devoted disciple, and later took up the vows of a sannyasin (renunciate). Following Ramakrishna’s death, Vivekananda travelled extensively across the Indian subcontinent as a wandering monk, gaining first-hand knowledge of the often harsh living conditions endured by the Indian masses under then British India, he sought a way to alleviate their suffering by establishing social services but lacked capital. In 1893, he travelled to the United States to participate in the Parliament of the World's Religions in Chicago, where he delivered a landmark speech beginning with the words "Sisters and brothers of America...". His powerful message introduced Hindu spiritual thought and advocated for both religious tolerance and universal acceptance.[10][11] The speech made a profound impression; an American newspaper described him as "an orator by divine right and undoubtedly the greatest figure at the Parliament".[12]

Following his success in Chicago, Vivekananda lectured widely across the United States, the United Kingdom, and continental Europe, disseminating the essential principles of Hindu philosophy. He established the Vedanta Society of New York and the Vedanta Society of San Francisco (now the Vedanta Society of Northern California),[13] both of which became the foundations for later Vedanta Societies in the West. In India, he founded the Ramakrishna Math, a monastic order for spiritual training, and the Ramakrishna Mission, dedicated to social services, education, and humanitarian work.[7]

Vivekananda is widely regarded as one of the greatest modern Indian thinkers. He was a prominent philosopher, social reformer, and the most successful proponent of Vedanta philosophy abroad. He played a crucial role in the Hindu revivalist movement and contributed significantly to the rise and development of Indian nationalism in colonial India.[14] Celebrated as a patriotic saint, his birth anniversary is observed in India as National Youth Day.[15][16]
"""


response = chain.invoke({"text": text})
print(response)

chain.get_graph().print_ascii()
