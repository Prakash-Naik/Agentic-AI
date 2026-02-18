
def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def reverse_text(text: str):
    return text[::-1]

def count_chars(text: str):
    return str(len(text))

def call_tool(tool_name, tool_args):
    if tool_name == "calculator":
        return calculator(tool_args)
    elif tool_name == "reverse_text":
        return reverse_text(tool_args)
    elif tool_name == "count_chars":
        return count_chars(tool_args)
    else:
        return "ERROR: Unknown tool"
