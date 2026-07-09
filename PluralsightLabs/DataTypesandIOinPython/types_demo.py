"""Type and conversion helpers for the Python Foundations demo project."""

from calculations import create_rectangle_variables, calculate_rectangle_area
from formatting import describe_rectangle



def infer_number_type(value):
    # TODO: Task 3.1 - Identify int and float values
    # Hint: Check for int before float so whole numbers are reported correctly
    value_type = ""
    if isinstance(value, int):
        value_type = "int"
    elif isinstance(value, float):
        value_type = "float"
    else:
        value_type = "unknown"
    return value_type



def parse_age_text(age_text):
    # TODO: Task 3.2 - Parse age text into an integer
    # Hint: Remove surrounding spaces, convert with int(), and reject negative ages
    age_text.strip()
    age = int(age_text)
    if age < 0:
        raise ValueError
    return age



def convert_number_to_text(number):
    # TODO: Task 3.3 - Convert numbers to text for output
    # Hint: Python's built-in str() function creates a string representation
    return str(number)



def run_shell_demo(output_func=print):
    # TODO: Task 5.1 - Build a shell-style demo
    # Hint: Reuse the rectangle and type helper functions to create several output lines
    rect_dict = create_rectangle_variables()
    rect_length = rect_dict["length"]
    rect_width = rect_dict["width"]
    rect_area = calculate_rectangle_area(rect_length, rect_width)
    rect_description = describe_rectangle(rect_dict, rect_area)
    output_lines = [
        "Rectangle Descriptions (Area, Length, Width)",
        f"Rectangle Length: {rect_length}, Width {rect_width}",
        f"Rectangle Area: {rect_area}"
        f"Rectangle Length is an {infer_number_type(rect_length)} and 10.5 is a {infer_number_type(10.5)}"
        f"Rectangle Area: {rect_area}",
        rect_description
    ]
    for line in output_lines:
        output_func(line)
    return output_lines
