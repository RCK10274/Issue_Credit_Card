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

#-----------------------------------------------------------------------------#
'''進行資料處理工程'''
df = df[df["年齡"]>17]
df["年齡"] = df["年齡"].astype(int)






print(df.head())
TrainData = df
TrainData.to_csv('New_DataSet.csv', index=False)


















































