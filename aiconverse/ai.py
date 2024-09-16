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


class AIConverse:
    def __init__(self):
        # Initialize the OpenAI chat model with the asynchronous interface
        self.llm = ChatOpenAI(
            model="gpt-4o"
        )  # Optionally incorporate config system - temperature=0.7,  openai_api_key=os.getenv("OPENAI_API_KEY"))

    async def send(self, prompt):
        # Send the prompt using the asynchronous OpenAI chat model
        return await self.llm.ainvoke(prompt)
