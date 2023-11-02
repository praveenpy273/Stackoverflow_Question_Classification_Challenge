import pandas as pd
import csv

df = pd.read_csv('Stackoverflow_Question_Classification_Challenge/full_data.csv',sep=';')
# print(df.describe())
labels_list= df['label'].unique()
# print(df['label'].count())
# print(df['label'].value_counts())
print('unique_labels:',labels_list)
# print(df['tags'].count())
# print(df['tags'].value_counts())
tags_list= df['tags'].unique()
print('unique_tags:',tags_list)




