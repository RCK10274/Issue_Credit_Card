import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import product

class GridSearch:
    def __init__(self, model, model_str, param_grid):
        self.model = model
        self.param_grid = param_grid
        self.best_params = {}
        self.best_score = -np.inf
        self.model_name = model_str
        
    def fit(self, X_train, y_train, X_test, y_test):
        param_combinations = list(product(*self.param_grid.values()))
 
        for combination in tqdm(param_combinations, desc=f"GridSearch-{self.model_name}"):
            params = dict(zip(self.param_grid.keys(), combination))

            LR = self.model(**params)
            LR.fit(X_train, y_train)
            score = LR.score(X_test, y_test)

            if score > self.best_score:
                self.best_score = score
                self.best_params = params
        res = pd.DataFrame({"Best Score":self.best_score, "Best Parameters":self.best_params})
        res.to_csv("Best_Parameters.csv")