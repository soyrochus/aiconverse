# aiconverse/main.py

import sys
from aiconverse2.cmdline import parse_args
from aiconverse2.ui import get_user_prompt, display_ai_response
from aiconverse2.ai import create_prompt_from_template, get_ai_response

def main():
    try:
        args = parse_args()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    template_path = args.template

    # Simple loop for single prompts or a REPL. 
    # You could also accept a command-line argument to do "single-prompt" or "repl".
    while True:
        user_input = get_user_prompt()
        if not user_input.strip():
            print("Empty input detected. Exiting.")
            break

        # Render the prompt
        rendered_prompt = create_prompt_from_template(template_path, user_input)

        # Get AI response
        try:
            response = get_ai_response(rendered_prompt)
        except Exception as e:
            print(f"Error communicating with AI: {e}")
            break

        # Display AI response
        display_ai_response(response)

        # Optionally, ask user if they want to continue or not
        # For a single-prompt mode, you could simply exit here if needed:
        # break

if __name__ == "__main__":
    main()
