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



   



#test()
X, y, data = main_p()

#G = GaussianNaiveBayes()
#G.fit(X,y)

def PlotGaussian(mean0, std0, label, color, X):
    sigma = np.sqrt(std0)
    #x = np.linspace(mean0 - 3*sigma, mean0 + 3*sigma, 100)#隨機從中取100個值當變量 根據三西格瑪原則
    X = np.sort(X[(X>=(mean0-3*sigma)) & (X<=(mean0+3*sigma))])

    #1/(std*根號(2pi))*(自然數)**((-1/2)*((x-mean)/std)**2)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((X - mean0)/ sigma) ** 2)#高斯分布
    
    plt.plot(X, y, label=f'{label}', color=color)

plt.figure(figsize=(5, 10))
plt.subplot(3, 1, 1)
PlotGaussian(data["reports"][data["card"]==1].mean(), data["reports"][data["card"]==1].std(), 'reports When card==1', 'red', data["reports"])
PlotGaussian(data["reports"][data["card"]==0].mean(), data["reports"][data["card"]==0].std(), 'reports When card==0', 'blue', data["reports"])

plt.title('reports')
plt.xlabel('reports Value')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(3, 1, 2)
PlotGaussian(data["age"][data["card"]==1].mean(), data["age"][data["card"]==1].std(), 'age When card==1', 'red', data["age"])
PlotGaussian(data["age"][data["card"]==0].mean(), data["age"][data["card"]==0].std(), 'age When card==0', 'blue', data["age"])
plt.title('age')
plt.xlabel('age Value')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(3, 1, 3)
PlotGaussian(data["income"][data["card"]==1].mean(), data["income"][data["card"]==1].std(), 'income When card==1', 'red', data["income"])
PlotGaussian(data["income"][data["card"]==0].mean(), data["income"][data["card"]==0].std(), 'income When card==0', 'blue', data["income"])
plt.title('income')
plt.xlabel('income Value')
plt.ylabel('Probability Density')
plt.legend()

plt.tight_layout()
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=1, hspace=1)
plt.show()
#plt.savefig(r"D:\Github\Issue_Credit_Card\PlotGaussian.png")