from sklearn.metrics import accuracy_score
from logistic_regression import MyLR
from Ft_array import *
import numpy as np
import pandas as pd
import argparse

DEFAULT_FILE = "./dataset_test.csv"
CLASSES = "Hogwarts House"

def predict(path):
    thetas = np.loadtxt(DEFAULT_SAVED_FILE)

    lr_classes = [MyLR(np.array(theta)) for theta in thetas]

    data = pd.read_csv(path)

    y = data[CLASSES]
    print(data)
    x = data.select_dtypes(exclude=['object']).dropna()

    predict = [lr.predict_(normalize_features(x)) for lr in lr_classes]
    predict = np.array(predict)
    data[CLASSES] = predict.T
    # print(predict.T)
    # unique, counts = np.unique(house_predict == y, return_counts=True)
    # print(dict(zip(unique, counts)))

DEFAULT_SAVED_FILE = ".thetas"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default=DEFAULT_FILE, help="dataset_train.csv")
    args = parser.parse_args()

    predict(args.path)

if __name__ == '__main__':
    main()
