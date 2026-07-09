"""Formatting helpers for the Python Foundations demo project."""


def describe_rectangle(rectangle, area):
    # TODO: Task 2.3 - Format a rectangle summary
    # Hint: Use the stored length and width values in a readable sentence
    length = rectangle["length"]
    width = rectangle["width"]
    return f"A rectangle with length {length} and width {width} has an area of {area}."



def format_age_report(age, decades, years):
    # TODO: Task 4.2 - Format the age report
    # Hint: Mention the original age, the number of decades, and the remaining years
    return f"You are {age} years old, or {decades} decades and {years} years."