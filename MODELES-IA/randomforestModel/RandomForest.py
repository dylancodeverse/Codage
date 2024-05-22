# pip install numpy
import numpy as np
# pip install pandas
import pandas as pd
# pip install matplotlib
from matplotlib import pyplot as plt

# ato le donnees d'entrainement
df_train = pd.read_csv("C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/training/Training.csv")

# ato le donnees atao prediction
df_test = pd.read_csv("C:/Users/MISA/Desktop/Workspace/S6/Codage/MODELES-IA/datas/training/ToPredict.csv")

# Sélectionner toutes les lignes et les colonnes à partir de la colonne nommée 'isCode' jusqu'à la fin
X_train = df_train.loc[:, 'isCode':].values

# Sélectionner toutes les lignes 
y_train = df_train.loc[:, 'isCode'].values
