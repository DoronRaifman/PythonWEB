import os
import pickle

from Lesson10.titanic_reader import DataReader
from Lesson10.titanic_train import ClassifierModel


class Worker:
    def __init__(self):
        pass

    def do_work(self, csv_file_name):
        reader = DataReader(csv_file_name)
        x, y = reader.do_work(is_remove_bad=False)
        file_name = os.path.join('Data', 'best_model.sav')
        best_model:ClassifierModel = pickle.load(open(file_name, 'rb'))
        y_predict, score = best_model.predict(x, y)
        model_name = best_model.name
        print(f'Best model is {model_name}, score={score}')


if __name__ == '__main__':
    csv_file_name = 'titanic_train.csv'
    worker = Worker()
    worker.do_work(csv_file_name)
