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
df.drop(df[df["age"]<15].index, inplace=True)
#-----------------------------------------------------------------------------#
'''製作出信用卡核准狀況的圖例'''
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
'''年齡分布-箱型圖及分布圖'''
age_median = df["age"].median()       #中位數:31歲
age_mode = df["age"].mode().values[0] #眾數:28歲
age_mean = df["age"].mean()           #平均數33.38歲

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x=df["age"], color="skyblue", orient="h")
plt.xlabel("年齡", fontname=Font)
plt.xticks([20, 40, 60, 80])

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

plt.axvline(x=age_median, color='r', linestyle='--', ymin=(ymax - ymin) * 0.1 / (ymax - ymin), ymax=(ymax - ymin) * 0.9 / (ymax - ymin))
plt.axvline(x=age_mode, color='g', linestyle='--', ymin=(ymax - ymin) * 0.1 / (ymax - ymin), ymax=(ymax - ymin) * 0.9 / (ymax - ymin))
plt.axvline(x=age_mean, color='b', linestyle='--', ymin=(ymax - ymin) * 0.1 / (ymax - ymin), ymax=(ymax - ymin) * 0.9 / (ymax - ymin))

plt.title("年齡-箱型圖", fontname=Font)
plt.grid(axis='x')

plt.subplot(1, 2, 2)
sns.histplot(df["age"], bins=20, color="skyblue")
plt.xlabel("年齡", fontname=Font)
plt.ylabel("人數", fontname=Font)
plt.xticks([20, 40, 60, 80])
plt.yticks([0, 50, 100, 150])
plt.title("年齡分布圖", fontname=Font)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
#-----------------------------------------------------------------------------#
'''年齡與核卡關係-交叉分析長條圖'''
#df["年齡分組"] = pd.cut(df["年齡"], bins=[17, 29, 39, 49, 59, 69, 99], labels=["18~29歲", "30~39歲", "40~49歲","50~59歲", "60~69歲", "70歲以上"])
# No_counts = df[df['核卡狀況'] == 'no']['年齡分組'].value_counts()
# Yes_counts = df[df['核卡狀況'] == 'yes']['年齡分組'].value_counts()

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
'''年齡與核卡成功率關係'''
# Age_total = df["年齡分組"].value_counts()
# Card_yes = df[df['核卡狀況'] == 'yes']['年齡分組'].value_counts()

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
# '''年收入-箱型圖及分布圖'''
# income_mean = df["年收入"].mean()
# income_mode = df["年收入"].mode()
# income_median = df["年收入"].median()

# plt.figure(figsize=(10, 6))
# # # 箱型图
# plt.subplot(1, 2, 1)
# sns.boxplot(df["年收入"], color="skyblue", orient="h")
# plt.xlabel("年收入", fontname=Font)
# plt.xticks([0, 5, 10])
# plt.title("年收入-箱型图", fontname=Font)

# # # 分布图
# plt.subplot(1, 2, 2)
# plt.hist(df["年收入"], bins=30, color="skyblue", width=10)
# plt.xlabel("年收入", fontname=Font)
# plt.ylabel("人数", fontname=Font)
# plt.xticks([20, 40, 60, 80])
# plt.title("年收入分布图", fontname=Font)
# plt.grid(True)

# plt.tight_layout()
# plt.savefig("年收入-箱型图及分布图")
# plt.show()
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

