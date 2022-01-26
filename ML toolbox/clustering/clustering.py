import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA
import matplotlib.cm as cm
from sklearn.cluster import KMeans

import os


def visualize_by_label(df, label_col='', outputpath=None, fname='NoName', use_labels=True, print_path=True):
    if outputpath == None:
        outputpath = os.path.dirname(os.path.realpath(__file__))

    outputpath = os.path.join(outputpath, '{}.png'.format(fname))
    if print_path:
        print "Printing graph to {}".format(outputpath)

    data = df.copy()
    if use_labels:
        pass
    else:
        data[label_col] = 0
    labels = data[label_col]

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, labels], axis=1)

    targets = labels.unique()
    tags = len(targets)
    colors = cm.rainbow(np.linspace(0, 1, tags))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 component PCA', fontsize=20)

    for target, color in zip(targets, colors):
        indicesToKeep = finalDf[label_col] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c=color,
                   s=50,
                   )
    if use_labels:
        ax.legend(targets)
    ax.grid()
    plt.savefig(outputpath)


if __name__ == '__main__':
    print_header = True
    if print_header:
        print "Clustering demo."
        print "Author: Guy Barash"
        print ""

        del print_header

    create_data = True
    if create_data:
        # Make example data with three clusters
        X, y = make_blobs(n_samples=1000, centers=3, n_features=3, cluster_std=2.5)
        with_labels_df = pd.DataFrame(columns=['f{}'.format(i) for i in range(X.shape[1])] + ['label'],
                                      index=range(X.shape[0]))
        for col in range(X.shape[1]):
            with_labels_df['f{}'.format(col)] = X[:, col]
        with_labels_df['label'] = y
        df = with_labels_df.drop(columns=['label'])

        # Visualize
        visualize_by_label(df, label_col='label', use_labels=False, fname='NO CLUSTERS')

        del create_data
        del X, y, col

    cluster_data = True
    if cluster_data:
        # Cluster the data found in df
        max_num_of_clusters = 5  # you do have to "guess" how many clusters are there
        min_num_of_clusters = 2
        for k in range(min_num_of_clusters, max_num_of_clusters + 1):
            print "Clustering with {} clusters".format(k)
            clstr = KMeans(n_clusters=k)
            clstr.fit(df)
            predicted_labels = clstr.labels_
            clstr_df = df.copy()
            clstr_df['label'] = predicted_labels

            # Visualize
            visualize_by_label(clstr_df, label_col='label', use_labels=True, fname='{} CLUSTERS'.format(k))

        del cluster_data
        del max_num_of_clusters, min_num_of_clusters, k, clstr, predicted_labels, clstr_df

    print "END OF CODE."
