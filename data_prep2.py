import pandas as pd
import csv

df = pd.read_csv('Stackoverflow_Question_Classification_Challenge/full_data.csv',sep=';')
print(df.describe())
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

'''Determining length of question'''
y = lambda x: len(x.split(' '))
new_df = df
length = new_df['title'].apply(y)
new_df.insert(column='title_length', value=length, loc=1)
print(new_df.head())

'''Replacing column "tags" by length of number of tags'''
print(df.head())
tag_length = new_df['tags'].apply(y)
new_df.insert(column='len_tags', value=tag_length, loc=2)
tag_df = new_df.drop('tags',axis = 1)
print(tag_df.head())

'''Filter the dataframe to only contain examples where label is “python”'''
python_df = df.loc[df['label']=='python']
print(python_df)

''' drop extra columns'''
columns_to_drop = ['title_length','len_tags']
df = df.drop(columns_to_drop,axis=1)

'''Filter the dataframe to only contain examples where tag is “python”'''
def filter_tag(tag_list,tag):
    return tag in tag_list

filtered_tag = df['tags'].apply(filter_tag,tag='python')
filtered_df_tag = df[filtered_tag]
print(filtered_df_tag.tail())

'''Group questions by tags and count how many questions belong to each tag'''
# 1. group by tags

grouped = df.groupby('tags')
counts_per_tags = grouped['title'].count()
print(counts_per_tags)

# 2. group by tag

def find_tag(tag_list):
    for tag in eval(tag_list):
        return tag
    
sep_tag = df['tags'].apply(find_tag)

group_tag = df.groupby(sep_tag)
count_per_tag = group_tag['title'].count()
print(count_per_tag)

'''Group questions by “done” and count how many questions belong to each category of “done”'''
done_group = df.groupby('done')
done_list = done_group['title'].count()
print(done_list)

'''Check in how many questions does 1 or more tag appear as part of the question title'''
def tags_to_check(ques,tag_list):
  for tag in tag_list:
    if tag in ques:
      return True
    else:
      False

df['contain_tag'] = df['title'].apply(tags_to_check,tag_list = sep_tag)
total = df['contain_tag'].sum()
print(total)

'''What are the most common words in question titles or bodies?'''

word_dict = {}
for title in df['title']:
  for word in title.split():
    if word not in word_dict:
      word_dict[word] = 1
    else:
      word_dict[word] += 1
common_word = ''
max_count = 0
for i,v in word_dict.items():
  if v > max_count:
    common_word = i
    max_count = v
print(common_word,':', max_count)