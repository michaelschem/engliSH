import os
import asyncio
import time
import openai

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion

openai.api_key = os.environ.get('OPENAI_API_KEY')

class GPTCompleter(Completer):
    def get_completions(self, document, complete_event):
        # print(self, document, complete_event)

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Give me some mac bash that will {document.text}. Only provide the code, not the prompt.",
            max_tokens=1024,
            n=3,
            stop=None,
            temperature=0.5,
        )
        options = set([choice["text"].replace('\n', '') for choice in response["choices"]])
        options = [Completion(option, start_position=-len(document.text)) for option in options]
        # yield Completion('completion3', start_position=-5)
        return options

while True:
    session = PromptSession(completer=GPTCompleter(), complete_while_typing=False)
    result = session.prompt('> ')
    # print(result)
    os.system(result)
