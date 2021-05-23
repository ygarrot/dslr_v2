import seaborn as sns
from feature_scaling import *
import matplotlib.pyplot as plt
import pandas as pd
import sys

# def slice_name(array)
#     line =
#     for index in array
#         index

def pair_plot(file, get_head=False):
    house_column = 'Hogwarts House'
    sns.set(style="ticks", color_codes=True)
    points = pd.read_csv(file).dropna()

    if (get_head is True):
        points = points.head(200)
    only_int = points.select_dtypes(exclude=['object'])
    min_c = only_int.apply(mean_normalization)
    # only_int.apply(remove, index=[0])

    houses = points.loc[:, house_column]
    only_int.loc[:, house_column] = houses.loc[:]
    sns.pairplot(only_int, hue=house_column)
    plt.show()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        try:
            pair_plot(sys.argv[1], len(sys.argv) > 2 and sys.argv[2] == "-h")
        except:
            print("error")
