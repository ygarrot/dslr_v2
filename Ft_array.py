import numpy as np
from feature_scaling import *
import pandas as pd

def ft_mediane(array):
    array = array.tolist()
    lena = len(array)
    array.sort()
    if (lena % 2):
        return (array[int(lena / 2)] + array[int((lena + 1) / 2)]) / 2
    return array[lena / 2]

def ft_min(array):
    # def min()
    # test = np.apply_along_axis(
    ret = False 
    for rows in array:
        ret = rows if ret is False or rows < ret else ret
    return ret

def ft_max(array):
    ret = False 
    for rows in array:
        ret = rows if ret is False or rows > ret else ret
    return ret

def ft_mode(array):
    lst = list(array.astype(int))
    return(max(lst, key=lst.count))

def ft_mean(array):
    array = array[~pd.isnull(array)]
    return sum(array) / len(array)

def ft_std_mediane(array):
    lena = len(array) - 1
    mediane = ft_mediane(array)
    return np.sqrt(((array - mediane)**2).sum() / lena)

def ft_std(array):
    lena = len(array) - 1
    mean = ft_mean(array)
    return np.sqrt(((array - mean)**2).sum() / lena)

def ft_count(array):
    return len(array)

def ft_percentile(array, percent):
   array.sort()
   n = len(array) * percent / 100
   return array[int(n)]

def ft_median(array):
    return ft_percentile(array.tolist(), 50)

def ft_first_quar(array):
    return ft_percentile(array.tolist(), 25)

def ft_third_quar(array):
    return ft_percentile(array.tolist(), 75)

def ft_normalize(array):
   return rescaling(array)

