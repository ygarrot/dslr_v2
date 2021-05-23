def mean_normalization(x, mean=False, std=False):
    mean = mean if mean is not False else x.mean()
    std = std if std is not False else x.std()
    return (x - mean) / std

def rescaling(x, min_x=False, max_x=False):
    min_x = min_x if min_x is not False else x.min()
    max_x = max_x if max_x is not False else x.max()
    return ((x - min_x) / (max_x - min_x))

def reverse_rescaling(x, min_x=False, max_x=False):
    min_x = min_x if min_x is not False else x.min()
    max_x = max_x if max_x is not False else x.max()
    return (x * (max_x - min_x) - min_x)

