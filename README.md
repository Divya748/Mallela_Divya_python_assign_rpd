
## Instructions to execute this project

1. clone the repository
2. create new environment
3. install the required libraries using requirements.txt
- command to install libraries in requirements.txt
  >pip install -r requirements.txt
4. Go to data_base.py file change \'**username**\' and \'**password**\' for mysql connection
5. Run main.py file


## Files_Description
1. preprocessing.py
    * This file is made 
        * To read csv file named HDFCBANK_01-01-2021_27-09-2021.csv
        * To reanme the columns 
        * To add a new column
        * To save the file with name \'processed_data\'
        * To find the correlation of the \'processed_data\'
2. data_base.py
    * This file is used to perform mysql database operations to insert the data from \'processed_data.csv\' file to \'MYSQL\' database
