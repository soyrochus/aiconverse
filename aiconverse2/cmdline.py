# aiconverse/cmdline.py

import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(
        prog="aiconverse",
        description="AI Converse Application"
    )
    parser.add_argument(
        "--template",
        default="template_plain.txt",
        help="Path to the prompt template file. Defaults to 'template_plain.txt'."
    )
    args = parser.parse_args()

    # Validate template file path
    template_path = Path(args.template)
    if not template_path.is_file():
        raise FileNotFoundError(f"Template file not found: {template_path}")

    return args
