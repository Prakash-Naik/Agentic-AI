

#Ollama takes only text input Not python dict
#so convert prompt list of dictionary to string format

def str_prompt(conversation):
    prompt_str = ""

    #intial Prompt conversion to string
    for msg in conversation:
        role = msg["role"]
        content = msg["content"]
        prompt_str += f"{role}: {content}\n"

    #addding Assistant role to prompt after every conversion
    prompt_str += "Assistant :"

    return prompt_str

