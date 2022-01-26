import pandas as pd
from sklearn.model_selection import KFold
from sklearn import svm

print "<>"
print "K-folds demo"
print "by Guy Barash <Guy.Barash@wdc.com>"
print "<>"

# URL of database
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# load dataset into Pandas DataFrame
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
label = 'target'
df = pd.read_csv(url, names=features + [label])

# Seperate to data (X) and labels (Y)
X, y = df.loc[:, features], df[label]

# K-folds
folds = 10
kf = KFold(n_splits=folds)
results = pd.Series(index=range(folds))
for kidx, (train_index, test_index) in enumerate(kf.split(X)):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]

    clf = svm.SVC(gamma='scale')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_true = y_test

    hit_rate = (y_pred == y_true).mean()
    print "Hit rate for iteration {}: {:>.2f}".format(kidx + 1, hit_rate)
    results[kidx] = hit_rate

print "Accuracy: {:>.2f} with deviation of {:>.2f}".format(results.mean(), results.std())
print "CODE COMPLETED"
