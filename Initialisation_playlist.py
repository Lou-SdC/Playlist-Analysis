#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:44:45 2025

@author: Ith
"""

import pandas as pd
import copy
import numpy as np

#Open the .csv obtained with Exportify
csv_raw = pd.read_csv('des_sons_et_des_gens.csv')

#Copy the dataframe, get the columns names and drop the ones we don't care about
csv = copy.deepcopy(csv_raw)
columns = csv.columns
csv = csv.drop(["URI du titre", "URI(s) de l'artiste", "URI de l'album", "URI(s) de l'artiste de l'album",
          "Nom(s) de l'artiste de l'album", "Date de sortie de l'album", "URL de l'image de l'album",
          'Numéro de disque', 'Numéro du titre', 'URL de prévisualisation du titre', 'Explicite', 'Popularité', 'ISRC',
          'Ajouté par', 'Ajouté le'], axis=1)

#Create a new column for the person(s) attached to the song
csv['Personne'] = np.zeros([len(csv)])

csv.columns = ['Nom', 'Artiste(s)', 'Album', 'Durée (ms)', 'Personne(s)']

#%%

#Get asked for the names of the person(s) for each song

for i in range(len(csv)):
    if csv['Personne(s)'][i] == 0.0:
        print('le titre de la chanson est ' + csv.loc[i, 'Nom'] + ', de ' + csv.loc[i, "Artiste(s)"])
        csv.loc[i, 'Personne(s)'] = input('personne(s) ?')



#%%

#Save the new dataframe in a .csv file

csv.to_csv('des_sons_et_des_gens_MotsClefs.csv', index=False)
