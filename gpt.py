#!/bin/python3
import openai
import os
import colorama
from colorama import Fore, Back, Style
import requests

# Clear screen -wanted by tetra
print("\033c")

# Check for update notification disabled
config_file = os.path.expanduser('~/.config/cli-gpt.conf')
with open(config_file, 'r') as f:
    for line in f:
        if line.startswith('UPDATE_NOTIFICATION='):
            update_notification = line.strip().split('=')[1]
            break

# check value
if update_notification == "false":
    nothing="true"
else:
    # Define directory
    CLI_GPT_DIRECTORY = os.path.expanduser("~/CLI-GPT")

    def is_git_repository():
        return os.path.exists(os.path.join(CLI_GPT_DIRECTORY, ".git"))


    def get_latest_commit_hash():
        url = f"https://api.github.com/repos/TETRA326/CLI-GPT/commits/main"
        response = requests.get(url)
        latest_commit_hash = response.json()["sha"]
        return latest_commit_hash


    def check_for_updates():
        if not is_git_repository():
            print(Fore.YELLOW + "WARNING: something went wrong (git repo not found)" + Style.RESET_ALL)
            return

        latest_commit_hash = get_latest_commit_hash()
        current_commit_hash = os.popen(f'cd {CLI_GPT_DIRECTORY} && git rev-parse HEAD').read().strip()
        if latest_commit_hash != current_commit_hash:
            print(Fore.RED + Style.BRIGHT + "NOTICE: " + Style.NORMAL + "An update is available. Run " + Fore.YELLOW + Style.BRIGHT + "gpt-update" + Fore.RED + Style.NORMAL + " to get the latest features." + Style.RESET_ALL)

    check_for_updates()

print(Fore.BLUE + "Commands:")
print(Style.BRIGHT + "exit" + Style.NORMAL + "  [quit, x, q]    - quit conversation")
print(Style.BRIGHT + "clear" + Style.NORMAL + "                 - clear the screen")
print(Style.BRIGHT + "log" + Style.NORMAL + "   [history]       - shows the previous messages in the conversation"  + Style.RESET_ALL)
print(Fore.CYAN + "Tip: You can copy using 'CTRL + SHIFT + C' and paste using 'CTRL + SHIFT + V'" + Style.RESET_ALL)

# Set up OpenAI API key
openai.api_key = ""

# Initialize history
history = []

# Tone and writing style
tone=" "
writingstyle=" "
tone_desc="Default"
style_desc="Default"

# Define function to retrieve bot response
def get_bot_response(prompt, history):
    # Append user prompt to history
    history.append({"user": prompt})

    # Generate response based on concatenated prompt and history
    prompt = "\n".join([f"{h['user']}\n{h.get('bot', '')}" for h in history])
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=tone+writingstyle+prompt,
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
    if user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "x" or user_input.lower() == "q":
        break
    elif user_input.lower() == "clear":
        print("\033c")
        history.append({"user": user_input})
    elif user_input.lower() == "log" or user_input.lower() == "history":
        for x in range(len(history)):
            print(history[x])
    else:
        # Get bot response
        bot_response = get_bot_response(user_input, history)

        # Print bot response
        print(Back.GREEN + "ChatGPT:" + Style.RESET_ALL + Fore.GREEN, bot_response + Style.RESET_ALL)
