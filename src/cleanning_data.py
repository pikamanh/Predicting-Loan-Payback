import pandas as pd
import os

class DataCleaner:
    def __init__(self, train_filename, test_filename):
        self.dir_path = os.getcwd()
        self.train_filename = train_filename
        self.test_filename = test_filename
        
    def load_data(self):
        try:
            data_folder = os.path.join(self.dir_path, "dataset")
            train_path, test_path = os.path.join(data_folder, self.train_filename), os.path.join(data_folder, self.test_filename)
            
            train_data, test_data = pd.read_csv(train_path), pd.read_csv(test_path)

            return train_data, test_data
        except Exception as e:
            print("Đã xảy ra lỗi: ", e)
            return pd.DataFrame([]), pd.DataFrame([])
        
    def clean_data(self):
        train_data, test_data = self.load_data()

        train_data.dropna(inplace=True)
        test_data.dropna(inplace=True)

        train_data.drop(['id'], axis=1, inplace=True)

        return train_data