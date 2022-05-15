"""
排序模型训练
"""

from joblib import dump
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from conf import lr_model_path


def train_model():
    X, y = datasets.load_digits(return_X_y=True)
    X = StandardScaler().fit_transform(X)
    y = (y > 4).astype(int)

    lr_model = LogisticRegression(C=0.01, penalty="l1", tol=0.01, solver="saga")

    lr_model.fit(X, y)

    lr_model.score(X, y)

    dump(lr_model, lr_model_path)


train_model()
