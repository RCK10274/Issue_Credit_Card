#-----------------------------------------------------------------------------#
'''導入Module'''
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------------#
'''讀取CSV檔案並轉換成DataFrame資料型態進行資料處理'''
DataSet = pd.read_csv("AER_credit_card_data.csv")
df = pd.DataFrame(DataSet)

#-----------------------------------------------------------------------------#
'''將原DataSet欄位標題轉為中文'''
df.rename(columns={"card": "核卡狀況",
                   "reports": "聯徵紀錄",
                   "age": "年齡",
                   "income": "年收入",
                   "share": "信用卡收支比",
                   "expenditure": "每月信用卡支出平均",
                   "owner": "房地產",
                   "selfemp": "創業人士",
                   "dependents": "扶養人數",
                   "months": "居住時間",
                   "majorcards": "持有主卡",
                   "active": "活躍帳戶數量",
},inplace=True)

def ceilingfloor(df, col):#天花板與地板法 IOR找出極端值
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    #極端值定義 Q1 - 1.5IQR 或是高於 Q3 + 1.5IQR 的值。
    lower_limit = Q1 - 1.5 * IQR #極端值(下限)
    upper_limit = Q3 + 1.5 * IQR #極端值(上限)

    extreme_values = df[(df[col] < lower_limit) | (df[col] > upper_limit)].index
    max = df[col].drop(index=extreme_values).max()
    min = df[col].drop(index=extreme_values).min()

    df.loc[df[col] < lower_limit, col] = min
    df.loc[df[col] > upper_limit, col] = max


    return df

print(ceilingfloor(df, "年收入")["年收入"].describe())