import psycopg2
import pandas as pd
from io import StringIO

#Connect to postgres
conn = psycopg2.connect(
    host="localhost",
    dbname="bank_db",
    user="postgres",
    password="sm199500",
    port=5432
)
cur = conn.cursor()

#Read dataset
df = pd.read_csv("D:/Trains/bank_marketing_proj/data/input/clean_bank_dataset.csv")

#Add data to database
buffer = StringIO()
df.to_csv(buffer, index=False, header=False)
buffer.seek(0)

cur.copy_from(buffer, 'bank_marketing', sep=',')

conn.commit()

cur.close()
conn.close()

print('All data successfully added.')