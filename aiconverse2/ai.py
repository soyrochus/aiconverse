# aiconverse/ai.py

import os
from langchain_openai import ChatOpenAI
import openai
from dotenv import load_dotenv
from jinja2 import Template
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def load_openai_key():
    """
    Load the OPENAI_API_KEY from the environment.
    """
    load_dotenv()  # Loads variables from .env if present
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    return key

def create_prompt_from_template(template_path: str, user_prompt: str) -> str:
    """
    Load a Jinja template from file and render it with the user_prompt variable.
    """
    with open(template_path, "r", encoding="utf-8") as f:
        template_text = f.read()
    jinja_template = Template(template_text)
    rendered_prompt = jinja_template.render(user_prompt=user_prompt)
    return rendered_prompt

def get_ai_response(rendered_prompt: str) -> str:
    """
    Use Langchain’s LLMChain with an OpenAI model to generate a response.
    Adjust model_name to the specific model (e.g., 'gpt-4').
    """
    # Use the environment variable for the key
    openai.api_key = load_openai_key()

    # Build a Langchain PromptTemplate and LLMChain
    # prompt_template = PromptTemplate(
    #     input_variables=[],
    #     template=rendered_prompt
    # )
    llm = ChatOpenAI(
        temperature=0.7,
        model_name="gpt-4o"  # or "GTP-40" if using a custom alias
    )
    #chain = LLMChain(llm=llm, prompt=prompt_template)
    #response = chain.run({})

    response = llm.invoke(rendered_prompt).content
    return response
