import openai
import os

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
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract bot response from OpenAI API response
    bot_response = response.choices[0].text.strip()

    # Append bot response to history
    history[-1]["bot"] = bot_response

    return bot_response


# Start conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Check for exit command
    if user_input.lower() == "exit":
        break

    # Get bot response
    bot_response = get_bot_response(user_input, history)

    # Print bot response
    print("ChatGPT: ", bot_response)
