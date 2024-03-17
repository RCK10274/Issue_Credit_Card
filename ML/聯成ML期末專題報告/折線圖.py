#-----------------------------------------------------------------------------#
'''導入Module'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#-----------------------------------------------------------------------------#
'''讀取CSV檔案'''
DataSet = pd.read_csv("New_DataSet.csv")
df = pd.DataFrame(DataSet)
#print(df.head())
#-----------------------------------------------------------------------------#
'''製作出信用卡核准狀況的圖例'''
Font = "SimSun" 
# sizes = df["核卡狀況"].value_counts()
# labels = sizes.index.tolist()
# colors = ['gold', 'lightcoral']
# plt.pie(sizes, colors=colors, autopct='%1.1f%%')
# plt.title("信用卡核准比例", fontname=Font)
# plt.axis('equal')
# plt.legend(loc="upper left", labels=labels)
# plt.savefig("信用卡核准比例-圓餅圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年齡分布'''
# Age = df["年齡"]
# Age_mean = Age.mean()
# Age_median = Age.median()
# Age_mode = Age.mode()[0]

# plt.figure(figsize=(10, 6))
# plt.subplot(1, 2, 2)
# plt.hist(Age, bins=40, color="skyblue", edgecolor="black")
# plt.xlabel("年齡", fontname=Font)
# plt.ylabel("人數", fontname=Font)
# plt.title("年齡分布-長條圖", fontname=Font)
# plt.grid(True)

# plt.subplot(1, 2, 1)
# sns.boxplot(x="年齡", data=df, color="skyblue",)
# plt.xlabel("年齡", fontname=Font)
# plt.title("年齡分布-箱型圖", fontname=Font)
# plt.legend([f'平均數: {Age_mean:.0f}歲', 
#             f'中位數: {Age_median:.0f}歲', 
#             f'眾數: {Age_mode}歲'],)
# plt.tight_layout()
# plt.savefig("年齡分布-箱型圖及長條圖")
# plt.show()
#-----------------------------------------------------------------------------#
'''年齡與核卡關係'''
df["年齡分組"] = pd.cut(df["年齡"], bins=[17, 29, 39, 49, 59, 69, 99], labels=["18~29歲", "30~39歲", "40~49歲","50~59歲", "60~69歲", "70歲以上"])
# No_counts = df[df['核卡狀況'] == 'no']['年齡分組'].value_counts()
# Yes_counts = df[df['核卡狀況'] == 'yes']['年齡分組'].value_counts()

# bar_1 = np.arange(len(No_counts))
# bar_2 = bar_1 + 0.35

# plt.figure(figsize=(10, 6))

# plt.bar(bar_1, No_counts, color='skyblue', width=0.35, label='No')
# plt.bar(bar_2, Yes_counts, color='lightcoral', width=0.35, label='Yes')
# plt.xticks(bar_1 + 0.35 / 2, No_counts.index)

# plt.xlabel('年齡')
# plt.ylabel('人數')
# plt.title('年齡與核卡狀況關係-柱狀圖')
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

# plt.xlabel('年齡分布')
# plt.ylabel('核卡成功率 (%)')
# plt.title('年齡與核卡成功率關係-長條圖')

# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.grid(axis='y')
# plt.savefig("年齡與核卡成功率關係-長條圖")
# plt.show()

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

