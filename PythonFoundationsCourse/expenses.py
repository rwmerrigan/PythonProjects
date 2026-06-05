
expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum with a for loop
# sum = 0
# for x in expenses:
#     sum += x

total = sum(expenses)

# able to set the separater (sep) to the character specified, in this case 
# we want an empty string that has no characters, in essence specifying 
# no space
print('You spent $', total, sep = '')