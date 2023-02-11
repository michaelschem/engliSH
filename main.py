import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

def get_command(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )
    message = response["choices"][0]["text"]
    return message.strip('\n')

while True:
    request = input("gpt_bash: ")
    if request == "quit":
        break
    bash_command = get_command(f"Give me some mac bash that will {request}")
    print(f"Bash Command: {bash_command}")

