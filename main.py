from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
import openai
import os

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

class OpenAICompleter(Completer):
    def get_completions(self, document, complete_event):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Give me some mac bash that will {document.text}",
            max_tokens=1024,
            n=10,
            stop=None,
            temperature=0.5,
        )
        options = [choice["text"] for choice in response["choices"]]
        for option in options:
            yield Completion(option, start_position=-len(document.text))

completer = OpenAICompleter()

while True:
    request = prompt("gpt_bash: ", completer=completer)
    if request == "quit":
        break
    bash_command = get_command(f"Give me some mac bash that will {request}")
    print(f"Bash Command: {bash_command}")
