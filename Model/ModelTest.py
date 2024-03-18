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
    def __init__(self, weight=None, bias=None, learning_rate=0.01, iter=100):
        self.weight=weight
        self.bias=bias
        self.learning_rate=learning_rate
        self.iter=iter

    def fit(self, X, y):
        self.X = X
        self.y = y
        if self.weight==None:
            self.weight = np.ones(X.shape[1])
        if self.bias==None:
            self.bias = 0

    def sigmoid(self,z):#定義邏輯回函數(閥0.5)
        return 1 / (1 + np.exp(-z))#g(z) = 1/(1+e^-z)

    def predict(self, features):
        """
        features: 特徵
        """
        z = np.dot(features, self.weights) + self.bias#(Θ0 + Θ1*w1 + Θ2*w2 + Θn*wn)
        return np.where(self.sigmoid(z)>=0.5, 1, 0)#回傳邏輯回歸假設函數

    def loss_funtion(self,true, pred):#Cost(hΘ(x),y)=-ylog(hΘ(x)-(1-y)log(1-hΘ(x)))
        m = len(true)
        loss = np.sum(true * np.log(pred) - (1 - true) * np.log(1 - pred))
        loss2 = -np.sum()#-Σ{1~i}Σ{1~c} yiclog(pre)
        return loss

    def cost_funtion(self,true, pred):#計算代價函數
        return

    def gradient_descent(self):
        """
        weights: 權重
        bias: 偏至
        learning_rate: 學習速率
        """
        m = len(self.y)
        features = self.X
        weights = self.weight
        bias = self.bias

        for _ in range(self.iter):
            y_pred = self.predict(features, weights, bias)

            #損失函數的差異
            w = (1/m) * np.dot(features.T, (y_pred - y_true))#1/m Σ{1~m} x(hΘ(x)-y)
            b = (1/m) * np.sum(y_pred - y_true)
            #更新權重與偏移
            weights -= self.learning_rate * w#Θ = Θ-learning_rate()
            bias -= self.learning_rate * b
            print(weights, bias)
            
        return weights,bias
     
    def score(self, X, y):
        y_pred = self.predict(X)
        accuracy = np.sum(y == y_pred) / len(y)
        return accuracy




data_numeric = pd.read_csv("Data/Data2.csv")
data_numeric = data_numeric.astype(float)
features = data_numeric.drop('card', axis=1).values
y_true = data_numeric['card'].values


#z = features
#a = 1 / (1 + np.exp(-z))
#a = np.where(a<0.5, 0, 1)
#print(np.sum(a==0))
#print(np.sum(a!=0))
'''
X_train,  X_test, y_train, y_test = train_test_split(data_numeric.iloc[:,1:], data_numeric.iloc[:,0], test_size=0.2)

LG = LogisticRegression()
LG.fit(X_train,y_train)
print(LG.score(X_test,y_test))
'''