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
from sklearn.linear_model import LogisticRegression



def Table(df):

    df['LogIncome'] = np.log1p(df['income'])
    df['LogExpenditure'] = np.log1p(df['expenditure'])
    df['LogMonths'] = np.log1p(df['months'])
    df['LogActive'] = np.log1p(df['active'])
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


import numpy as np


class LogisticR:
    def __init__(self) -> None:
        pass

    def sigmoid(self,z):#定義邏輯回函數
        return 1 / (1 + np.exp(-z))#g(z) = 1/(1+e^-z)

    def predict(self, features, weights, bias):
        """
        features: 特徵
        weights: 權重
        bias: 偏至
        """
        z = np.dot(features, weights) + bias#(Θ0 + Θ1*w1 + Θ2*w2 + Θn*wn)
        return self.sigmoid(z)#回傳邏輯回歸假設函數

    def compute_loss(self,true, pred):#計算損失函數
        m = len(true)
        loss = -(1/m) * np.sum(true * np.log(pred) + (1 - true) * np.log(1 - pred))
        return loss

    # 定义梯度下降函数
    def gradient_descent(self,features, y_true, weights, bias, learning_rate):
        """
        features: 特徵
        y_true: 真實預測值
        weights: 權重
        bias: 偏至
        learning_rate: 學習速率
        """
        m = len(y_true)
        y_pred = self.predict(features, weights, bias)
        
        dw = (1/m) * np.dot(features.T, (y_pred - y_true))
        db = (1/m) * np.sum(y_pred - y_true)
        
        weights -= learning_rate * dw
        bias -= learning_rate * db
        
        return weights, bias




data_numeric = pd.read_csv("Data/Data2.csv")
data_numeric = data_numeric.astype(float)

# 初始化权重和偏置
np.random.seed(0)  # 确保可复现性
weights = np.random.rand(data_numeric.shape[1] - 1)  # 不包括目标变量
bias = np.random.rand()
# 演示更新一次权重和偏置
features = data_numeric.drop('card', axis=1).values
y_true = data_numeric['card'].values
learning_rate = 0.01

# 更新权重和偏置
weights, bias = gradient_descent(data_numeric.iloc[:,1:], data_numeric.iloc[:,0], weights, bias, learning_rate)

# 输出更新后的权重和偏置

#print(weights , bias)
    
    
X_train,  X_test, y_train, y_test = train_test_split(data_numeric.iloc[:,1:], data_numeric.iloc[:,0], test_size=0.2)

LG = LogisticRegression()
LG.fit(X_train,y_train)
print(LG.score(X_test,y_test))