# AIConverse

AIConverse is a Python console application designed to demonstrate the power and ease of **Prompt-Driven Development**. It allows users to interact with an AI through single-prompt inputs or via an ongoing conversation using a REPL (Read-Eval-Print Loop). The project also supports customizable prompt templates and utilizes Langchain for AI communication.

This project serves as an example of how prompt-driven engineering can shift the focus from *how* the code is written to *what* needs to be built, allowing AI to handle the technical details and empowering developers to focus on innovation and problem-solving.

## Prompt-Driven Development

Prompt-driven engineering is emerging as the next phase in design-first software development. Instead of writing traditional code, developers can provide natural language prompts that describe what they want, and AI generates the code.

With advanced large language models (LLMs) like GPT-4, Claude, or reasoning models like OpenAI's newly released o1, AI interprets prompts and turns them into actionable systems, architectures, or features. This shifts the focus from writing code to designing solutions.

**AIConverse** is a practical demonstration of how this methodology can be used to accelerate development. Designers and engineers provide high-level prompts to define their intent, while the AI handles the technical aspects.

## Features

- **Single Prompt Mode**: Interact with the AI by sending a single prompt and receiving an immediate response.
- **REPL Mode**: Maintain an ongoing conversation with the AI in a loop, allowing continuous interaction.
- **Customizable Prompt Templates**: Define prompt templates using simple text files with placeholders, filled by the user's input during runtime.
- **Modular Architecture**: Clear separation of concerns with modules for user interaction, template management, and AI communication.

## Project Structure

```bash
aiconverse/
│
├── pyproject.toml               # Poetry project file
├── LICENSE                      # License file (MIT License)
├── README.md                    # Project description and setup instructions
├── aiconverse/                  # Main Python package
│   ├── __init__.py              # Module init file
│   ├── __main__.py              # Main application entry point
│   ├── cli.py                   # Command-line parsing module
│   ├── ai.py                    # AI communication module
│   └── template_handler.py       # Template handling module
└── tests/                       # Test files
    └── test_aiconverse.py        # Unit tests
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/soyrochus/aiconverse.git
cd aiconverse
```

2. Install dependencies using Poetry:

```bash
poetry install
```

### Running the Application

AIConverse supports two modes: Single Prompt Mode and REPL Mode.

1. **Single Prompt Mode**: Allows you to send a single prompt to the AI and get a response.

2. **REPL Mode**: Engage in a continuous conversation with the AI in a loop.

To run the application, use the following command:

```bash
python -m aiconverse --template path/to/template.txt
```

- `--template` specifies the path to a prompt template file that will be used during the interaction.

Example of a template file (`template.txt`):

```bash
Hello, AI! I am {{ user_prompt }}.
```

### Modes

- **Single Prompt Mode**: Enter a prompt and receive a single response.
- **REPL Mode**: Continuous conversation until you type `exit`.

Upon running the application, you'll be prompted to choose the mode you'd like to run.

### Testing

To run tests:

```bash
poetry run pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/soyrochus/aiconverse/blob/main/LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests to improve AIConverse. Contributions are welcome!

## Author

Created by Iwan van der Kleijn, 2024.


