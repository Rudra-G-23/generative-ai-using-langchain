#### Notebook

```mermaid
graph TD
    A[ Output] --> B(Unstructured Output)
    A --> C(Structured Output)
```

---

```mermaid
graph TD
    A[LLM's Output] --> B(Unstructured Output)
    A --> C(Structured Output)
    B --> |Output Parsers| C
    C --> |By Default| D(With Structured Output)
    D --> E(TypeDict)
    D --> F(Pydantic)
    D --> G(Json Schema)
```

#### Why do we need Structured Output?
- Data Extraction
- API Building
- Multi Agents

#### Few things to remember 

```mermaid
graph TD
    WSO(with_structured_output) --> |Claude, Gemini| A(json_format)
    WSO --> |OpenAI| B(function_calling)
```

#### Resources
- https://github.com/campusx-official/langchain-structured-output