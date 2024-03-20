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
    
    return f, pre_score, re_score
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

data2 = pd.read_csv("Data/Data3.csv")
target_y2 = pd.read_csv("Data/Credit_card_label.csv")

data2 = data2.astype(float)
y_true2 = data2["label"]
feature2 = data2.drop(["Ind_ID","label"], axis=1)
feature2 = feature2.rename(columns={"Annual_income":"income", "owner_0":"owner_no", "owner_1":"owner_yes"})
#print(feature2)

data_numeric = pd.read_csv("Data/Data2.csv")
data_numeric = data_numeric.astype(float)
#features = data_numeric.drop(['核卡狀況', "每月信用卡支出平均"], axis=1)#收支比,每月信用卡支出平均
#features = data_numeric.drop(['card','expenditure'], axis=1)
features = data_numeric[["income", "age_18~30", "age_30~50", "age_50~", "owner_no", "owner_yes", "dependents_0~1", "dependents_1~"]]
y_true = data_numeric['card']
#y_true = data_numeric['核卡狀況']
#print(features)

res_feature = pd.concat([features, feature2], axis=0)
res_true = pd.concat([y_true, y_true2], axis=0)


X_train, X_test, y_train, y_test = train_test_split(res_feature, res_true, test_size=0.2)
GR = LogisticR(learning_rate=0.030999999999999996, iter= 940)
#GR.fit(X_train, y_train)
#pre = GR.predict(X_test)
#sc = GR.score(X_test,y_test)
#print(sc)


score = []
fscore_db = []
pre_db = []
re_db = []

test_iters = 100
for i in tqdm(range(test_iters)):
    GR = LogisticR(learning_rate=0.030999999999999996, iter=720)
    GR.fit(X_train, y_train)
    pre = GR.predict(X_test)
    sc = GR.score(X_test,y_test)
    score.append(sc)
    f, pre_score, re_score = matrix(y_test, pre)
    fscore_db.append(f)
    pre_db.append(pre_score)
    re_db.append(re_score)
    #print(f"Precision: {pre_score}")
    #print(f"Recall: {re_score}")
    #print(f"f-measure: {f}")

all_score = pd.DataFrame({"score":score, "Precision":pre_db, "Recall":re_db, "f_measure":fscore_db})
all_score.describe().to_csv("Data/all_score_describe3.csv")

from matplotlib import pyplot as plt

plt.plot(np.arange(1,test_iters+1), all_score.iloc[:,0], label="Score", color="#00ffc8")
plt.axhline(y=all_score.iloc[:,0].mean(), linestyle="--", color="#00ffc8")
plt.plot(np.arange(1,test_iters+1), all_score.iloc[:,1], label="Precision", color="#a6cfff")
plt.axhline(y=all_score.iloc[:,1].mean(), linestyle="--", color="#a6cfff")
plt.plot(np.arange(1,test_iters+1), all_score.iloc[:,2], label="Recall", color="#ffc9f5")
plt.axhline(y=all_score.iloc[:,2].mean(), linestyle="--", color="#ffc9f5")
plt.plot(np.arange(1,test_iters+1), all_score.iloc[:,3], label="F_measure", color="#FF3333")
plt.axhline(y=all_score.iloc[:,3].mean(), linestyle="--", color="#FFD7AF")
plt.xlabel("Number of iterations")
plt.ylabel("Score")
plt.xlim([0,test_iters+1])
plt.ylim([0.0,1.00])
plt.yticks(np.arange(0.0, 1.05, 0.05))
plt.legend()
#plt.show()
plt.savefig("Data/score3.png")


#parameter={"learning_rate":[i for i in np.arange(0.001,0.1,0.01)], "iter":[i for i in np.arange(100,1000,10)]}
#gs = GridSearch(LogisticR, "LogisticR", parameter)
#gs.fit(X_train,y_train, X_test, y_test)

#Best Parameters: {'learning_rate': 0.030999999999999996, 'iter': 940}
#{'learning_rate': 0.030999999999999996, 'iter': 720}


"""
LG2 = LogisticRegression()
LG2.fit(X_train,y_train)
pre2 = LG2.predict(X_test)
matrix(y_test, pre2)
"""