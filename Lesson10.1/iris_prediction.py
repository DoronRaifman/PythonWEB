import os
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


class ClassifyIris:
    def __init__(self):
        self.iris_name_to_val = {
            'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
        }
        self.class_names = list(self.iris_name_to_val.keys())

    def read_and_clean_data(self):
        file_name = os.path.join('Data', 'iris_data.csv')
        data = pd.read_csv(file_name)
        # replace class_id str to enumerated int values
        for iris_name in self.iris_name_to_val.keys():
            data['class_id'] = data['class_id'].replace(
                iris_name, self.iris_name_to_val[iris_name])
        X = data.drop(columns=['class_id'])     # take all except class_id
        y = data['class_id']                    # y - class_id true result
        return X, y

    def classify_logistic_regression(self, X, y):
        model = LogisticRegression()    # construct the classifier
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.8, random_state=42)
        model.fit(X_train, y_train)         # train the model
        y_predict = model.predict(X_test)   # predict the test set
        score = 100.0 * metrics.accuracy_score(y_test, y_predict)
        print(f'Iris prediction accuracy score: {score:.1f}%')
        self.print_confusion_matrix(model, X_test, y_test)

    def print_confusion_matrix(self, model, X_test, y_test):
        disp = plot_confusion_matrix(
            model, X_test, y_test, display_labels=self.class_names,
            cmap=plt.cm.Blues, normalize='true')
        disp.ax_.set_title('Iris prediction confusion matrix')
        plt.show()


if __name__ == '__main__':
    print('logistic regression')
    classifier = ClassifyIris()
    X, y = classifier.read_and_clean_data()
    classifier.classify_logistic_regression(X, y)

