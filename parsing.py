

def parse_response(response):

    #strip response for any leading/trailing whitespace, \n, \t
    response = response.strip()

    #Tools use check
    if response.startswith("TOOL=") and "\nARGS=" in response:
        lines = response.split()
        if len(lines) >= 2 and "ARGS=" in lines[1]:
            tool_name = lines[0].split("TOOL=")[1].strip()
            args = lines[1].split("ARGS=")[1].strip()
            return ("TOOL", tool_name, args)
        else:
            return ("invalid", response)
    
    #Final answer check
    if response.startswith("FINAL="):
        final_answer = response.split("FINAL=")[1].strip()
        return ("FINAL", final_answer)

    #Invalid response
    return ("invalid", response)