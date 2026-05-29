from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> float | int:
    """Multiply tow numbers"""
    return a * b


print(multiply.invoke({"a": 3, "b": 5}))

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(multiply.args_schema.model_json_schema())
