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
tags= df['tags']

def unique_tags(df):
    lst1 = []
    for i in df:
        for j in eval(i):
            if j not in lst1:
                lst1.append(j)
    return lst1

uq_tags = unique_tags(tags)
print(uq_tags)
print(len(uq_tags))

'''finding number of questions with given label'''
label = input('Enter the label to find the questions associated with it?: ')

if label not in labels_list:
    print('Invalid label')
else:
    question_for_label = df.loc[df['label']==label,'title']

# print(question_for_label)
print(question_for_label)
print(question_for_label.count())

''''Determining length of question'''
question = pd.Series('title')
print('question: ', question)
len_ques = lambda x: len(x)
print(question.apply(len_ques))



