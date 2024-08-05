import numpy as np
import pandas as pd

def run():
    # Create a DataFrame with random data
    df=pd.read_csv('RESULTADOS_2024_CSV_V1.csv')
    #print(df.columns())
    #EM=df['EM'].sum()
    #NM=df['NM'].sum()
    #print(f'EM: {EM}, NM: {NM}')
    print(df.head())
    #print(df.tail())
    #print(df.groupby('EM').sum())
    #print(df.columns)
    
    
if __name__ == '__main__':  
    run() 