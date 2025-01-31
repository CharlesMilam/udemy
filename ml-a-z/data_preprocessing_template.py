# Data Preprocessing
# %%
# import the libraries
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from pprint import pprint

# suppress printing of scientific notation
np.set_printoptions(suppress=True)

# %%
# import the dataset
dataset = pd.read_csv('Data.csv')

# %%
# create features matrix
X = dataset.iloc[:, : -1].values
# create dependent variable vector
y = dataset.iloc[:, -1].values

# %%
# take care of missing data
imputer = Imputer('NaN')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# %%
# encode categorical data
labeler_X = LabelEncoder()
X[:, 0] = labeler_X.fit_transform(X[:, 0])
hotlabler = OneHotEncoder(categorical_features = [0])
X = hotlabler.fit_transform(X).toarray()
labeler_y = LabelEncoder()
y = labeler_X.fit_transform(y)

# %%
# splitting the dataset into a training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# %%
# feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
