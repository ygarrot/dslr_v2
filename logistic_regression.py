import numpy as np

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
