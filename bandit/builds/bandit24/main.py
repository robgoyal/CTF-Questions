#!/usr/bin/python3

import click
import secrets
import string

@click.command()
@click.argument("length", default=12, required=False)
@click.option("--special-chars", default=string.punctuation, help="Special characters to use in password as a single string. If set to None, no special characters are used.]", required=False)
def generate_password(length, special_chars):
    """Simple program that generates a password with N characters with or without special characters."""

    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits

    if special_chars ==  "None":
        alphabet = letters + digits
    elif special_chars:
        alphabet = letters + digits + special_chars
    
    print(''.join([secrets.choice(alphabet) for i in range(length)]))

if __name__ == "__main__":
    print(generate_password())
