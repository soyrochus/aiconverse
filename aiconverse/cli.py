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

# aiconverse/cli.py
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Converse Application",
        prog="aiconverse",
        epilog="Interact with an AI using single-prompt or REPL modes.",
    )
    parser.add_argument(
        "--template",
        type=str,
        default=None,
        help="Path to the prompt template file. Defaults to 'template.txt'.",
    )
    args = parser.parse_args()

    return args
