import os
from sklearn.decomposition import PCA
import matplotlib.cm as cm

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def visualize_by_label(df, label_col, outputpath, fname='NoName', components=2):
    outputpath = os.path.join(outputpath, '{}.png'.format(fname))

    data = df.drop(columns=[label_col])
    labels = df[label_col]

    pca = PCA(n_components=components)
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])

    finalDf = pd.concat([principalDf, labels], axis=1)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 component PCA', fontsize=20)
    targets = labels.unique()
    tags = len(targets)
    colors = cm.rainbow(np.linspace(0, 1, tags))

    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[label_col] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c=color,
                   s=50,
                   )
    ax.legend(targets)
    ax.grid()
    plt.savefig(outputpath)


if __name__ == '__main__':
    # URL of database
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

    # load dataset into Pandas DataFrame
    features = ['sepal length', 'sepal width', 'petal length', 'petal width']
    label = 'target'
    df = pd.read_csv(url, names=features + [label])

    data_path = os.path.dirname(os.path.realpath(__file__))
    fname = 'PCA_visualization'
    visualize_by_label(df, 'target', data_path, fname)
