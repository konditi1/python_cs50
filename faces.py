""""
In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
"""
def convert(input_str):
    match input_str:
        case s if  ":)" in s:
            output = s.replace(":)", "😀")

        case s if ":(" in s:
            output = s.replace(":(", "🙁")

        case _:
            output = input_str
    print(output)

str_input = input()
convert(str_input)


