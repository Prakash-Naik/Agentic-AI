def prompt_builder(user_Query):
    prompt = []

    #Add system prompt
    system_prompt = "You are a helpful assistant that provides accurate and concise answers to user queries."

    #add system prompt to prompt list.
    prompt.append({"role": "system", "content": system_prompt})

    #add user query to prompt
    prompt.append({"role": "user", "content": user_Query})

    return prompt

msg = input("Enter your query: ")


print(prompt_builder(msg))