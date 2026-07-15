import numpy as np

# create a np array (able to specify data type)
a = np.array([1,2,3], dtype="int16")
# 2d array
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
# output
#[[9. 8. 7.]
#[6. 5. 4.]]
# Get dimension
print(a.ndim) # 1
print(b.ndim) # 2
print(a.shape) # (3,) meaning 1 row, 3 columns
print(b.shape) # (2,3) meaning 2 rows, 3 columns
print(a.dtype) # int64
print(a.itemsize) # size in bytes - 2 (for int16)
print(b.itemsize) # 8 bytes for float

# Access / Change Rows, Columns etc.
x = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# Get a specific element - [row,column]
# To get 13 for example:
thirteen_element = x[1,5] # uses zero based indexing for rows and columns
# can also use negtive indexing like lists
print(f"Element 13 - {thirteen_element}") # Element 13 - 13

# Get a specific row
print(f"First row of x matrix: {x[0,:]}") # First row of x matrix: [1 2 3 4 5 6 7]

# Get a specific column 
print(f"Third Column of x matrix: {x[:,2]}") # Third Column of x matrix: [ 3 10]

# Start index, get every element after in n steps
print(f"First row, start at second element, end at > 6th element, step by 2: {x[0,1:6:2]}")

# Change an element 
x[1,5] = 20
print(f"[1,5] change to {x[1,5]}")

# Change a column
x[:,2] = [1,2]
print(f"Column 3 changed to {x[:,2]}")

# 3d example
y = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(y)

# Get a 3d element y[matrix number, row number, column number]
print(f"Get element 4 - y[0,1,1] : {y[0,1,1]}")

# Change 3d version
# y[:,1,:] first colon means all the matrices in this array, 1 means the second row
# in the matrix, and the last colon means the whole row
y[:,1,:] = [[9,9],[8,8]]
print(f"Change elements using colon notation: \n{y[:,1,:]}")

# Initialize a zero matrix
zeros = np.zeros((2,3,3))
print(f"Two 3d zeros arrays \n{zeros}")

# Initialize a ones matrix
ones = np.ones((2,3,3))
print(f"Two 3d ones arrays \n{ones}")

# Initialize another number matrix
some_number = np.full((2,2), 255)
print(some_number)

# Initialize with random decimal numbers
rand_nums = np.random.rand(4,2)
print(rand_nums)

# Initialize with random Ints (low, high, size=(x,y))
rand_ints = np.random.randint(2,7, size=(3,3))
print(rand_ints)

