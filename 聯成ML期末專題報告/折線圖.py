#-----------------------------------------------------------------------------#
'''導入Module'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#-----------------------------------------------------------------------------#
'''讀取CSV檔案'''
DataSet = pd.read_csv("AER_credit_card_data.csv")
df = pd.DataFrame(DataSet)
print(df.columns)
print('-'*50)
#-----------------------------------------------------------------------------#
'''資料處理'''
df.drop(df[df["age"] <15].index, inplace=True)
df["age"] = df["age"].astype(int)
df["income"] = df["income"] * 10000
df["months"] = df["months"] // 12
#-----------------------------------------------------------------------------#
'''核卡結果比率 - 圓餅圖'''#OK
plt.rcParams['font.sans-serif'] = ['SimSun']
Font = "SimSun" 
# sizes = df["card"].value_counts()
# labels = sizes.index.tolist()
# colors = ['gold', 'lightcoral']

# plt.pie(sizes, colors=colors, autopct='%1.1f%%')
# plt.title("信用卡核准比例", fontname=Font)
# plt.axis('equal')
# plt.legend(loc="upper left", labels=labels)
# plt.savefig("信用卡核准比例-圓餅圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年齡分布 - 箱型圖及分布圖'''
# age_median = df["age"].median()       #中位數:31歲
# age_mode = df["age"].mode().values[0] #眾數:28歲
# age_mean = df["age"].mean()           #平均數33.38歲
# age_Q1 = df['age'].quantile(0.25)     #Q1: 25歲
# age_Q2 = df['age'].quantile(0.5)      #Q2: 31歲
# age_Q3 = df['age'].quantile(0.75)     #Q3: 39歲

# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
# sns.boxplot(x=df["age"], color="skyblue", orient="h")
# plt.xlabel("年齡", fontname=Font)
# plt.xticks([20, 40, 60, 80])

# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()

# plt.axvline(x=age_mean, color='r', linestyle='--', ymin=(ymax - ymin) * 0.1 / (ymax - ymin), ymax=(ymax - ymin) * 0.9 / (ymax - ymin))

# plt.title("年齡-箱型圖", fontname=Font)
# plt.grid(axis='x')

# plt.subplot(1, 2, 2)
# sns.histplot(df["age"][df["card"]=='yes'], bins=20, color="skyblue")
# plt.xlabel("年齡", fontname=Font)
# plt.ylabel("人數", fontname=Font)
# plt.xticks([20, 40, 60, 80])
# plt.yticks([0, 50, 100, 150])
# plt.title("年齡分布圖", fontname=Font)
# plt.grid(axis='y')

# plt.tight_layout()
# plt.show()
#-----------------------------------------------------------------------------#
'''年齡與核卡結果關係 - 交叉分析長條圖'''#ok
df["年齡分組"] = pd.cut(df["age"], bins=[17, 29, 39, 49, 59, 69, 99], labels=["18~29歲", "30~39歲", "40~49歲","50~59歲", "60~69歲", "70歲以上"])
# No_counts = df[df['card'] == 'no']['年齡分組'].value_counts()
# Yes_counts = df[df['card'] == 'yes']['年齡分組'].value_counts()

# bar_1 = np.arange(len(No_counts))
# bar_2 = bar_1 + 0.35

# plt.figure(figsize=(10, 6))

# plt.bar(bar_1, No_counts, color='skyblue', width=0.35, label='No')
# plt.bar(bar_2, Yes_counts, color='lightcoral', width=0.35, label='Yes')
# plt.xticks(bar_1 + 0.35 / 2, No_counts.index, fontname=Font)

# plt.xlabel('年齡', fontname=Font)
# plt.ylabel('人數', fontname=Font)
# plt.title('年齡與核卡狀況關係-柱狀圖', fontname=Font)
# plt.legend()
# plt.savefig("年齡與核卡狀況關係-柱狀圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年齡與核卡結果關係 - 長條圖'''#OK
# Age_total = df["年齡分組"].value_counts()
# Card_yes = df[df['card'] == 'yes']['年齡分組'].value_counts()

# yes_rates = (Card_yes / Age_total) * 100

# plt.figure(figsize=(10, 6))
# plt.bar(yes_rates.index, yes_rates.values, width=0.5, color='red')
# #yes_rates.plot(kind='bar', color='red') 

# plt.xlabel('年齡分布', fontname=Font)
# plt.ylabel('核卡成功率 (%)', fontname=Font)
# plt.title('年齡與核卡成功率關係-長條圖', fontname=Font)

# plt.xticks(rotation=0, fontname=Font)
# plt.tight_layout()
# plt.grid(axis='y')
# plt.savefig("年齡與核卡成功率關係-長條圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年收入 - 箱型圖及分布圖'''
# income_mean = df["income"].mean()       #33.6
# income_mode = df["income"].mode()[0]    #30
# income_median = df["income"].median()   #29
# income_Q1 = (df['income']/1000).quantile(0.25)     #Q1: 22.3
# income_Q2 = (df['income']/1000).quantile(0.5)      #Q2: 29.0
# income_Q3 = (df['income']/1000).quantile(0.75)     #Q3: 49.0
# #箱型圖
# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
# sns.boxplot(df["income"]/10000, color="skyblue", orient="h")
# plt.xlabel("年收入", fontname=Font)
# plt.xticks([0, 5, 10])
# plt.title("年收入-箱型图", fontname=Font)
# plt.grid(axis='y')
# #分布圖
# plt.subplot(1, 2, 2)
# plt.hist((df["income"]/1000)[df["card"]=="yes"], bins=30, color="skyblue", width=4.5)
# plt.xlabel("年收入", fontname=Font)
# plt.ylabel("人數", fontname=Font)
# plt.xticks([20, 40, 60, 80])
# plt.title("年收入分布圖", fontname=Font)
# plt.grid(axis='y')

# plt.tight_layout()
# plt.savefig("年收入-箱型圖及分布图")
# plt.show()
#-----------------------------------------------------------------------------#
'''年收入與核卡結果關係 - 交叉分析長條圖'''
df["年收分組"] = pd.cut(df["income"]/1000, bins=[20, 39, 59, 79, np.inf], labels=["20~39K", "40~59K", "60K~79K","80K以上"])

# No_counts = df[df['card'] == 'no']['年收分組'].value_counts()
# Yes_counts = df[df['card'] == 'yes']['年收分組'].value_counts()

# bar_1 = np.arange(len(No_counts))
# bar_2 = bar_1 + 0.35

# plt.figure(figsize=(10, 6))

# plt.bar(bar_1, No_counts, color='skyblue', width=0.35, label='No')
# plt.bar(bar_2, Yes_counts, color='lightcoral', width=0.35, label='Yes')
# plt.xticks(bar_1 + 0.35 / 2, No_counts.index, fontname=Font)
# plt.grid(axis='y')
# plt.xlabel('年收入(單位:千)', fontname=Font)
# plt.ylabel('人數', fontname=Font)
# plt.title('年收入與核卡結果關係-交叉分析長條圖', fontname=Font)
# plt.legend()
# plt.savefig("年齡與核卡結果關係-交叉分析長條圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年收入與核卡結果關係 - 長條圖'''
# income_total = df["年收分組"].value_counts()
# Card_yes = df[df['card'] == 'yes']['年收分組'].value_counts()
# df['income'] = df['income']/1000

# yes_rates = (Card_yes / income_total) * 100

# plt.figure(figsize=(10, 6))
# plt.bar(yes_rates.index, yes_rates.values, width=0.5, color='red')
# #yes_rates.plot(kind='bar', color='red') 

# plt.xlabel('年收入(單位:千)', fontname=Font)
# plt.ylabel('核卡成功率 (%)', fontname=Font)
# plt.title('年收入與核卡結果關係 - 長條圖', fontname=Font)

# plt.xticks(rotation=0, fontname=Font)
# plt.yticks([20, 40, 60, 80])
# plt.grid(axis='y')
# plt.tight_layout()
# plt.savefig("年收入與核卡結果關係 - 長條圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''租屋族與買房族'''#OK
# Owner_counts = df['owner'].value_counts()

# plt.pie(Owner_counts, autopct='%1.f%%', colors=['lightcoral', 'yellow'], startangle=249)
# plt.title("租屋族與買房族人數比例 - 圓餅圖", fontname=Font)
# plt.axis('equal')
# plt.legend(loc="upper right", labels=["租屋族", "購屋族"])
# plt.savefig("租屋族與買房族人數比例 - 圓餅圖")
#-----------------------------------------------------------------------------#
'''持有房屋與核卡成功率關係'''#OK
# Owner_total = df["owner"].value_counts()
# Card_yes = df[df['card'] == 'yes']['owner'].value_counts()
# yes_rates = (Card_yes / Owner_total) * 100

# plt.bar(["租屋族", "買屋族"], yes_rates.values, width=0.5, color='red')
# plt.xlabel('租屋族群', fontname=Font)
# plt.ylabel('核卡成功率 (%)', fontname=Font)
# plt.title('持有房屋與核卡成功率關係-長條圖', fontname=Font)
# plt.xticks(fontname=Font)
# plt.yticks([20, 40, 60, 80])
# plt.tight_layout()
# plt.grid(axis='y')
# plt.savefig("持有房屋與核卡成功率關係-長條圖")
#-----------------------------------------------------------------------------#
'''創業人士及雇員的申辦者比例 - 圓餅圖'''#OK
# Selemp_conuts = df["selfemp"].value_counts()
# plt.pie(Selemp_conuts, autopct='%1.f%%', colors=['lightcoral', 'yellow'], startangle=115)
# plt.title("創業人士及雇員的申辦者比例 - 圓餅圖")
# plt.axis('equal')
# plt.legend(loc="upper right", labels=["雇員", "創業人士"])
# plt.savefig("創業人士及雇員的申辦者比例 - 圓餅圖")
#-----------------------------------------------------------------------------#
'''創業人士成功核卡率 - 長條圖'''#OK
# Selfemp_total = df["selfemp"].value_counts()
# Selfemp_yes = df[df["card"]== "yes"]['selfemp'].value_counts()
# yes_rates = (Selfemp_yes / Selfemp_total) * 100

# plt.bar(["雇員", "創業人士"], yes_rates.values, width=0.5, color='red')
# plt.xlabel("職務身份")
# plt.ylabel("核卡成功率")
# plt.tight_layout()
# plt.grid(axis='y')
# plt.savefig("職務身份與核卡成功率關係 - 長條圖")
#-----------------------------------------------------------------------------#
'''撫養人數''' 
# Dependents_median = df["dependents"].median()       #中位數:1
# Dependents_mode = df["dependents"].mode().values[0] #眾數:0
# Dependents_mean = df["dependents"].mean()           #平均數:0.99
# Dependents_Q1 = df["dependents"].quantile(0.25)    #Q1: 0
# Dependents_Q2 = df["dependents"].quantile(0.5)     #Q2: 1
# Dependents_Q3 = df["dependents"].quantile(0.75)    #Q3: 2

# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
# sns.boxplot(x=df["dependents"], color="skyblue", orient="h")
# plt.xlabel("扶養人數", fontname=Font)
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# plt.axvline(Dependents_mean, color='r', linestyle='--', ymin=(ymax - ymin) * 0.1 / (ymax - ymin), ymax=(ymax - ymin) * 0.9 / (ymax - ymin))
# plt.title("扶養人數 - 箱型圖", fontname=Font)

# plt.subplot(1, 2, 2)
# plt.hist(df["dependents"][df["card"]=='yes'], bins=15, color="skyblue", width=1.2)
# plt.xlabel("扶養人數", fontname=Font)
# plt.ylabel("信用卡申辦者人數", fontname=Font)
# plt.title("信用卡申辦者的扶養人數-分布圖", fontname=Font)
# plt.grid(axis='y')
# plt.tight_layout()
# plt.savefig("扶養人數 - 箱型圖及分布圖")
#-----------------------------------------------------------------------------#
'''扶養人數核卡率長條圖''' #OK
# Dependents_total = df["dependents"].value_counts()
# Dependents_yes = df[df["card"]== "yes"]["dependents"].value_counts()
# yes_rates = (Dependents_yes / Dependents_total) * 100

# plt.bar(Dependents_total.index, yes_rates.values, width=0.5, color='red')
# plt.xlabel("扶養人數")
# plt.ylabel("核卡成功率")
# plt.grid(axis='y')
# plt.savefig("扶養人數核卡率 - 長條圖")
#-----------------------------------------------------------------------------#
'''居住時間(Year)統計圖'''
# Months_median = df["months"].median()       #中位數:2
# Months_mode = df["months"].mode().values[0] #眾數:1
# Months_mean = df["months"].mean()           #平均數:4.3
# Months_Q1 = df["months"].quantile(0.25)    #Q1: 1
# Months_Q2 = df["months"].quantile(0.5)     #Q2: 2
# Months_Q3 = df["months"].quantile(0.75)    #Q3: 6

# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 1)
# sns.boxplot(x=df["months"], color="skyblue", orient="h")
# plt.xlabel("居住時間(單位:年)", fontname=Font)
# plt.grid(axis='x')
# plt.title("居住時間 - 箱型圖", fontname=Font)

# plt.subplot(1, 2, 2)
# plt.hist(df["months"][df["card"]=='yes'], bins=15, color="lightcoral", width=3)
# plt.xlabel("居住時間", fontname=Font)
# plt.ylabel("申辦人數", fontname=Font)
# plt.title("居住時間 -分布圖", fontname=Font)
# plt.grid(axis='y')
# plt.tight_layout()
# plt.savefig("居住時間 - 箱型圖及分布圖")
#-----------------------------------------------------------------------------#
'''居住時間與核卡率關係 - 長條圖'''
# df['居住時間分組'] = pd.cut(df['months'], bins=range(0, df['months'].max() + 6, 5), include_lowest=True, labels=[f"{i}~{i+5}" for i in range(0, df['months'].max() + 1, 5)])
# grouped_total = df.groupby('居住時間分組').size()
# grouped_yes = df[df['card'] == 'yes'].groupby('居住時間分組').size()
# grouped_yes_rates = (grouped_yes / grouped_total) * 100

# plt.figure(figsize=(10, 6))
# plt.bar(grouped_yes_rates.index, grouped_yes_rates.values, width=0.5, color='lightcoral')

# plt.xlabel('居住時間（單位:年）', fontname=Font)
# plt.ylabel('核卡率 (%)', fontname=Font)
# plt.title('居住時間與核卡率關係', fontname=Font)
# plt.grid(axis='y')

# plt.savefig("居住時間與核卡率關係-長條圖")
#-----------------------------------------------------------------------------#
'''是否擁有主卡 - 圓餅圖'''
# Majorcards_conuts = df["majorcards"].value_counts()
# plt.pie(Majorcards_conuts, autopct='%1.f%%', colors=['lightcoral', 'yellow'], startangle=156)
# plt.title("是否擁有主卡 - 圓餅圖")
# plt.axis('equal')
# plt.legend(loc="upper right", labels=["有主卡", "有主卡"])
# plt.savefig("是否擁有主卡 - 圓餅圖")
#-----------------------------------------------------------------------------#
'''是否擁有主卡與核卡率關係 - 長條圖'''
# Majorcards_total = df["majorcards"].value_counts()
# Majorcards_yes = df[df["card"]== "yes"]['majorcards'].value_counts()
# yes_rates = (Majorcards_yes / Majorcards_total) * 100  # 有主卡 79.5%  沒主卡68.5%

# plt.bar(["有主卡", "沒主卡"], yes_rates.values, width=0.5, color='red')
# plt.xlabel("是否擁有主卡")
# plt.ylabel("核卡成功率")
# plt.grid(axis='y')
# plt.savefig("是否擁有主卡與核卡率關係 - 長條圖")
#-----------------------------------------------------------------------------#
''' 活躍用戶帳戶數量 - 箱型圖及分布圖''' # 以上的圖片都以存檔

#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#

