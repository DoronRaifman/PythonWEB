import os
from enum import Enum
import numpy as np
import pandas as pd


class ClassResult(Enum):
    Drowned = 0
    Survived = 1


class Sex(Enum):
    female = 0
    male = 1
    no_gender = 2


class Fields(Enum):
    Pclass = 0
    Sex = 1
    Age = 2
    SibSp = 3
    Parch = 4


class DataReader:
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def do_work(self, is_remove_bad):
        df = self.read_data()
        # print(df)
        new_df = self.remove_unwanted_features(df)
        new_df = self.fix_simple_values(new_df, is_remove_bad)
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

    def fix_simple_values(self, data:pd.DataFrame, is_remove_bad):
        for sex_enum in Sex:
            data['Sex'] = data['Sex'].replace(sex_enum.name, sex_enum.value)
        # handle age
        # count = sum(pd.isnull(data['Age']))
        # print(f'there are {count} null in age')
        count_orig = data.shape[0]
        if is_remove_bad:
            data = data.dropna()
        else:
            average_age = data['Age'].mean()
            # average_age = data['Age'].median()
            data['Age'] = data['Age'].replace(np.nan, average_age)
        count_final = data.shape[0]
        # print(f'count: orig={count_orig}, final={count_final}')
        return data

    def get_x_y(self, data:pd.DataFrame):
        # x_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
        x_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
        x = data[x_cols].to_numpy()
        y = data['Survived'].to_numpy()
        return x, y
