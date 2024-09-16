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

import sys
from aiconverse.cli import parse_arguments
from aiconverse.ai import AIConverse
from aiconverse.template_handler import load_template, render_template

def single_prompt_mode(ai, template_content):
    user_input = input("Enter your prompt: ")
    prompt = render_template(template_content, {"user_prompt": user_input})
    response = ai.send(prompt)
    print(f"AI: {response}")

def repl_mode(ai, template_content):
    print("Entering REPL mode. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        prompt = render_template(template_content, {"user_prompt": user_input})
        response = ai.send(prompt)
        print(f"AI: {response}")

def main():
    try:
        # Parse command-line arguments
        args = parse_arguments()

        # Load the prompt template file
        template_content = load_template(args.template)

        # Initialize AI communication module
        ai = AIConverse()

        # Choose between single prompt and REPL modes
        mode = input("Choose mode: [1] Single Prompt, [2] REPL: ")
        if mode == '1':
            single_prompt_mode(ai, template_content)
        elif mode == '2':
            repl_mode(ai, template_content)
        else:
            print("Invalid option. Exiting.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
