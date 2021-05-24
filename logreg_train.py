import numpy as np
import pandas as pd
import argparse
from Ft_array import *

def mean_normalization(x):
    ret = (x - np.mean(x)) / np.std(x)
    return ret

def normalize_features(x):
    for e in x:
        x[e] = mean_normalization(x[e])
    return x

class MyLR():
    def __init__(self, theta, alpha=0.001, n_cycle=1000):
        self.theta = theta
        self.alpha = alpha
        self.n_cycle = n_cycle

    def add_intercept(self, x):
        return np.c_[np.ones(x.shape[0]), x]

    def sigmoid(self, x):
        ret = 1 / (1 + np.exp(-x))
        return ret

    def cost_(self, y_hat, y, eps=1e-15):
        return -(((y @ np.log(y_hat + eps)) + ((1 - y) @ np.log(1 - y_hat + eps))) / y.shape[0])

    def predict_(self, x):
        return self.sigmoid(self.add_intercept(x) @ self.theta)

    def hypothesis(self, x):
        return self.sigmoid(x @ self.theta)

    def fit(self, x, y):
        x_prime = self.add_intercept(x)
        for _ in range(self.n_cycle):
            predict = self.hypothesis(x_prime)
            nabla = (x_prime.T @ (predict - y)) / y.shape[0]
            self.theta -= self.alpha * nabla

def model_training(x, y, house_name):
    print("training : {}".format(house_name))
    theta = np.zeros(x.shape[1] + 1)
    lr = MyLR(theta, 0.1, 2000)
    y = np.array(y[...] == house_name).astype(float)
    lr.fit(x, y)
    return lr

def train(path):
    ignore = ["Index", "Hogwarts House", "First Name", "Last Name", "Birthday", "Best Hand"]
    accept = ["Herbology", "Ancient Runes", "Astronomy"]
    classes = "Hogwarts House"
    data_train = pd.read_csv(path).dropna()

    y = data_train[classes]
    x = data_train[accept].dropna(how='all')

    houses_name = pd.unique(y)

    x = normalize_features(x)
    all_classes = [model_training(x, y, house) for house in houses_name]

    # for elem in all_classes:
    #     print(elem.theta)
    data_test = pd.read_csv("dataset_test.csv")
    # x_test = data_test.drop(columns = ignore).dropna()
    # x_test = data_test[accept]
    x_test = x
    predict = [lr.predict_(normalize_features(x_test)) for lr in all_classes]

    predict = np.array(predict).T
    y_predict = np.argmax(predict, axis=1)
    house_predict = [houses_name[index] for index in y_predict]

    # compare = np.concatenate((y_test, y_predict), axis=1)
    # compare = pd.dataframe(compare.astype("int64"))
    # print(pd.dataframe(compare.astype("int64")))

    unique, counts = np.unique(house_predict == y, return_counts=True)
    print(dict(zip(unique, counts)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default="./dataset_train.csv", help="dataset_train.csv")
    args = parser.parse_args()

    # try:
    train(args.path)
    # except:
    #     print("Error")

if __name__ == '__main__':
    main()
