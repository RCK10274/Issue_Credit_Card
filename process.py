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


def main_p():

    data = pd.read_csv("AER_credit_card_data.csv")

    data['card']=data["card"].map({"yes":1, "no":0})
    data["selfemp"]=data['selfemp'].map({"yes":1, "no":0})
    data["owner"]=data['owner'].map({"yes":1, "no":0})
    
    y = data['card']  # 目標列
    X = data.drop(columns="card", axis=1)  # 特徵
    
    return X, y, data

def main_t_B(X, y):

    #分割資料
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    Gaussian_model=GaussianNB() 
    Gaussian_model.fit(X_train, y_train)
    print(Gaussian_model.score(X_test, y_test))

    Multinomial_model=MultinomialNB() 
    Multinomial_model.fit(X_train, y_train)
    print(Multinomial_model.score(X_test, y_test))
    
    Bernoulli_model=BernoulliNB() 
    Bernoulli_model.fit(X_train, y_train)
    print(Bernoulli_model.score(X_test, y_test))

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

def DecisionTree(X,y):#decision tree

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    decison_tree = DecisionTreeClassifier()
    decison_tree.fit(X_train,y_train)
    pre = decison_tree.predict(X_test)
    matrix(y_test,pre)
    




X, y, data=main_p()
#print(data)
#main_t_B(X,y)
Table(data)
#DecisionTree(X, y)