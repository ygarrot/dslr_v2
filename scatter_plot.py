import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def scatter(file, get_head=False):
    sns.set(style="ticks", color_codes=True)

    house_column = 'Hogwarts House'
    first = 'Astronomy'
    second = 'Defense Against the Dark Arts'

    points = pd.read_csv(file)
    if (get_head is True):
        points = points.head(50)
    only_int = points.select_dtypes(exclude=['object'])
    sns.scatterplot(data=points, hue=house_column, x=first, y=second)
    plt.show()


if __name__ == '__main__':
    if (len(sys.argv) > 1 ):
        try:
            scatter(sys.argv[1], len(sys.argv) > 2 and sys.argv[2] == "-h")
        except:
            print("error")
