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

data_name ="Data/Data2.csv"
data2 = pd.read_csv(data_name)
target2 = data2["card"]
feature_df2 = data2.iloc[:,1:]
X_train, X_test, y_train, y_test = train_test_split(feature_df2, target2, test_size=0.2)

G = GaussianNaiveBayes()
G.fit(X_train,y_train)
print(G.predict(X_test))