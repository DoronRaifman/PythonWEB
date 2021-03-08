import os
from enum import Enum
import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier


class Sex(Enum):
    female = 0
    male = 1
    no_gender = 2


class DataReader:
    def __init__(self):
        pass

    def do_work(self):
        df = self.read_data()
        # print(df)
        new_df = self.remove_unwanted_features(df)
        new_df = self.fix_simple_values(new_df)
        # print(f'cols: {new_df.columns.tolist()}')
        # print(new_df)
        x, y, = self.get_x_y(new_df)
        return x, y

    def read_data(self):
        file_name = os.path.join('Data', 'titanic_train.csv')
        data = pd.read_csv(file_name)
        return data

    def remove_unwanted_features(self, data:pd.DataFrame):
        droped_data = data.drop(columns=['PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
        return droped_data

    def fix_simple_values(self, data:pd.DataFrame):
        data['Sex'] = data['Sex'].replace(np.nan, 'no_gender')
        for sex_enum in Sex:
            data['Sex'] = data['Sex'].replace(sex_enum.name, sex_enum.value)
        data['SibSp'] = data['SibSp'].replace(np.nan, 0)
        # Todo: handle age
        count = sum(pd.isnull(data['Age']))
        # print(f'there are {count} null in age')
        data['Age'] = data['Age'].replace(np.nan, 30)
        return data

    def get_x_y(self, data:pd.DataFrame):
        x_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
        x = data[x_cols].to_numpy()
        y = data['Survived'].to_numpy()
        return x, y


class Classifier:
    def __init__(self, classifier):
        self.model = classifier

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x_test, y_test):
        y_predict = self.model.predict(x_test)
        score = 100.0 * metrics.accuracy_score(y_test, y_predict)
        score = round(score, 2)
        return y_predict, score


class MainManager:
    def __init__(self):
        pass

    def do_work(self):
        reader = DataReader()
        x, y = reader.do_work()
        classifiers = {
            'KNN': KNeighborsClassifier(n_neighbors=3),
            'KNN Pipeline': Pipeline([('nca', NeighborhoodComponentsAnalysis(random_state=100)),
                                      ('knn', KNeighborsClassifier(n_neighbors=3))]),
            'DecisionTree': DecisionTreeClassifier(random_state=0),
            'Naive Base': GaussianNB(),
            'RandomForest': RandomForestClassifier(),
            'sgd': SGDClassifier(loss="huber", penalty="elasticnet", max_iter=10000, tol=0.001),
            'logistic_regression': LogisticRegression(random_state=0, solver='newton-cg', multi_class='multinomial',
                                                      max_iter=10000),
            'gradient_boosting': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1,
                                                            random_state=0),
            'MLP': MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, ), random_state=1,
                                   max_iter=10000),
        }
        for name, classifier_class in classifiers.items():
            classifier = Classifier(classifier_class)
            classifier.fit(x, y)
            y_predict, score = classifier.predict(x, y)
            print(f'classifier {name}: score={score}')


if __name__ == '__main__':
    worker = MainManager()
    worker.do_work()

