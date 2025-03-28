import pandas as pd
import sqlalchemy as sal
from secret import connection 

def main():
    df = pd.read_csv('./data/netflix_titles.csv')
    engine = sal.create_engine(connection.get_connection())
    conn = engine.connect()
    df.to_sql('netflix_raw', con=conn, index=False, if_exists='append')

if __name__ == '__main__':
    main()