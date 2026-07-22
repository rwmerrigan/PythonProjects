import pandas as pd
import numpy as np

# Create a data frame and then print it
student_data_frame = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [22, 25, 21, 23],
    'Score': [85.5, 90.0, 78.5, 92.0]
}

sdf = pd.DataFrame(student_data_frame)
print(sdf)

# Filter the data frame to show only the students who scored
# higher than 80 into a new data frame
high_scorers = sdf[sdf['Score'] > 80]
print(f"High scorers (<80): \n{high_scorers}")

# Average score of the students
avg_score = sdf['Score'].mean()
print(f"Average Score of Students: \n{avg_score}")

# New data set:
data = {
    'Book_ID': [101, 102, 103, 104, 105, 106],
    'Title': ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Moby Dick', 'The Hobbit', '1984'],
    'Genre': ['Classic', 'Classic', 'Sci-Fi', 'Adventure', 'Fantasy', 'Sci-Fi'],
    'Price': [10.99, 12.50, 8.99, 15.00, np.nan, 8.99], # Note the NaN value and duplicate
    'Quantity_Sold': [15, 22, 40, 8, 12, 40]
}

bdf = pd.DataFrame(data)

# Check for and drop duplicates (keeps the first occurence)
bdf = bdf.drop_duplicates()

# Find the average price of the non-missing books
mean_price = bdf['Price'].mean()

# Fill missing values in the 'Price' column
bdf['Price'] = bdf['Price'].fillna(mean_price)
print(bdf)

# Extract a subset of the data frame containing only books with a price < 12$
# and a quantity_sold > 10
filtered_books = bdf[(bdf['Price'] < 12.00) & (bdf['Quantity_Sold'] > 10)]
print(f"Price < 12$ and quantity sold > 10: \n{filtered_books}")

# Create a new column via vectorization
bdf['Total_Revenue'] = bdf['Price'] * bdf['Quantity_Sold']
print(f"Total Revenue column added:\n{bdf}")

# Find the total Quantity_Sold and the average Price for each genre in the bookstore
genre_summary = bdf.groupby('Genre').agg({
    'Quantity_Sold': 'sum', # sum and mean are operations being performed
    'Price': 'mean'
}).rename(columns={'Quantity_Sold': 'Total_Sold', 'Price': 'Average_Price'})

print(genre_summary)