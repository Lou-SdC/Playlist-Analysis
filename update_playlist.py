#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:44:45 2025

@author: Ith
"""

import pandas as pd
import copy
import numpy as np


#open the new csv with the latest version of the playlist and the csv already processed on the previous time
csv_raw = pd.read_csv('des_sons_et_des_gens.csv')
csv = pd.read_csv('des_sons_et_des_gens_MotsClefs.csv')

#clean the new dataframe
columns = csv_raw.columns
new_csv = copy.deepcopy(csv_raw)

new_csv = new_csv.drop(["URI du titre", "URI(s) de l'artiste", "URI de l'album", "URI(s) de l'artiste de l'album",
          "Nom(s) de l'artiste de l'album", "Date de sortie de l'album", "URL de l'image de l'album",
          'Numéro de disque', 'Numéro du titre', 'URL de prévisualisation du titre', 'Explicite', 'Popularité', 'ISRC',
          'Ajouté par', 'Ajouté le'], axis=1)

new_csv.columns = ['Nom', 'Artiste(s)', 'Album', 'Durée (ms)']

new_csv['Personne(s)'] = np.zeros([len(new_csv)])



#%%
#get the differences between the two dataframes
diff = new_csv[~new_csv['Nom'].isin(csv['Nom'])].reset_index(drop=True)


#%%
#Enter the persons names for the new songs

for i in range(len(diff)):
    if diff['Personne(s)'][i] == 0.0:
        print('le titre de la chanson est ' + diff.loc[i, 'Nom'] + ', de ' + diff.loc[i, "Artiste(s)"])
        diff.loc[i, 'Personne(s)'] = input('personne(s) ?')


#%%
#append the diff dataframe to the csv and save it

csv = pd.concat([csv, diff], axis=0)

csv.to_csv('des_sons_et_des_gens_MotsClefs.csv', index=False)
