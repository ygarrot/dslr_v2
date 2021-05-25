import numpy as np
import pandas as pd
import argparse
from Ft_array import *
from logistic_regression import MyLR

def mean_normalization(x):
    ret = (x - np.mean(x)) / np.std(x)
    return ret

def normalize_features(x):
    for e in x:
        x[e] = mean_normalization(x[e])
    return x

DEFAULT_SAVED_FILE = ".thetas"

def model_training(x, y, house_name):
    print("training : {}".format(house_name))
    theta = np.zeros(x.shape[1] + 1)
    lr = MyLR(theta, 0.1, 2000)
    y = np.array(y[...] == house_name).astype(float)
    lr.fit(x, y)
    print(lr.theta)
    return lr

# accept = ["Herbology", "Ancient Runes", "Astronomy"]
CLASSES = "Hogwarts House"

def train(path):
    data_train = pd.read_csv(path).dropna()

    y = data_train[CLASSES]
    x = data_train.select_dtypes(exclude=['object']).dropna()

    houses_name = pd.unique(y)

    x = normalize_features(x)
    thetas = [model_training(x, y, house).theta for house in houses_name]
    np.savetxt(".thetas", np.array(thetas))

    print("train has been done!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, default="./dataset_train.csv", help="dataset_train.csv")
    args = parser.parse_args()

    train(args.path)

if __name__ == '__main__':
    main()
