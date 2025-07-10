# LionsFin/main.py

import pandas as pd
import duckdb
from pathlib import Path

from helpers import query, query1, query_inc, query_bud, query_exp

# CONSTANTS
file_path = Path('data/Ledger 26.xlsx')
results_path = Path('data/trial.xlsx')
# OR
# file_path = Path('data/ADMIN Ledger 26.xlsx')

ledger = pd.read_excel(file_path, usecols="A:G")
budget = pd.read_excel(file_path, sheet_name=1)
ledger.columns = ['id','date', 'payee/from', 'check', 'amount', 'budget_line', 'budget']

conn = duckdb.connect()
cur =  conn.cursor()

# create the tables
cur.sql(query())
cur.sql(query1())

# create the list of budget_line
list_ = [10*i for i in range(1,37)]
results = []
for x in list_:
    if x in [60, 310]:
        continue
    row = (
        int(x),
        cur.sql(query_bud(x)).fetchall()[0][0],
        cur.sql(query_inc(x)).fetchall()[0][0],
        cur.sql(query_exp(x)).fetchall()[0][0],
    )
    results.append(row)
df = pd.DataFrame(results)
print(df.info())
print(df.head(10))
df.columns = ['budget_line', 'budget', 'income', 'expenses']
df = df.fillna(0)
print(df.head(10))
df.to_excel(results_path, index=False)
