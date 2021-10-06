from preprocessing import preprocess
from data_base import dboperations
import pandas as pd
import matplotlib.pyplot as plt

# object creation for preprocess class
process_data = preprocess()

# To read the file
data = process_data.file_reading()

# To rename the columns
data = process_data.col_rename(data)

# To add the columns
data = process_data.add_new_column(data)

# To save the file
saved_file = process_data.file_save(data)

# Save the data into database
# create object for database
mysql_data_base = dboperations()

#insert data
mysql_data_base.insertion_of_data()

# reading processed_data to find correlation
final_data = pd.read_csv('processed_data.csv')
#find correlation
corr_image = process_data.find_correlation(final_data)
plt.savefig('corr_matrix.png')