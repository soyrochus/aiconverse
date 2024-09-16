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


import subprocess


def run_checks() -> None:
    commands = [
        ["black", "aiconverse"],
        ["flake8", "aiconverse"],
        ["mypy", "aiconverse"],
        ["pytest"],
    ]

    for command in commands:
        result = subprocess.run(command)
        if result.returncode != 0:
            print(f"Command {command} failed with return code {result.returncode}")
            break  # Stop running the next commands if one fails


if __name__ == "__main__":
    run_checks()
