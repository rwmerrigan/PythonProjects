
#region Print Formatted List Function
def printFormattedListWithTaskInfo(passedList, taskNumber, taskStringDescriptor):
    print('Task Number - ' + str(taskNumber) + ' - ' + taskStringDescriptor)
    for i in range(len(passedList)):
        print('Element ' + str(i) + ' - ' + str(passedList[i]))
#endregion

#region Task 1: Create a list containing 5 favorite foods.
foods = ["peanut butter", "cheese", "apples", "bread", "yogurt"]
#endregion

#region Task 2: Print the first item in a list.
print(foods[0])
#endregion

#region Task 3: Print the last item.
print(foods[-1]) 
#endregion

#region Task 4: Count how many items are in a list.
print(len(foods))
#endregion

#region Task 5: Add "ice cream" to the end.
foods.append('ice cream')
printFormattedListWithTaskInfo(foods,5,'Add ice cream to the end')
#endregion

#region Task 6: Insert "salad" at index 1.
foods.insert(1, 'salad')
printFormattedListWithTaskInfo(foods,6,'Insert salad at index 1')
#endregion

#region Task 7: Remove Yogurt
foods.remove('yogurt')
printFormattedListWithTaskInfo(foods,7,'Remove yogurt')
#endregion

#region Task 8: Remove the last item
foods.pop(-1)
printFormattedListWithTaskInfo(foods,8,'Remove the last item')
#endregion

#region Task 9: Check if "pizza" exists, in keyword in this case is 
# checking if the list contains the string, simple boolean expression
print("pizza" in foods)
#endregion

#region Task 10: Loop through the list
printFormattedListWithTaskInfo(foods,10,'Print the List')
#endregion

#region Task 11: Sum Numbers
numsTask11 = [1, 2, 3, 4, 5]
print(sum(numsTask11))
#endregion

#region Task 12: Find the largest number
numsTask12 = [2, 6, 7, 3, 2, 9, 9]
print(max(numsTask12))
#endregion

#region Task 13: Find the smallest number
numsTask13 = [2, 6, 7, 3, 2, 9, 9]
print(min(numsTask13))
#endregion

#region Task 14: Count Occurences
numsTask14 = [2, 6, 7, 3, 2, 9, 9, 9]
print(numsTask14.count(9))
#endregion

#region Task 15: Find the Index of an Item
print('Index of Cheese - ' + str(foods.index('cheese')))
#endregion

#region Task 16: Reverse a List
numsTask14.reverse()
printFormattedListWithTaskInfo(numsTask14, 16, 'Reverse a List')
#endregion

#region Task 17: Sort a List
numsTask14.sort()
printFormattedListWithTaskInfo(numsTask14, 17, 'Sort a List')
#endregion

#region Task 18: Copy a List
numsCopy = numsTask14.copy()
printFormattedListWithTaskInfo(numsCopy, 18, 'Copy a List')
#endregion

#region Task 19: Concatenate Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
printFormattedListWithTaskInfo(c, 19, 'Concatenate Lists')
#endregion

#region Task 20: Clear a List
c.clear()
printFormattedListWithTaskInfo(c, 20, 'Clear a List')
#endregion

#region Task 21: Print only even numbers
numsList20 = [5, 6, 3, 4, 8, 23, 456, 32, 9, 1, 2, 2, -2, -67, -908]
for i in range(len(numsList20)):
    if numsList20[i] % 2 == 0:
        print(numsList20[i])
#endregion

#region Task 22: Print only Odd numbers
for i in range(len(numsList20)):
    if numsList20[i] % 2 != 0:
        print(numsList20[i])
#endregion

#region Task 23: Create Squares List
squares = [x**2 for x in range(10)]
printFormattedListWithTaskInfo(squares, 23, 'Create a list of Squares from 0-9')
#endregion

#region Task 24: Create Cubes List
cubes = [x**3 for x in range(10)]
printFormattedListWithTaskInfo(cubes, 24, 'Create a List of Cubes from 0-9')
#endregion

#region Task 25: Find the Average
average = sum(numsList20) / len(numsList20)
print(average)
#endregion

#region Task 26: Find the Second largest
numsList20.sort()
print(numsList20[-2])
#endregion

#region Task 27: Remove Duplicates
listToSet = list(set(numsList20))
printFormattedListWithTaskInfo(listToSet, 27, 'Remove duplicates in a List')
#endregion

#region Task 28: Count Positive and Negative Numbers
positiveCount = 0
for i in range(len(numsList20)):
    if numsList20[i] > 0:
        positiveCount += 1
print(positiveCount)

negativeCount = 0
for i in range(len(numsList20)):
    if numsList20[i] < 0:
        negativeCount += 1
print(negativeCount)
#endregion

#region Task 29: Find all Negative Numbers
negatives = [n for n in numsList20 if n < 0]
printFormattedListWithTaskInfo(negatives, 29, 'Find all Negatives')
#endregion

#region Task 30: Multiply all nums in a list 
simpleNumsList = [1, 2, 3]
multipliedListResult = 1
for n in simpleNumsList:
    print(n)
    multipliedListResult *= n
print(multipliedListResult)
#endregion

#region Task 31: Find Common Elements
a = [1, 4, 5, 6, 3, 7, 0]
b = [6, 5, 6, 5, 6, 1, 3, 0, 9, 8, 5, 4]

sharedValues = []
for x in a:
    if x in b:
        sharedValues.append(x)
a.sort()
b.sort()
sharedValues.sort()
printFormattedListWithTaskInfo(sharedValues, 31, 'Find Common Elements')
#endregion

#region Task 32: Find Difference Between Lists

#endregion