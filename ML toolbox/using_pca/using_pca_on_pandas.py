import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import svm

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# load dataset into Pandas DataFrame
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
label = ['target']
df = pd.read_csv(url, names=features + label)

# Seperate to data (X) and labels (Y)
X, y = df.loc[:, features], df.loc[:, label]

# Normalize X between 0-1
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)

# Perform PCA, reduce to N=2 features/dimentions ,
pca = PCA(n_components=2)
X_reduces = pca.fit_transform(X_scaled)

# Fit
clf = svm.SVC(gamma='scale')
clf.fit(X_reduces, y)

print "CODE COMPLETED"
