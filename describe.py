import pandas as pd
from Ft_array import *
import sys

def describe(file, get_head=False):
    points = pd.read_csv(file).dropna()

    only_int = points.select_dtypes(exclude=['object'])
    if (get_head is True):
        only_int = only_int.head()

    functions = {
            "Count": ft_count,
            "Mean": ft_mean,
            "Std": ft_std,
            "Std med": ft_std_mediane,
            "Min": ft_min,
            "25%": ft_first_quar,
            "50%": ft_mean,
            "75%": ft_third_quar,
            "Max": ft_max,
            "med": ft_median,
            "mode": ft_mode
    }

    all_stat = [ only_int.apply(v) for (k, v) in functions.items()]
    print(pd.DataFrame(all_stat, index=functions.keys()).to_string(col_space=2))

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        try:
            describe(sys.argv[1], len(sys.argv) > 2 and sys.argv[2] == "-h")
        except:
            print("error")
