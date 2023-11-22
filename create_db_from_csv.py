'''Click Run to create stockprice database'''

import os
import pandas as pd
import sqlite3

input_path = r"C:\Users\kbala\OneDrive\Documents\Projects\SP_Stock_Price_Analysis\csv_data"
files_in_path = os.listdir(input_path)

#Create and connect to Sqlite database
connection = sqlite3.connect('stockprice.db')

#Creating table names from csv folder
for tableName in files_in_path:
    tableName = tableName[:-4]
    
# Creating the tables into our database through SQLite connection 
    df = pd.read_csv(input_path+"\\"+tableName+".csv")
    df =df.reset_index()
    df =df.drop('index',axis=1)
    df.to_sql(tableName,connection,if_exists="replace")
    
# Close the connection
connection.close()