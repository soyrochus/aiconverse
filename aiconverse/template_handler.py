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


from jinja2 import Template

def load_template(template_path):
    """Load the prompt template from the file."""
    
    if template_path:
        
        with open(template_path, 'r') as file:
            return file.read()
     
    else: 
        return """You are an AI assistent. You are an expert in the topic the user requests info about.
Respond concisely but completely without leaving detail. Explain the "why" of your choices.
This is the user prompt: 

{{ user_prompt }}

"""

        raise FileNotFoundError(f"Template file '{args.template}' does not exist.")

def render_template(template_content, variables):
    """Render the template with the provided variables."""
    template = Template(template_content)
    return template.render(**variables)
