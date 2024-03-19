import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
from itertools import product

def matrix(true, pre):#混淆矩陣
    f = metrics.f1_score(true, pre)
    pre_score = metrics.precision_score(true, pre)
    re_score = metrics.recall_score(true, pre)
    print(f"Precision: {pre_score}")
    print(f"Recall: {re_score}")
    print(f"f-measure: {f}")

class GridSearch:
    def __init__(self, model, model_str, param_grid):
        self.model = model
        self.param_grid = param_grid
        self.best_params = {}
        self.best_score = -np.inf
        self.model_name = model_str
    def fit(self, X_train, y_train, X_val, y_val):
        param_combinations = list(product(*self.param_grid.values()))
 
        for combination in tqdm(param_combinations, desc=f"GridSearch-{self.model_name}"):
            params = dict(zip(self.param_grid.keys(), combination))

            clf = self.model(**params)
            clf.fit(X_train, y_train)
            score = clf.score(X_val, y_val)

            if score > self.best_score:
                self.best_score = score
                self.best_params = params
        print(f"Best Score: {self.best_score}")
        print(f"Best Parameters: {self.best_params}")

class LogisticR:
    def __init__(self, learning_rate=0.01, iter=10000, s=None):
        """
        learning_rate:學習率
        iter:跌代次數
        s:指定random seed
        """
        self.learning_rate = learning_rate
        self.iter = iter
        self.s = s
        self.weight = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        rng = np.random.RandomState(self.s)
        self.weight = rng.randn(n_features)
        self.bias = 0

        for _ in range(self.iter):
            y_pred = self.get_predict(X)
            dw = (1 / n_samples) * np.dot(X.T, y_pred-y)
            db = (1 / n_samples) * np.sum(y_pred - y)
            self.weight -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
        return self.weight, self.bias
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def get_predict(self, X):
        z = np.dot(X, self.weight) + self.bias
        return self.sigmoid(z)

    def predict(self, X):
        probabilities = self.get_predict(X)
        return np.array([1 if i > 0.5 else 0 for i in probabilities])

    def score(self, X, y):
        y_pred = self.predict(X)
        return np.mean(y == y_pred)

data_numeric = pd.read_csv("Data/Data1.csv")
data_numeric = data_numeric.astype(float)
features = data_numeric.drop(['核卡狀況','每月信用卡支出平均','收支比'], axis=1)
y_true = data_numeric['核卡狀況']
X_train, X_test, y_train, y_test = train_test_split(features, y_true, test_size=0.2)

GR = LogisticR(learning_rate=0.020999999999999998, iter=730)
GR.fit(X_train, y_train)
pre = GR.predict(X_test)
matrix(y_test, pre)

#gs = GridSearch(LogisticR, "LogisticR", {"learning_rate":[i for i in np.arange(0.001,0.1,0.01)], "iter":[i for i in np.arange(100,1000,10)]})
#gs.fit(X_train,y_train, X_test, y_test)
'''
LG2 = LogisticRegression()
LG2.fit(X_train,y_train)
pre2 = LG2.predict(X_test)
matrix(y_test, pre2)
'''