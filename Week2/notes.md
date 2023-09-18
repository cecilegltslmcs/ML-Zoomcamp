# Régression linéaire

- [Youtube - 2.1 à 2.16](https://www.youtube.com/watch?v=vM3SqPNlStE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=11)
- [Github - Notebook](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/chapter-02-car-price)
- [Github - DataTalksClub](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/02-regression)
- [Notebook d'illustration](https://github.com/cecilegltslmcs/ML-Zoomcamp/blob/main/Week2/car_price_prediction.ipynb)

## 1) Description du problème

On va chercher à créer un outil pour aider les gens à estimer le prix d'une voiture. Pour cela, on va analyser des données pour pouvoir construire un modèle de régression capable d'estimer le prix d'une voiture à partir de différentes informations. Le jeu de données utilisé provient du site [Kaggle](https://www.kaggle.com/datasets/CooperUnion/cardataset).
- Préparer des données et réaliser d'une analyse exploratoire
- Utiliser une régression linéaire pour prédire le prix
- Comprendre ce qui se passe dans ce modèle et comment il peut prédire un prix.
- Utiliser le RMSE pour évaluer notre modèle
- Réaliser du feature engineering
- Utiliser la régularisation pour régler des problèmes en lien avec le modèle.
- Utiliser le modèle.
## 2) Régression linéaire

C'est un modèle que l'on utilise pour résoudre des problèmes de régression. On peut modéliser notre problème sous cette forme $g(X) = y$ avec : 
- *g* est notre modèle (régression linéaire)
- *X* les caractèristiques des voitures
- *y* les prix

On cherchera à avoir une fonction qui prendra $x_{i1}, x_{i2},..., x_{in}$ pour deviner les prix $y_{i1}, y_{i2}, ..., y_{in}$.

Par exemple :

On part du principe que l'on n'a besoin que de trois caractéristiques d'une voiture pour estimer son prix : la puissance, la consommation en ville et sa popularité. On représentera ces informations sous cette forme :  $x_i = [453, 11, 86]$. Pour ce cas précis, on aura une régression linéaire sous cette forme :  $g(x_{i}) = w_0 + w_1 \times x_{i1} + w_2 \times x_{i2} + w_3 \times x_{i3}$ avec :
- $w_0$ l'intercept, c'est-à-dire la valeur de y quand X est égale à 0.
- $w_1, w_2$ et $w_3$ : les poids (ou coefficients associés à des valeurs $x_i$)
- $x_{i1}, x_{i2}$ et $x_{i3}$ : les valeurs des caractéristiques de la voiture (puissance, consommation en ville et popularité).

La généralisation de la formule s'écrit de la manière suivante :
$g(x_i) = w_0 + \sum\limits_{j = 1}^n (w_j \cdot x_{ij})$

On peut l'implémenter en Python sous cette forme :
```
def linear_regression(xi):
    n = len(xi)
    
    pred = w0
    
    for j in range(n):
        pred = pred + w[j] * xi[j]
    
    return pred
```

## 3) Généralisation à une forme vectorielle

Si on reprend cette formule : $ g(x_i) = w_0 + \sum\limits_{j = 1}^n (w_j \cdot x_{ij}) $. La partie après la somme est un produit scalaire. On peut donc réécrire la formule de cette manière $g(x_i) = w_0 + x_i^T \cdot w_j$. L'implémentation en Python de cette formule est la suivante : 

```
def dot(xi, w):
    n = len(xi)
    
    res = 0.0
    
    for j in range(n):
        res = res + xi[j] * w[j]
        
    return res

def linear_regression(xi):
    return w0 + dot(xi, w)
```

Le vecteur w possède cette forme $W = [ w_0, w_1, w_2, ..., w_n]$ et le vecteur $X_i$ est égale à $X_i = [ X_{i0}, X_{i1}, X_{i2}, ..., X_{in}]$. On peut donc écrire :
$W^T \cdot X_i = X_i^T \cdot W$. 

Implémentation en Python: 

```
w_new = [w0] + w

def linear_regression(xi):
    xi = [1] + xi
    return dot(xi, w_new)
```

Après cette simplification d'écriture, on peut passer à la généralisation pour chaque voiture. Cette généralisation représente une multiplication entre une matrice X contenant les différentes caractéristiques de nos voitures et un vecteur w qui contient les poids à attribuer à ligne. Le produit scalaire de la matrice X par le vecteur w donne un vecteur y qui correspond aux prix des voitures.

```math
X =
\begin{bmatrix}
1 & X_{11} & X_{22} & ... & X_{1n}\\
1 & X_{21} & X_{22} & ... & X_{2n}\\
1 & & ...& \\
1 & X_{m1} & X_{m2} & ... & X_{mn}
\end{bmatrix}

\cdot

\begin{bmatrix}
w_0\\
w_1\\
...\\
w_n
\end{bmatrix}

= 

\begin{bmatrix}
X_1^T \cdot w\\
X_2^T \cdot w\\
...\\
X_m^T \cdot w
\end{bmatrix}

```
