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
from tqdm import tqdm

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

        for _ in tqdm(range(self.iter)):
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

data_numeric = pd.read_csv("Data/Data2.csv")
data_numeric = data_numeric.astype(float)
features = data_numeric.drop(['card','share','expenditure'], axis=1)
y_true = data_numeric['card']
X_train, X_test, y_train, y_test = train_test_split(features, y_true, test_size=0.2)

#print(X_train.shape, y_train.shape)
GR = LogisticR()
GR.fit(X_train, y_train)
print(GR.score(X_test, y_test))
print(GR.weight)
print(GR.bias)
#z = features
#a = 1 / (1 + np.exp(-z))
#a = np.where(a<0.5, 0, 1)
#print(np.sum(a==0))
#print(np.sum(a!=0))
'''
X_train,  X_test, y_train, y_test = train_test_split(data_numeric.iloc[:,1:], data_numeric.iloc[:,0], test_size=0.2)
'''

#LG2 = LogisticRegression()
#print(LG2.fit(X_train,y_train))
#print(LG2.score(X_test,y_test))