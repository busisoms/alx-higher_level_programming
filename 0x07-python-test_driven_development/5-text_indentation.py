#!/usr/bin/python3

# prints a text with 2 new lines after each of these characters: ., ? and :


def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    formatted_text = ""

    # Initialize a flag to track whether a newline has been added
    newline_added = False

    for index, char in enumerate(text):

        if char in ['.', '?', ':']:
            formatted_text += char + '\n\n'
            newline_added = True

        elif char == ' ' and newline_added:
            continue

    elif char == ' ':
        formatted_text += char
        newline_added = False
        # If the character is not a whitespace, set the newline flag to False
    else:
        formatted_text += char
        newline_added = False

        if index == len(text) - 1:
            if char not in ['.', '?', ':']:
                formatted_text = formatted_text[:-2]

    print(formatted_text)
