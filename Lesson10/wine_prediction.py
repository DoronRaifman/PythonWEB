import numpy as np
from sklearn.datasets import load_diabetes, load_boston, load_wine
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix


# res = load_diabetes()
# res = load_boston()
res = load_wine()
X = res['data']
y = res['target']

feature_names = res['feature_names']
print(feature_names)

# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=50)

from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
model = Pipeline([
    ('nca', NeighborhoodComponentsAnalysis(random_state=100)),
    ('knn', KNeighborsClassifier(n_neighbors=3))])

# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=3)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
score = 100.0 * metrics.accuracy_score(y_test, y_predict)
print(f'result: {score:.1f}')


