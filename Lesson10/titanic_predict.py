import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Lesson10.titanic_reader import DataReader, Fields, ClassResult
from Lesson10.titanic_train import ClassifierModel


class Worker:
    def __init__(self):
        self.best_model = None

    def do_work(self, csv_file_name):
        reader = DataReader(csv_file_name)
        x, y = reader.do_work(is_remove_bad=False)
        file_name = os.path.join('Data', 'best_model.sav')
        best_model: ClassifierModel = pickle.load(open(file_name, 'rb'))
        self.best_model = best_model
        y_predict, score = best_model.predict(x, y)
        model_name = best_model.name
        print(f'Best model is {model_name}, score={score}')
        self.draw_clustering(model_name, x, y, y_predict, score)
        self.print_confusion_matrix(x, y, y_predict)

    def draw_clustering(self, model_name, x, y, y_predict, score):
        fig = plt.figure(figsize=(18, 10))
        plt.suptitle(f"Best model is {model_name}, score={score}"
                     f" - Clustering", size=30)
        ax = Axes3D(fig)
        fields = [Fields.Pclass, Fields.Sex, Fields.Age]
        field_values = [x[:, field.value] for field in fields]
        field_names = [field.name if field != Fields.Sex else
                       field.name+', female=0, male=1' for field in fields]
        ax.set_xlabel(field_names[0])
        ax.set_ylabel(field_names[1])
        ax.set_zlabel(field_names[2])
        ax.scatter(np.extract(y_predict == ClassResult.Drowned.value, field_values[0]),
                   np.extract(y_predict == ClassResult.Drowned.value, field_values[1]),
                   np.extract(y_predict == ClassResult.Drowned.value, field_values[2]),
                   color='red', marker='o', s=40, label='Drowned')
        ax.scatter(np.extract(y_predict == ClassResult.Survived.value, field_values[0]),
                   np.extract(y_predict == ClassResult.Survived.value, field_values[1]),
                   np.extract(y_predict == ClassResult.Survived.value, field_values[2]),
                   color='blue', marker='x', s=40, label='Survived')
        plt.legend(loc='lower left')
        plt.show()
        plt.close(fig)

    def print_confusion_matrix(self, x, y, y_predict):
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import plot_confusion_matrix
        mtx = np.array(confusion_matrix(y, y_predict))
        mtx = np.round(mtx, 2)

        class_names = [class_result.name for class_result in ClassResult]
        disp = plot_confusion_matrix(self.best_model.model, x, y,
                                     display_labels=class_names,
                                     cmap=plt.cm.Blues,
                                     normalize='true')
        disp.ax_.set_title('confusion matrix')

        print('confusion matrix')
        print(mtx)

        plt.show()


if __name__ == '__main__':
    csv_file_name = 'titanic_train.csv'
    worker = Worker()
    worker.do_work(csv_file_name)
