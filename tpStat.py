#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:44:57 2022

"""

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pan 
import scipy.stats as st 
from statsmodels.distributions.empirical_distribution import ECDF
import statsmodels.api as sm 
import seaborn as sns 



                            ##### EXERCICE 1  #####
                            

Air=pan.read_csv('http://tinyurl.com/y39an7ef/Data68169.csv',sep='\t',na_values='-')




    #### PARTIE A : INFORMATION GÉNÉRAL ####



        #### QUESTION 2 ####

# nouveau data frame avec les 6 colonnes à étudier 
dfazote = pan.DataFrame(Air,columns = ["Lyon Gerland Monoxyde d'azote","Villeurbanne Place Grandclément Monoxyde d'azote","Est lyonnais / Saint Exupéry Monoxyde d'azote","Lyon Centre Monoxyde d'azote","Lyon - Tunnel Croix-Rousse - Sortie Rhône Monoxyde d'azote","Lyon Périphérique Monoxyde d'azote"])

# nouveau data frame comprenant uniquement des booleen pour indiquer si on a une valeur ou non
dfazotebool = dfazote.isna()

# nouveau data frame avec uniquement les jours où a été mesuré dans toutes les stations le monoxyde d'azote
dfazotoutemesure = dfazotebool[(dfazotebool['Lyon Gerland Monoxyde d\'azote'] == False ) & 
          (dfazotebool['Villeurbanne Place Grandclément Monoxyde d\'azote'] == False ) &
          (dfazotebool['Est lyonnais / Saint Exupéry Monoxyde d\'azote'] == False ) &
          (dfazotebool['Lyon Centre Monoxyde d\'azote'] == False ) &
          (dfazotebool['Lyon - Tunnel Croix-Rousse - Sortie Rhône Monoxyde d\'azote'] == False ) &
          (dfazotebool['Lyon Périphérique Monoxyde d\'azote'] == False )]



        #### QUESTION 3 ####

Air.isna().sum() 

m=np.array([46,45,57,50,27,26,23,64,62,69,29,26,26,12,67,43,25,25,47,6,8,8,23])

print(m[m<25])   

# création d'un data frame avec les composants ayant moins de 25 observations 

data = { 'Ville': ['Villeurbanne Place Grandclément', 'Lyon Centre', 'Lyon Périphérique', 
                   'Lyon péréphirique', 'Lyon Périphérique', 'Lyon periphérique'], 
        'composant chimique': ['Particule PM10','ozone','Dioxyde d azote','monoxyde de carbone',
                               'monoxyde d azote','particule PM10']}

df = pan.DataFrame(data, index=['0','1','2','3','4','5'])
print(df)



        #### QUESTION 4 ####
    

Air['Lyon Périphérique Monoxyde carbone'].dropna(how='all').describe()
np.var(Air['Lyon Périphérique Monoxyde carbone'].dropna(how='all')) # variance empirique 
np.var(Air['Lyon Périphérique Monoxyde carbone'].dropna(how='all'),ddof=1) # variance empirique non biaisée



        #### QUESTION 5 ####
        

df2PM10 =  pan.DataFrame(Air,columns = ["Lyon Gerland Particules PM10",
                                      "Villeurbanne Place Grandclément Particules PM10",
                                      "Est lyonnais / Saint Exupéry Particules PM10",
                                      "Lyon Centre Particules PM10",
                                      "Lyon - Tunnel Croix-Rousse - Sortie Rhône Particules PM10",
                                      "Lyon Périphérique Particules PM10"]) 

row_means = df2PM10.dropna(how='all').mean(axis=1)

# représentation de la fonction de répartition 
ecdf2 = ECDF(row_means) 
plt.step(ecdf2.x,ecdf2.y)
plt.xlim(0,100)
plt.ylim(0,1)
plt.title("fonction de répartition de la moyenne ")

prob = 1 - ecdf2(50) # probabilité >50
print(prob)

prob2 = 1 - ecdf2(80) # probabilité >80 
print(prob2)


        #### QUESTION 6 ####

    # partie sur les particule de PM10 

# data frame avec la date et les données pour les particules PM10 ainsi qu'une colonne moyenne pour la moyenne de chaque jours de l'émission de la particule 
dep10 = pan.DataFrame(Air,columns = [ "Date", 
                                        "Lyon Gerland Particules PM10",
                                      "Villeurbanne Place Grandclément Particules PM10",
                                      "Est lyonnais / Saint Exupéry Particules PM10",
                                      "Lyon Centre Particules PM10",
                                      "Lyon - Tunnel Croix-Rousse - Sortie Rhône Particules PM10",
                                      "Lyon Périphérique Particules PM10",
                                      ]) 
dep10['col8'] = row_means 


# data frame avec uniquement les jours dépassant le seuil de 50 
dep10sup50 = dep10[(dep10['col8']>50)] 
# data frame avec uniquement les jours dépassant le seuil de 80 
dep10sup80 = dep10[(dep10['col8']>80)] 


# creer la liste de jour de dépassement du seuil de 50 de PM10 
listePM10sup50 = dep10sup50['Date'].tolist() 
print(listePM10sup50)


# creer la liste de jour de dépassement du seuil de 80 de PM10 
listePM10sup80 = dep10sup80['Date'].tolist() 
print(listePM10sup80)




    # partie sur les particule d'ozone 
    
ozonepourmoy = pan.DataFrame(Air,columns = [ "Lyon Gerland Ozone ",
                                      "Est lyonnais / Saint Exupéry Ozone ",
                                      "Lyon Centre Ozone "
                                      ]) 


row_means2 = ozonepourmoy.dropna(how='all').mean(axis=1)
    

depozone = pan.DataFrame(Air,columns = [ "Date", 
                                        "Lyon Gerland Ozone ",
                                      "Est lyonnais / Saint Exupéry Ozone ",
                                      "Lyon Centre Ozone ",
                                      ]) 
depozone['col5'] = row_means2 

# data frame avec uniquement les jours dépassant le seuil de 180 
depozonesup180 = depozone[(depozone['col5']>180)] 
# data frame avec uniquement les jours dépassant le seuil de 240 
depozonesup240 = depozone[(depozone['col5']>240)] 


# creer la liste de jour de dépassement du seuil de 180 de particule d'ozone 
listeozonesup180 = depozonesup180['Date'].tolist() 
print(listeozonesup180)


# creer la liste de jour de dépassement du seuil de 240 de particule d'ozone 
listeozonesup240 = depozonesup240['Date'].tolist() 
print(listeozonesup240)



        
    #### PARTIE B : ÉTUDE DE LA POLLUTION À LA STATION DE LYON GERLAND ####
    
        

# création du data frame df1 rassemblant les mesures faites à Lyon Gerland     
df1 = pan.DataFrame(Air,columns = ["Lyon Gerland Dioxyde d'azote","Lyon Gerland Monoxyde d'azote","Lyon Gerland Ozone","Lyon Gerland Particules PM10"])
print(df1)

# création du data frame df2 rassemblant seulement les mesures de particules et d'ozones de gerland 
df2 = pan.DataFrame(Air,columns = ["Lyon Gerland Ozone","Lyon Gerland Particules PM10"])
print(df2)


        #### QUESTION 1 #### 

# covaiation des deux data frames crée
covdf1 = df1.dropna(how='all').cov()  
covdf2 = df2.dropna(how='all').cov()  
        


# correlation des deux data frames crée 
corrdf1 = df1.dropna(how='all').corr()  
corrdf2 = df2.dropna(how='all').corr()           
        
        
## j ai les meme resultats dans les deux data pour l'ozone et le PM 



        #### QUESTION 2 #### 


y2 = df2["Lyon Gerland Particules PM10"]
y2_filled = y2.fillna(0) 

x2 = df2["Lyon Gerland Ozone"]
x2_filled = x2.fillna(0)

z2 = np.log(y2)
z2_filled = z2.fillna(0)

l = len(x2)

l2 = len(y2)

# droite de regression de z en fonction de x 

X=np.column_stack((x2_filled,np.ones(l)))
res=sm.OLS(z2_filled,X).fit();print(res.summary())



# nuage de point et la droite de regression  => ne fonctionne pas pourtant meme code que le prof 

prediction=res.get_prediction().summary_frame(alpha=0.1)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x2_filled, z2_filled, "o", label="data")
ax.plot(x2_filled,  prediction["mean"], label="OLS",color="blue")#droite de rÈgression
ax.plot(x2_filled, prediction["obs_ci_lower"], color="red")#borne inf de la prÈdiction
ax.plot(x2_filled, prediction["obs_ci_upper"], color="red")#borne sup  de la prÈdiction
ax.legend(loc="best")
fig.suptitle("Regression de z en fonction de x avec intervalle de prediction ")



        #### QUESTION 3 #### 


# droite de regression 

X=np.column_stack((y2_filled,np.ones(l2)))
res2=sm.OLS(x2_filled,X).fit();print(res.summary())

# nuage de point entre x2 et y2 

prediction2=res2.get_prediction().summary_frame(alpha=0.1)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(y2_filled, x2_filled, "o", label="data")
ax.plot(y2_filled,  prediction["mean"], label="OLS",color="blue")#droite de rÈgression
ax.plot(y2_filled, prediction["obs_ci_lower"], color="red")#borne inf de la prÈdiction
ax.plot(y2_filled, prediction["obs_ci_upper"], color="red")#borne sup  de la prÈdiction
ax.legend(loc="best")
fig.suptitle("Regression de x en fonction de y avec intervalle de prediction ")



res2.get_prediction(exog=[(180,1)]).summary_frame(alpha=0.1)  
# on obtient l'intervalle de prediction à 90% [-69.541573 ,-69.541573]   

res2.get_prediction(exog=[(240,1)]).summary_frame(alpha=0.1)         
# on obtient l'intervalle de prediction à 90% [-97.857013 ,-1.310546]           


        
                
        
    
