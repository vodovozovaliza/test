import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from math import sqrt

dpi = 80

def minmax_normalization(df):
    """
    :does: normalizez the data for that it numbers are between 0 and 1
    """
    result = df.copy()
    for feature_name in df.columns[1:]:
        # Minimum
        min = df[feature_name].min()
        # Maximum
        max = df[feature_name].max()

        result[feature_name] = (df[feature_name] - min) / (max - min)
    return result

def show(input_filename, weights):
    """
    :does: shows all the data in a diagram
    """
    df = pd.read_csv(input_filename)

    # Normalize
    print(df[df.columns[1:]])
    df = minmax_normalization(df)
    print(df[df.columns[1:]])

    # Data processing
    df['Total score'] = (df[df.columns[1:]] * weights).sum(axis=1)
    # print(df['Total score'])

    # Sort values by total score
    df.sort_values(by='Total score', ascending=True, inplace=True)

    # Set font size
    mpl.rcParams.update({'font.size': 9})
    # Create figure
    _, ax = plt.subplots(dpi = dpi, figsize = (512 / dpi, 384 / dpi), num = 'Test')
    # Drawing vertical lines for x axis
    ax.xaxis.grid(True, zorder = 1)
    ax.set_title('Test')
    # The y coordinates of the bars
    xs = range(len(df['Total score'].values))

    # Create a horizontal bar plots
    plt.barh(xs, df['Total score'].values,
            height = 0.2, color = 'blue', alpha = 0.7, label = 'KPI',
            zorder = 2)

    # Draw names of objects
    plt.yticks(xs, df[df.columns[0]].values, rotation = 10)

    # Set legend location
    plt.legend(loc='upper right')
    plt.savefig('result.png')
    plt.show()

if __name__ == '__main__':
    show('movehubcostofliving.csv', [0.1, 0.1, 0.1, 0.2, 0.2, 0.4])
    #show('test.csv', [0.1, 0.1, 0.1, 0.2, 0.2, 0.4])