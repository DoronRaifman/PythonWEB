import os
from enum import Enum
import numpy as np
import pickle
from sklearn import metrics
from sklearn.model_selection import train_test_split
from Lesson10.titanic_reader import DataReader


class ClassifierModel:
    def __init__(self, name, classifier_model_object):
        self.name = name
        self.model = classifier_model_object

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x_test, y_test):
        y_predict = self.model.predict(x_test)
        if self.name == 'linear regression':
            y_predict = np.round(y_predict, 0)
        score = 100.0 * metrics.accuracy_score(y_predict, y_test)
        score = round(score, 2)
        return y_predict, score


class MainManager:
    def __init__(self):
        pass

    def do_work(self, csv_file_name):
        from sklearn.pipeline import Pipeline
        from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.naive_bayes import GaussianNB
        from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
        from sklearn.linear_model import LogisticRegression, LinearRegression
        from sklearn.neural_network import MLPClassifier

        classifiers = {
            'KNN': {'model': KNeighborsClassifier(n_neighbors=3)},
            'KNN Pipeline': {
                'model': Pipeline([
                    ('nca', NeighborhoodComponentsAnalysis(random_state=100)),
                    ('knn', KNeighborsClassifier(n_neighbors=3))])},
            'DecisionTree': {'model': DecisionTreeClassifier(random_state=0)},
            'RandomForest': {'model': RandomForestClassifier()},
            'Naive Base': {'model': GaussianNB()},
            'logistic regression': {
                'model': LogisticRegression(random_state=0, solver='newton-cg',
                                            multi_class='multinomial', max_iter=10000)},
            'linear regression': {'model': LinearRegression()},
            'gradient boosting': {'model':  GradientBoostingClassifier(
                n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)},
            'MLP': {'model': MLPClassifier(
                solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15, ), random_state=1,
                                           max_iter=10000)},
        }
        reader = DataReader(csv_file_name)
        # x_no_bad, y_no_bad = reader.do_work(is_remove_bad=True)
        x_all, y_all = reader.do_work(is_remove_bad=False)
        # X_train, X_test, y_train, y_test = train_test_split(
        #       x_all, y_all, test_size=0.8, random_state=0)
        names = list(classifiers.keys())
        for name in names:
            classifier_data = classifiers[name]
            classifier_model_object = classifier_data['model']
            classifier_model = ClassifierModel(name, classifier_model_object)
            # classifier_model.fit(x_no_bad, y_no_bad)
            classifier_model.fit(x_all, y_all)
            # y_predict, score = classifier_model.predict(x_no_bad, y_no_bad)
            # y_predict, score = classifier_model.predict(X_test, y_test)
            y_predict, score = classifier_model.predict(x_all, y_all)
            classifier_data['score'] = score
            classifier_data['classifier_model'] = classifier_model

        # order by score descending
        classifiers_list = [
            (name, classifiers[name]['score'])
            for name in classifiers.keys()]
        sorted_classifiers = sorted(
            classifiers_list, key=lambda tup:tup[1], reverse=True)
        for item in sorted_classifiers:
            name, score = item
            classifier_data = classifiers[name]
            print(f'classifier {name}: score={score}')
        # take best classifier
        best_classifier_item = sorted_classifiers[0]
        best_classifier_name, _ = best_classifier_item
        best_classifier_data = classifiers[best_classifier_name]
        best_model = best_classifier_data['classifier_model']
        file_name = os.path.join('Data', 'best_model.sav')
        pickle.dump(best_model, open(file_name, 'wb'))


if __name__ == '__main__':
    csv_file_name = 'titanic_train.csv'
    worker = MainManager()
    worker.do_work(csv_file_name)

