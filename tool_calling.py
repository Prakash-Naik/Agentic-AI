def build_prompt(conversation):
    prompt = ""
    for msg in conversation:
        prompt += f"{msg['role'].upper()}: {msg['content']}\n"
    return prompt + "ASSISTANT:"

def calculator(expression: str):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

def reverse_text(text: str):
    return text[::-1]

def count_chars(text: str):
    return str(len(text))


def run_tool(name, arg):
    if name == "calculator":
        return calculator(arg)
    elif name == "reverse_text":
        return reverse_text(arg)
    elif name == "count_chars":
        return count_chars(arg)
    else:
        return "Unknown tool"


def call_llm(prompt: str) -> str:
    import subprocess
    response = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt.encode(),
        capture_output=True
    )
    return response.stdout.decode().strip()

def is_valid(response):
    response = response.strip()
    if response.startswith("TOOL=") and "\nARGS=" in response:
        return True
    if response.startswith("FINAL="):
        return True
    return False


def agent_loop(user_msg):
    conversation = [
        {        
        "role": "system",
        "content": ("You are an AI agent that must choose the next action.\n"
                    "Available actions:\n"
                    "1) CALL calculator\n"
                    "2) CALL reverse_text\n"
                    "3) CALL count_chars\n"
                    "4) FINISH\n"

                    "Rules:\n"
                    "- Reply with ONLY the action number.\n"
                    "- Do NOT explain.\n"
                    "- Do NOT write sentences."
                    )
        },
    
        {"role": "user", "content": user_msg}
    ]

    while True:
        prompt = build_prompt(conversation)
        response = call_llm(prompt)

        print(f"\nLLM Response:\n{response}")

        if not is_valid(response):
            print("[Invalid format — asking model to correct]")
            conversation.append({
                "role": "system",
                "content": "Invalid format. Follow the OUTPUT RULES exactly."
            })
            continue

        if response.startswith("TOOL="):
            lines = response.splitlines()
            tool_name = lines[0].split("TOOL=")[1].strip()
            argument = lines[1].split("ARGS=")[1].strip()

            print(f"\n[Using Tool: {tool_name}({argument})]")

            result = run_tool(tool_name, argument)

            print(f"[Tool Result: {result}]")

            # Add assistant tool request
            conversation.append({"role": "assistant", "content": response})

            # Add tool result
            conversation.append({
                "role": "system",
                "content": f"Tool {tool_name} returned: {result}.  Use this result to continue solving task."
            })

        else:
            print("\nFinal Answer:", response)
            break


agent_loop(" count Number of chars in  the word hyderabad and Reverse")



