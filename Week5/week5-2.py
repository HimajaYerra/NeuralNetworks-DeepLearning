from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.svm import SVC



# Split dataset into training set and test set
dataset = pd.read_csv("glass.csv")

X = dataset.drop(['Type'], axis=1)

y = dataset['Type']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=109)

# 70% training and 30% testX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
model = SVC(kernel='rbf', random_state = 1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred)
      )
print("Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))