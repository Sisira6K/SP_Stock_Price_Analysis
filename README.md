# S&P Stock Data Analysis

## Purpose

This repository is demonstrated for CODE:YOU Data Analysis Capstone Project.I am using Python built in sqlite3 library to connect to a sqlite database. I am executing in JupyterNotebook through Pandas DataFrame and also Using Matplotlib and Seaborn for charting and Visualizations.

## Summary

This Project focuses on the technical analysis on moving average(SMA) and volume.

## Getting the Data

This dataset with historical stock prices for all companies currently found on the S&P 500 index .This data is presented from [Kaggle.com](https://www.kaggle.com/datasets/camnugent/sandp500)
csv_data folder has multiple csv files .I have created a utility script for working with multiple csv files and database.
1.create_db_from_csv.py
--This script recreates a database and loads the csv data into it so you can work on database using SQLite
(this is first requirement)

## To Run Project

1. Clone the repo to your machine.
2. Create and activate a virtual environment "See the Virtual Environment section for more instructions" and install the packages in requirements.txt file.
3. Run the create_db_from_csv.py script .This script will create a new connection database file
   'stockprice.db'
4. Open _Stockprice_Analysis.ipynb_ JupyterNotebook and install  "Python 3 ipykernel" .
5. click on 'Run All' cells

## Virtual Environment

1. After you have cloned the repo to your machine, navigate to the project folder in GitBash/Terminal.
2. Create a virtual environment in the project folder.  *python3 -m venv venv*
3. Activate the virtual environment.  *venv/Scripts/activate*
4. Install the required packages.  *pip install -r requirements.txt*
5. When you are done working on your repo, deactivate the virtual environment. *deactivate*

## Features

1. Set up a local database and read data in with SQLite
2. Clean your data and perform a SQL join with your data sets using the pandas Python library.
3. Make matplotlib and seaborn visualizations to display your data.
4. Utilize a virtual environment and include instructions in your README.md file.


