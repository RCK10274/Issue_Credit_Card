import pandas as pd
import numpy as np

def main1():
    df = pd.read_csv("STOCK_DAY_ALL_20240123.csv")

    print(df.head(10))
    print("-"*30)
    print(df.head(10).describe())
    print(df.head(10).describe().loc["mean"] * df.head(10).describe().loc["count"])


def main2():
    DataFrame = pd.read_csv('insurance.csv')
    print(DataFrame)
    print('- '*30)
    print('shape: ', DataFrame.shape)
    print('- '*30)
    print('dtypes:')
    print(DataFrame.dtypes)
    print('- '*30)
    print('value_counts():')
    print(DataFrame.dtypes.value_counts())
    print('- '*30)
    print('describe():')
    print(DataFrame.describe())
    print('- '*30)
    print('info():')
    print(DataFrame.info())

def main3():
    DataFrame = pd.read_csv('insurance.csv')
    print(DataFrame.dtypes)
    print('- '*30)
    print('查看sex欄位的包含哪些型別')
    print(DataFrame['sex'].apply(type).unique())

def main4():
    '''
    請使用醫療保險金資料集資料集
    將sex欄位中不是female、male的資料刪除
    '''
    df = pd.read_csv('D:/git/105714234/insurance.csv')
    
    new_df = df.drop(df[(df["sex"]!='female') & (df["sex"]!='male')].index)
    print(new_df)
if __name__=="__main__":
    #main1()
    #main2()
    #main3()
    main4()






