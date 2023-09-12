## 1) What is ML ?

A partir de données, le modèle transforme et extrait les informations à partir de ces données pour faire des prédictions. Les features sont les informations que l'on a à disposition et la target (ou cible) constitue ce que l'on cherche à prédire.
Un modèle encapsule tout ce qu'il aura appris à partir des features dans les données.

Les données sont de deux types : les features et la cible (target). Le modèle encapsule ces deux objets pour pouvoir en déduire des patterns.

## 2) Machine Learning vs Rule-Based Systems

Un système basé sur des règles va s'implémenter en transcrivant des règles en code. Le souci de ce type de système c'est qu'il peut vite devenir complexe. Le processus est itératif car on va y ajouter des règles au fur et à mesure, des retraits de règles, etc. On se retrouve avec quelque chose de difficile maintenable. On va donc plutôt lui préférer le machine learning.
Après avoir obtenu des données, on définit et calcule des features puis on entraîne et utilise le modèle obtenu.

## 3) Apprentissage supervisé

On aura des features et une cible. On va chercher à entraîner une fonction qui prend comme paramètres les features pour pouvoir atteindre la cible/prédiction.
Il existe plusieurs types d'apprentissage supervisé :
- la régression (prédiction du prix d'une voiture, d'une maison)
- la classification :
    - binaire
    - multiclasse
- le ranking (système de recommandation)
