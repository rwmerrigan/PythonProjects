
def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in line: 
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('The acronym does not exist')

def add_acronym():
    # Ask the user what acronym they want to add
    acronym = input('What acronym do you want to add?\n')

    # Then ask the user for the definition
    definition = input('What is the definition?\n')

    # Open the file, 'a' denotes append to the file 
    # Write the new acronym and definition to the file
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()