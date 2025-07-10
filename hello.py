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

conn = duckdb.connect()
cur =  conn.cursor()

cur.sql(query())

cur.sql(query1())

list_ = [10*i for i in range(1,37)]
results = [('BUDGET_LINE', 'BUDGET', 'Income', 'Expense')]
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
df.to_excel(results_path, index=False)
