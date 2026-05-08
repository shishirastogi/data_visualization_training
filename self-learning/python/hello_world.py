import argparse
import sys

def greet(name, enthusiastic=False):
    """A small CLI program to greet users."""
    greeting = f"Hello, {name}"
    if enthusiastic:
        greeting += "!!! Welcome to the program!"
    else:
        greeting += "."
    return greeting

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A greeting CLI tool.")
    parser.add_argument("--name", type=str, default="World", help="Name to greet")
    parser.add_argument("--enthusiastic", action="store_true", help="Add enthusiasm")
    
    args = parser.parse_args()
    print(greet(args.name, args.enthusiastic))
