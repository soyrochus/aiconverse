# aiconverse/ui.py

def get_user_prompt() -> str:
    """
    Prompt the user and return their input as a string.
    For single-prompt usage, just read one line of input.
    For a REPL session, this can be repeatedly called in a loop.
    """
    return input("You: ")

def display_ai_response(response: str):
    """
    Print the AI's response to the console.
    """
    print(f"AI: {response}")
