import pandas as pd
import csv

df = pd.read_csv('Stackoverflow_Question_Classification_Challenge/full_data.csv',sep=';')
# print(df.describe())
'''Finding unique labels'''
labels_list= df['label'].unique()
# print(df['label'].count())
# print(df['label'].value_counts())
print('unique_labels:',labels_list)
# print(df['tags'].count())
# print(df['tags'].value_counts())
'''Finding unique tags'''
tags_list= df['tags'].unique()
print('unique_tags:',tags_list)

'''finding number of questions with given label'''
label = input('Enter the label to find the questions associated with it?: ')

if label not in labels_list:
    print('Invalid label')
else:
    question_for_label = df.loc[df['label']==label,'title']

# print(question_for_label)
print(question_for_label)
print(question_for_label.count())




