import pandas as pd

def query_db(query, conn):
    df = pd.read_sql_query(query, conn)
    print(df.shape)
    return df
