import pandas as pd
from Ft_array import *
import sys

def describe(file, get_head=False):
    points = pd.read_csv(file).dropna()

    only_int = points.select_dtypes(exclude=['object'])
    if (get_head is True):
        only_int = only_int.head()

    count = only_int.apply(ft_count)
    std = only_int.apply(ft_std)
    std_med = only_int.apply(ft_std_mediane)
    mean = only_int.apply(ft_mean)
    median = only_int.apply(ft_median)
    first_quar = only_int.apply(ft_first_quar)
    third_quar = only_int.apply(ft_third_quar)
    median = only_int.apply(ft_median)
    min_c = only_int.apply(ft_min)
    max_c = only_int.apply(ft_max)
    mediane = only_int.apply(ft_mediane)
    mode = only_int.apply(ft_mode)

    name = ["Count",
            "Mean",
            "Std",
            "Std med",
            "Min",
            "25%",
            "50%",
            "75%",
            "Max",
            "med",
            "mode"]

    # print(only_int.describe().to_string())
    print(pd.DataFrame([count, mean, std, std_med, min_c, first_quar, median, third_quar, max_c, mediane, mode], index=name).to_string(col_space=2))

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        try:
            describe(sys.argv[1], len(sys.argv) > 2 and sys.argv[2] == "-h")
        except:
            print("error")
