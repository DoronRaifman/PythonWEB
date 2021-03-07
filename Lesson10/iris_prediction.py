import os
from enum import Enum
import numpy as np


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
        self.iris_name_to_val = {'Iris-setosa': 1, 'Iris-versicolor': 2, 'Iris-virginica': 3}

    def read_csv(self):
        file_name = os.path.join('Data', 'iris_data.csv')
        x, y = [], []
        x_val_count = 4
        with open(file_name, 'rt') as fdes:
            lines = fdes.readlines()
            for line in lines[1:]:
                row_values = line[:-1].split(sep=',')
                values = [float(row_values[i]) for i in range(x_val_count)]
                class_name = row_values[Fields.class_id.value]
                y_val = self.iris_name_to_val[class_name]
                x.append(values)
                y.append(y_val)
        x_val, y_val = np.array(x), np.array(y)
        return x_val, y_val

    def classify(self):
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split
        from sklearn import metrics

        model = LogisticRegression()
        X_train, X_test, y_train, y_test = train_test_split(self.x_val, self.y_val, test_size=0.4, random_state=42)
        model.fit(X_train, y_train)
        y_predict = model.predict(X_test)
        score = 100.0 * metrics.accuracy_score(y_test, y_predict)
        print(f'result: {score:.1f}')


if __name__ == '__main__':
    classifier = ClassifyIris()
    classifier.x_val, classifier.y_val = classifier.read_csv()
    classifier.classify()


