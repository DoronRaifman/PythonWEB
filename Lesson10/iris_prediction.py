import os
from enum import Enum
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt


class Fields(Enum):
    sepal_length = 0
    sepal_width = 1
    petal_length = 2
    petal_width = 3
    class_id = 4


class ClassifyIris:
    def __init__(self):
        self.x_val = None
        self.y_val = None
        self.iris_name_to_val = {
            'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
        }
        self.class_names = list(self.iris_name_to_val.keys())
        self.class_values = list(self.iris_name_to_val.values())

    def read_csv(self):
        file_name = os.path.join('Data', 'iris_data.csv')
        x_list, y_list = [], []
        x_val_count = 4
        with open(file_name, 'rt') as fdes:
            lines = fdes.readlines()
            for line in lines[1:]:
                row_values = line[:-1].split(sep=',')
                values = [
                    float(row_values[i])
                    for i in range(x_val_count)]
                class_name = row_values[Fields.class_id.value]
                y_val = self.iris_name_to_val[class_name]
                x_list.append(values)
                y_list.append(y_val)
        X, y = np.array(x_list), np.array(y_list)
        return X, y

    def classify_logistic_regression(self):
        from sklearn.linear_model import LogisticRegression

        model = LogisticRegression()
        X_train, X_test, y_train, y_test = train_test_split(
            self.x_val, self.y_val, test_size=0.8, random_state=42)
        model.fit(X_train, y_train)
        y_predict = model.predict(X_test)
        score = 100.0 * metrics.accuracy_score(y_test, y_predict)
        print(f'result: {score:.1f}')
        self.print_confusion_matrix(model, X_test, y_test, y_predict)

    def classify_linear_regression(self):
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        X_train, X_test, y_train, y_test = train_test_split(
            self.x_val, self.y_val, test_size=0.8, random_state=42)
        model.fit(X_train, y_train)
        y_predict = model.predict(X_test)
        y_predict_round = np.round(y_predict, 0)
        score = 100.0 * metrics.accuracy_score(y_test, y_predict_round)
        print(f'result: {score:.1f}')
        mtx = np.array(confusion_matrix(y_test, y_predict_round))
        mtx = np.round(mtx, 2)
        print('confusion matrix')
        print(mtx)
        self.draw_lin_regr_results(y_predict, y_predict_round, y_test)

    def draw_lin_regr_results(self, y_predict, y_predict_round, y_test):
        print('Results graph')
        fig = plt.figure(figsize=(18, 10))
        plt.suptitle(f"Linear regression results", size=30)
        plt.xlabel('true result', size=20)
        plt.ylabel('predicted result', size=20)
        hit = np.where(y_predict_round == y_test)
        miss = np.where(y_predict_round != y_test)
        plt.scatter(y_test[hit], y_predict[hit], color='green',
                    marker='+', s=40, label='Match')
        plt.scatter(y_test[miss], y_predict[miss], color='red',
                    marker='x', s=40, label='Not Match')
        for true_value in self.class_values:
            x = np.linspace(start=true_value-0.2, stop=true_value+0.2)
            y = np.full(x.size, true_value)
            plt.plot(x, y, '--', color='magenta')
        plt.legend()
        plt.show()
        plt.close(fig)

    def print_confusion_matrix(
            self, model, X_test, y_test, y_predict):
        mtx = np.array(confusion_matrix(y_test, y_predict))
        mtx = np.round(mtx, 2)
        print('confusion matrix')
        print(mtx)
        disp = plot_confusion_matrix(
            model, X_test, y_test,
            display_labels=self.class_names,
            cmap=plt.cm.Blues, normalize='true')
        disp.ax_.set_title('confusion matrix')
        plt.show()


if __name__ == '__main__':
    classifier = ClassifyIris()
    classifier.x_val, classifier.y_val = classifier.read_csv()
    print('logistic regression')
    classifier.classify_logistic_regression()
    print('linear regression')
    classifier.classify_linear_regression()

