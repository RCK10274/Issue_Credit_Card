import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class GaussianNaiveBayes:
    def __init__(self, priors=None, var_smoothing=1e-9):
        self.priors = priors #對每個特徵做機率比較, 先驗概率
        self.var_smoothing = var_smoothing
    
    def fit(self,X,y):
        self.means = {}
        self.stds = {}
        self.class_priors = {}
        
        uni_y = np.unique(y)
        uni_y_counts = len(np.unique(y))#分類的數量 (分類類別總數/分母)
        features_counts = X.shape[1]#特徵的數量 

        for cls in uni_y:#讀取目標唯一值
            X_cls = X[y==cls]#讀取當下迴圈的y==cls的所有特徵
            self.means[cls] = X_cls.mean(axis=0)#存取字典{目標唯一值:唯一值的平均值}
            self.stds[cls] = X_cls.std(axis=0)#存取字典{目標唯一值:唯一值的標準差}
            self.class_priors[cls] = X_cls.shape[0] / y.shape[0]#存取字典{目標唯一值:唯一值總數量/y總數量(概率)}
            #Step2 : 計算P(y1),P(y2),........,P(yn)

        #Step3 : 分別計算P(a1|y1),P(a2|y1)...P(am|y1)、P(a1|y2),P(a2|y2)...P(am|y2)、.......、P(a1|yn),P(a2|yn)...P(am|yn)


    def predict(self, X):
        predictions = []
        for x in X:
            class_probabilities = {}
            for cls, _ in self.means.items():
                prior = np.log(self.class_priors[cls])
                class_conditional = np.sum(np.log(self.probability_density(cls, x)))
                class_probabilities[cls] = prior + class_conditional

            predictions.append(max(class_probabilities, key=class_probabilities.get))
        return np.array(predictions)

    
    def probability_density(self, cls, x):#高斯概率密度函數
        #1/(std*根號(2pi))*(自然數)**((-1/2)*((x-mean)/std)**2)
        mean = self.means[cls]
        std = self.stds[cls]
        numerator = np.exp(- (x - mean) ** 2 / (2 * std ** 2))
        denominator = np.sqrt(2 * np.pi * std ** 2)
        return numerator / denominator





if __name__=="__main__":
    name2 = "Data/Data2.csv"
    data2 = pd.read_csv(name2)
    target2 = data2["card"]
    feature_df2 = data2.iloc[:,1:]

    X_train, X_test, y_train, y_test = train_test_split(feature_df2, target2, test_size=0.2)
    GN = GaussianNaiveBayes()
    GN.fit(X_train, y_train)
    print(GN.predict(X_test))