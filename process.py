import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB      
from sklearn.naive_bayes import MultinomialNB     
from sklearn.naive_bayes import BernoulliNB 
from fastai.tabular.all import *
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# 信用不良紀錄： 4點以下
# 年齡：青壯年族群
# 年收入： 33,000上下
# 信用卡消費金額: 大於5元
# 信用卡支出占比: 大於1%
# 是否擁有房地產: 有
# 是否非自顧人士: 否
# 扶養人數: 0~1人
# 居住時間: 1~5年
# 主卡數量: 擁有1張以上信用卡
# 活躍信用帳戶數量: 7個上下

def matrix(true, pre):#混淆矩陣
    confusion_mat = confusion_matrix(true, pre)
    tn, fp, fn, tp = confusion_mat.ravel()
    f = metrics.f1_score(true, pre)
    print(f"True Negatives: {tn}")
    print(f"False Positives: {fp}")
    print(f"False Negatives: {fn}")
    print(f"True Positives: {tp}")
    print(f"f-measure: {f}", f)


def DataProcess(path):

    data = pd.read_csv(path)
    check_null = np.sum(data.isnull(), axis=0)#確認沒有缺失值
    #print(check_null)
    data = data.drop(data[data["age"]<18].index, axis=0)
    data["reports"] = data.loc[:,"reports"].apply(lambda x: "less than 4" if x < 4 else "equal and greater then 4")
    one_hot_rep = pd.get_dummies(data["reports"], prefix="reports")#---------------------
    
    data['age'] = data['age'].astype(float)
    def age(row):
        if row>=18 and row<30:
            return "18~30"
        elif row>=30 and row<50:
            return "30~50"
        elif row>=50:
            return "50~"
    data['age']=data['age'].apply(age)
    one_hot_age = pd.get_dummies(data["age"], prefix="age")#------------------------
    #print(np.sort(data["age"].unique()))

    def ceiling_floor(df, column_name):
        Q1 = df[column_name].quantile(0.25)
        Q3 = df[column_name].quantile(0.75)
        IQR = Q3 - Q1
        lower_limit = Q1 - 1.5 * IQR
        upper_limit = Q3 + 1.5 * IQR
        max_d = df.loc[df[column_name] <= upper_limit, column_name].max()
        min_d = df.loc[df[column_name] >= lower_limit, column_name].min()
        df.loc[df[column_name] < lower_limit, column_name] = min_d
        df.loc[df[column_name] > upper_limit, column_name] = max_d
        return df
    data = ceiling_floor(data, 'income')
    data = ceiling_floor(data, 'expenditure')
    data = ceiling_floor(data, 'share')

    def z(row):#極值正規化
        return (row-row.mean())/row.std()
    data["income"] = z(data["income"])
    data["expenditure"] = z(data["expenditure"])

    one_hot_owner = pd.get_dummies(data["owner"], prefix="owner")#------------------------
    one_hot_selfemp = pd.get_dummies(data["selfemp"], prefix="selfemp")#------------------------
    
    def dep(row):
        if row==0 or row==1:
            return "0~1"
        else:
            return "1~"
    data["dependents"] = data["dependents"].apply(dep)
    one_hot_dep = pd.get_dummies(data["dependents"], prefix="dependents")#------------------------
    
    def mon(row):
        if row<50:
            return "~50"
        elif row<50 and 60<row:
            return "50~60"
        else:
            return "60~"
    data["months"] = data["months"].apply(mon)
    one_hot_mon = pd.get_dummies(data["months"], prefix="months")#------------------------
    
    def mc(row):
        if row>=1:
            return ">=1"
        else:
            return "0"
    data["majorcards"] = data["majorcards"].apply(mc)
    one_hot_mc = pd.get_dummies(data["majorcards"], prefix="majorcards")#------------------------
    
    def active(row):
        if row>=7:
            return ">=7"
        else:
            return "<7"
    data["active"] = data["active"].apply(active)
    one_hot_active = pd.get_dummies(data["majorcards"], prefix="majorcards")#------------------------
    
    feature_df = data.copy()
    target = data["card"].map({"yes":True, "no":False})
    feature_df = feature_df.drop(["card", "reports", "age", "owner", "selfemp", "dependents", "months", "majorcards", "active"], axis=1)
    feature_df = pd.concat([feature_df, one_hot_rep, one_hot_age, one_hot_owner, one_hot_selfemp, 
                    one_hot_dep, one_hot_mon, one_hot_mc, one_hot_active], axis=1).reset_index()
    #-----------------------------------------------------------------------------------
    print(feature_df)
    print(target)
    return feature_df, target

def Table(df):

    df['LogIncome'] = np.log1p(df['income'])
    df['LogExpenditure'] = np.log1p(df['expenditure'])
    df['LogMonths'] = np.log1p(df['months'])
    df['LogActive'] = np.log1p(df['active'])
    #print(df.isna().sum())
    splits = RandomSplitter(seed=42)(df)
    dls = TabularPandas(
        df, splits=splits,
        procs = [Categorify, FillMissing, Normalize],
        cat_names=["owner","selfemp","majorcards"],
        cont_names=['reports', 'age', 'share', 'dependents', 'LogIncome', 'LogExpenditure', 'LogMonths', 'LogActive'],
        y_names="card", y_block = CategoryBlock(),
    ).dataloaders(path=".")
    
    learn = tabular_learner(dls, metrics=accuracy, layers=[10,10])

    learn.lr_find(suggest_funcs=(slide, valley))
    learn.fit(16, lr=0.065)

    preds, actuals = learn.get_preds()
    predictions = np.argmax(preds, axis=1)
    actuals_1d = actuals.squeeze()
    print("-"*30)
    print(actuals_1d)
    #print(predictions, actuals_1d)
    matrix(actuals_1d, predictions)


data_name ="AER_credit_card_data.csv"
DataProcess(data_name)