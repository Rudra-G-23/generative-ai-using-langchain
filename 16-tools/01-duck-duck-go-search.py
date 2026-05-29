from langchain_community.tools import DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchResults()

result = search_tool.invoke("who is steve jobs")

print(result)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)
