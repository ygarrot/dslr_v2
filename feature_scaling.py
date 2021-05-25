# def mean_normalization(x, mean, std):
#     return (x - mean) / std

def rescaling(x, min_x, max_x):
    return ((x - min_x) / (max_x - min_x))

def reverse_rescaling(x, min_x, max_x):
    return (x * (max_x - min_x) - min_x)

def mean_normalization(x):
    ret = (x - np.mean(x)) / np.std(x)
    return ret


def normalize_features(x):
    for e in x:
        x[e] = mean_normalization(x[e])
    return x


