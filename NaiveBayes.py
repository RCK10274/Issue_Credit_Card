import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt

def main_p():
    data = pd.read_csv("AER_credit_card_data.csv")
    data['card']=data["card"].map({"yes":1, "no":0})
    data["selfemp"]=data['selfemp'].map({"yes":1, "no":0})
    data["owner"]=data['owner'].map({"yes":1, "no":0})
    y = data['card']  # 目標列
    X = data.drop(columns="card", axis=1)  # 特徵
    return X, y, data

def matrix(true, pre):#混淆矩陣
    f = metrics.f1_score(true, pre)
    print(f"f-measure: {f}")

def test():
    X, y, data=main_p()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    Gaussian_model=GaussianNB() #priors,var_smoothing
    Gaussian_model.fit(X_train, y_train)
    pre = Gaussian_model.predict(X_test)
    #print(Gaussian_model.score(X_test, y_test))
    matrix(y_test, pre)



#需要知識:高斯分布、貝是分類、
class GaussianNaiveBayes:
    def __init__(self, priors=None, var_smoothing=1e-9):
        self.priors = priors #對每個特徵做機率比較
        self.var_smoothing = var_smoothing
    
    def fit(self,X,y):
        
        ans = np.unique(y)
        ans_counts = len(np.unique(y))#分類的數量 (分類類別總數/分母)
        features_counts = X.shape[1]#特徵的數量 
        probability = np.empty([features_counts])
        #計算概率
