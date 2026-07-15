import numpy as np

# Create a 1D array from integers 10-50
# range starts at 10, ends at 51 (exclusive) and steps up by 2,
# thus getting all the evens
evens = np.arange(10, 51, 2)
print(evens)

# Create a 3x3 matrix from 0-8
# reshape here takes the the 1d array created with all the values 
# and rearranges them into a 3x3 matrix, this works because the 
# original matrix has 9 values, so reshaping into a 3x3 keeps
# the 9 element structure intact
matrix_3x3 = np.arange(9).reshape(3,3)
print(f"3x3 Matrix initialized with values from 0-8:\n{matrix_3x3}")

# Create a 5x5 identity matrix
identity_5x5 = np.eye(5)
print(f"Identity matrix using np.eye() function: \n{identity_5x5}")

# Create a 1D Array from 1 - 12
one_to_twelve = np.arange(1,13)
print(f"one_to_twelve in an array {one_to_twelve}")

# Reshape one_to_twelve to a 3x4 matrix
reshaped_one_to_twelve = one_to_twelve.reshape(3,4)
print(f"Reshaped one_to_twelve \n{reshaped_one_to_twelve}")

# Get the second row of reshaped_one_to_twelve
# [1,:] : 1 means the second row, : means the whole row 
second_row = reshaped_one_to_twelve[1,:]
print(f"Second row of reshaped_one_to_twelve \n{second_row}")

# Get the last colunmn
# [:,-1] : means the whole column, -1 means the last one
last_column = reshaped_one_to_twelve[:,-1]
print(f"The last column of reshaped_one_to_twelve {last_column}")

# Get the 2x2 top-right sub-matrix
# start:stop means "start at index start and go up to, but do not include, index stop."
# [0:2,2:4] - so get the first and second row, and the 3rd and 4th columns
# x x y y
# x x y y
# x x x x (where y is what we're selecting)
top_right = reshaped_one_to_twelve[0:2,2:4]
print(f"Top right 2x2 corner of the matrix \n{top_right}")

# Convert an array of temps in f to c
# Formula is C = (F-32) * 5/9
f_temps = np.array([32, 89, 85, 46])
# Able to perform the math on all elements of the array by just using the
# array name, instead of needing to loop over a list for example and get
# each element separetely 
c_temps = (f_temps - 32) * (5 / 9)
print(f"Fahrenheit temps array: \n{f_temps}")
np.set_printoptions(precision=2) # globally set the print options for floats
print(f"Celsius temps array: \n{c_temps}")

# From a given array, extract only the numbers that are strictly greater than 15
# and are also even numbers
num_data = np.array([1, 67, 68, 70, 5, 15, 16, 9, 45, 24, 68, 0])
# A boolean mask that is used to apply a filter to all elements and 
# exclude / include them in a new array if they satisfy the boolean statement
mask = (num_data > 15) & (num_data % 2 == 0)
# Filter the num_data array using the mask
mask_filtered_data = num_data[mask]

print(f"Original Data: \n{num_data}")
print(f"Filtered (even and > 15): \n{mask_filtered_data}")

# For a 2D array of exam scores, find:
scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 80, 85]
])
#   1. The overall average score of the entire class
overall_averages = np.mean(scores)
print(f"Overall Class Average: {overall_averages:.2f}")
#   2. The average score for each student (row-wise average).
#       a. axis=1 here represents 85 + 90 + 78 = Avg, 92 + 88 + 95 = Avg etc. 
student_averages = np.mean(scores, axis=1)
print(f"Averages per student (A, B, C): \n{student_averages}")
#   3. The highest score achieved in each subject
#       a. axis=0 here means the comparison happens to the whole row,
#          meaning 85 > 92?, 92 > 70? etc. 
highest_score_per_subject = np.max(scores, axis=0)
print("Highest score per subject (Math, Science, History):", highest_score_per_subject)