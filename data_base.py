import pandas as pd
#to connect mysql and python we need to install mysql-connector
"""
To install connector use this command 
    COMMAND : pip install mysql-connector-python
"""
import mysql.connector as msql
from mysql.connector import Error

class dboperations:
    """
    class-name: dboperations
    description: This class is used to send the data from csv file to mysql database
    """
    def insertion_of_data(self):
        """
        Method-name: insertion of data
        Description: Method is used to connect mysql, to create database, and to insert the data into mysql

        written by : Mallela Divya
        """
        #loading file into the dataframe
        Data = pd.read_csv('E:\python assignment\processed_data.csv')
        try:
            #connecting to the mysql
            '''
            to connect we need to give the following parameters in connect() function
            ->host="your localhost"
            ->user="user-name"
            ->password="your mysql password"
            Please change these parameters when you run this program in your local system
            '''
            conn = msql.connect(host='localhost', user='root',
                            password='mysql', use_pure=True)
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE python_fin_test")
                print("python database is created")
        except Error as e:
            print("Error while connecting to MySQL", e)
        try:
            #connecting to database
            #to connect database we need to mention database name
            conn = msql.connect(host='localhost',
                           database='python_fin_test', user='root',
                           password='mysql', use_pure=True)
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                cursor.execute('DROP TABLE IF EXISTS processed_data;')
                print('Creating table....')
                #query for creating the table named processed_data
                query = "CREATE TABLE processed_data(date VARCHAR(25),high VARCHAR(25),low VARCHAR(25), " \
                        "ClosePrice VARCHAR(25),trade VARCHAR(25),turnover_in_lakhs VARCHAR(25)," \
                        "contracts VARCHAR(25),difference VARCHAR(25))"
                cursor.execute(query)
                print("iris table is created....")
                #reading data from dataframe
                for i, row in Data.iterrows():
                    #insert command to insert data into the database
                    sql = "INSERT INTO python_fin_test.processed_data(date,high,low,ClosePrice,trade," \
                          "turnover_in_lakhs,contracts,difference) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql, tuple(row))
                    print("Record inserted")
                    # the connection is not auto committed by default, so we
                    #must commit to save our changes
                    conn.commit()
            conn.close() #to close database connection
        except Error as e:
            print("Error while connecting to MySQL", e)