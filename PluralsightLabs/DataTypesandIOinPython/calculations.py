"""Calculation helpers for the Python Foundations demo project."""


def create_rectangle_variables():
    # TODO: Task 2.1 - Create rectangle variables
    # Hint: Return the exact values from the lesson as a dictionary with two keys
    rectangle_values = {
        "length": 10,
        "width": 20
    }
    return rectangle_values



def calculate_rectangle_area(length, width):
    # TODO: Task 2.2 - Calculate rectangle area
    # Hint: Use Python's multiplication operator and return the computed value
    return length * width



def calculate_decades_and_years(age):
    # TODO: Task 4.1 - Compute decades and remaining years
    # Hint: Floor division finds whole decades and modulo finds leftover years
    return (0, age)