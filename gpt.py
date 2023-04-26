import openai
import os
import colorama
from colorama import Fore, Back, Style

print(Fore.CYAN + "Hint: You can copy using 'CTRL + SHIFT + C' and paste using 'CTRL + SHIFT + V'" + Style.RESET_ALL)

# Set up OpenAI API key
openai.api_key = ""

# Initialize history
history = []

# Define function to retrieve bot response
def get_bot_response(prompt, history):
    # Append user prompt to history
    history.append({"user": prompt})

    # Generate response based on concatenated prompt and history
    prompt = "\n".join([f"{h['user']}\n{h.get('bot', '')}" for h in history])
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract bot response from OpenAI API response
    bot_response = response.choices[0].text.strip()

    # Append bot response to history
    history[-1]["bot"] = bot_response

    return bot_response


# Start conversation loop
while True:
    # Get user input
    print(Back.WHITE + Fore.BLACK)
    user_input = input("You: ")
    print(Style.RESET_ALL)
    # Check for exit command
    if user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "x":
        break
    elif user_input.lower() == "clear":
        print("\033c")
        history.append({"user": user_input})
    else:
        # Get bot response
        bot_response = get_bot_response(user_input, history)

        # Print bot response
        print(Back.GREEN + "ChatGPT:" + Style.RESET_ALL + Fore.GREEN, bot_response + Style.RESET_ALL)
