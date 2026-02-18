import prompt_building
import call_llm
import parsing
import tool_call

def run_agent(task):
    # Step 1: build the conversation history as a list
    conversation = []
    system_prompt = "You are a helpful assistant that provides accurate and concise answers to user queries."
    conversation.append({"role": "system", "content": system_prompt})
    conversation.append({"role": "user", "content": task})

    while True:
        # Step 2: convert conversation to string prompt
        prompt_str = prompt_building.str_prompt(conversation)

        # Step 3: call the LLM with the prompt string
        response = call_llm.call_llm(prompt_str)

        # Step 4: parse the response
        parsed_response = parsing.parse_response(response)

        # Step 5: Check for tool call and execute if needed.
        if parsed_response[0] == "TOOL":
            tool_name = parsed_response[1]
            tool_args = parsed_response[2]

            tool_result = tool_call.call_tool(tool_name, tool_args)

            # Add LLM's response and tool result to conversation for better context.
            conversation.append({"role": "assistant", "content": response})
            conversation.append({"role": "tool", "content": f"TOOL_RESULT = {tool_result}"})

        elif parsed_response[0] == "FINAL":
            final_answer = parsed_response[1]
            print(f"Final Answer : {final_answer}")
            return final_answer

        else:
            conversation.append(
                {"role": "system",
                 "content": "Invalid format, strictly follow the format TOOL=tool_name ARGS=arguments or FINAL=final_answer"}
            )
