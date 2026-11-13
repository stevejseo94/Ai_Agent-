import json 
import os 
import argparse
import sys
from openai import OpenAI
from dotenv import load_dotenv
from prompts import system_prompt 
from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None: 
        raise RuntimeError("api key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1", 
        api_key=api_key, 
        )
    messages = [
        {"role": "system", "content": system_prompt}, 
        {"role": "user", "content": args.user_prompt}, 
    ]
    if args.verbose: 
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(20): 
        try: 
            final_response = generate_content(client, messages, args.verbose)
            if final_response: 
                print(f"Final Response: {final_response}") 
                return 
        except Exception as e: 
            print(f"Error in generate_content as {e}")

    print(f"Maximum iterations reached") 
    sys.exit(1)
       
def generate_content(client: OpenAI, messages: list, verbose: bool) -> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    if verbose:
        print("Prompt tokens:", response.usage.prompt_tokens)
        print("Response tokens:", response.usage.completion_tokens)

    message = response.choices[0].message
    messages.append(message) 

    if not message.tool_calls:
        return message.content

    for tool_call in message.tool_calls:
        if tool_call.type != "function": 
            continue 
        result_message = call_function(tool_call, verbose) 
        if result_message["content"] == "": 
            raise Exception("Error: content is empty")
        if verbose: 
            print(f"-> {result_message['content']}")
        messages.append(result_message) 

    return None 

if __name__ == "__main__":
    main()

