"""Entry point for the Python Foundations demo project."""

from calculations import calculate_decades_and_years
from formatting import format_age_report
from types_demo import parse_age_text, run_shell_demo



def run_age_in_decades_once(input_func=input, output_func=print):
    # TODO: Task 4.3 - Run one age-in-decades interaction
    # Hint: Prompt, parse, calculate, format, and print; on bad input, print a friendly error
    try:
        raw_age = input_func("How old are you? ")
        age = parse_age_text(raw_age)
        decades, years = calculate_decades_and_years(age)
        report = format_age_report(age, decades, years)
        output_func(report)
        return report
    except ValueError:
        message = "Please enter a whole number age."
        output_func(message)
        return message



def handle_menu_choice(choice, input_func=input, output_func=print):
    # TODO: Task 5.2 - Dispatch menu choices in the script
    # Hint: Choice '1' should run the demo, choice '2' should run the age calculator
    return None



def main():
    print("Python Foundations Demo")
    print("1. Shell-style variables and types demo")
    print("2. Age in decades calculator")
    choice = input("Choose an option: ").strip()
    handle_menu_choice(choice)



if __name__ == "__main__":
    main()
