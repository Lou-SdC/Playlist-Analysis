#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:06:45 2025

@author: Ith
"""

import pandas as pd
import copy
import numpy as np
import matplotlib as plt


#open the clean csv
csv = pd.read_csv('des_sons_et_des_gens_MotsClefs.csv')

#%%
#drop duplicated lines

csv = csv.drop_duplicates(ignore_index=True)


#%%
#get the list of persons in the "Personne(s)" column
liste = []

for i in csv['Personne(s)']:

    if ',' in i:
        l = i
        while ',' in l:
            virgule = l.find(',')
            name = l[0:virgule]
            if name in liste:
                r = name
                l = l.replace(l[0:virgule+2], '')
            else:
                liste.append(name)
                l = l.replace(l[0:virgule+2], '')
        name = l
        if name in liste:
            r = name
        else:
            liste.append(name)
         
    else:
        if i in liste :
            r = i
        else :
            name = i
            liste.append(name)
            

#%%
#get the category for each person

df_categories = pd.read_csv('categories.csv')

category = []
for name in liste:
    if name in df_categories['nom'].tolist():
        index = df_categories.index[df_categories['nom'] == name].tolist()
        cat = df_categories['catégorie'][index[0]]
    else : 
        cat = input('Dans quelle catégorie est : ' + name + '? ')
    category.append(cat)
    
df_categories_new = pd.DataFrame([liste, category]).T
df_categories_new.columns = ['nom', 'catégorie']
df_categories_new.to_csv('categories.csv', index=False)
    
    
#%%
#prepare dataframe for statistics

#get counts and duration of music for every name
counts = []
durations = []
for name in liste:
    count = 0
    duration = 0
    for i in range(len(csv)):
        if name in csv['Personne(s)'][i]:
            count = count + 1
            duration = duration + csv['Durée (ms)'][i]
    counts.append(count)
    durations.append(duration)
    
#%%
#analysis on the "count" parameter

    
df = pd.DataFrame([liste, category, counts, durations]).T
df.columns = ['Nom', 'catégorie', 'count', 'duration']
df = df.sort_values(by=["count"], ascending=False)
df.set_index('Nom', inplace=True)

df_catégories = df.groupby('catégorie').count()


ax = df_catégories.plot(kind='pie', y='count', autopct='%1.0f%%')
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')

ax = df.head(10).plot(kind = 'pie', y = 'count', autopct='%1.0f%%')
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')


#%%
#analysis on the "duration" parameter

    
df = pd.DataFrame([liste, category, counts, durations]).T
df.columns = ['Nom', 'catégorie', 'count', 'duration']
df = df.sort_values(by=["duration"], ascending=False)
df.set_index('Nom', inplace=True)

df_catégories = df.groupby('catégorie').sum()


ax = df_catégories.plot(kind='pie', y='duration', autopct='%1.0f%%')
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')

ax = df.head(10).plot(kind = 'pie', y = 'duration', autopct='%1.0f%%')
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')






















