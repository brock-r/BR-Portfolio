
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# This CSV doesn't have a header so pass
# column names as an argument


# Load in the data
df = pd.read_csv(r'C:\Users\brock\OneDrive\Documents\UFC_Fight.csv')

df2 = pd.read_csv(r'C:\Users\brock\OneDrive\Documents\UFC_Fighter_Stats.csv')

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://postgres:fartsarecooL4@localhost:5432/andnewanalytics')


df.to_sql(
    'Every_Fight', 
    engine,
    index=False,
    if_exists = 'replace'
)


df2.to_sql(
    'Fighter_Profile', 
    engine,
    index=False,
    if_exists = 'replace'
)

# Save the data from dataframe to
# postgres table "iris_dataset"


print("Worked")



