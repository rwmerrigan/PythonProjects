
# Ask the user what acronym they want to add
acronym = input('What acronym do you want to add?\n')

# Then ask the user for the definition
definition = input('What is the definition?\n')

# Open the file, 'a' denotes append to the file 
# Write the new acronym and definition to the file
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')

