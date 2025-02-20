# AIConverse: A Python console application to interact with an AI using Langchain.
#
# Project Description: This project allows users to interact with an AI either through
# single-prompt inputs or an ongoing conversation using a REPL. It includes customizable
# prompt templates and relies on Langchain for AI communication.
#
# License: MIT License
# For the full license text, please refer to the LICENSE file in the root of the project.
#
# Copyright (c) 2024 Iwan van der Kleijn

from langchain_openai.chat_models.base import ChatOpenAI
from langchain.chains import ConversationChain
from langchain_core.runnables.history import RunnableWithMessageHistory


# A helper class implementing in‑memory history.
class InMemoryHistory:
    def __init__(self):
        self.messages = []

    async def aget_messages(self):
        #print(f"Messages: {self.messages}")
        return self.messages

    async def aadd_messages(self, messages):
        self.messages.extend(messages)
        #print(f"New Messages: {self.messages}")
    
    # This is needed to make the class callable so RunnableWithMessageHistory will
    # use the same instance for each call.    
    def __call__(self):
        return self
    

class AIConverse:
    def __init__(self, has_memory=False):
        # Initialize the OpenAI chat model with the asynchronous interface
        if has_memory:
            self.llm = RunnableWithMessageHistory(
                runnable=ChatOpenAI(model="gpt-4o"),
                get_session_history=InMemoryHistory(),
                memory_key="history",
                return_messages=True
            )
        else:
            self.llm = ChatOpenAI(
                model="gpt-4o"
            )  # Optionally incorporate config system - temperature=0.7,  openai_api_key=os.getenv("OPENAI_API_KEY"))

    async def send(self, prompt):
        # Send the prompt using the asynchronous OpenAI chat model
        return await self.llm.ainvoke(prompt)

