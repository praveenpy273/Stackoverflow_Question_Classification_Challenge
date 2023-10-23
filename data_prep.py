import requests
import pandas as pd


csv_data = pd.read_csv('https://www.kaggle.com/datasets/nazeboan/stackoverflow-questions-classification-challenge?select=full_dataset.csv', on_bad_lines = 'skip')
csv_data.to_csv('full_data.csv',index=False)

#num of rows in csv file
num_of_lines = csv_data.shape[0]
print(num_of_lines)