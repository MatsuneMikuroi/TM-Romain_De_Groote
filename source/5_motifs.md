# Indentification de motifs
Pour cette dernière de compresion, l'objectif est d'identifier des motifs strict et de dire combien de fois ce dernier se répète. Reprenons notre exemple habituel en affichant une grille.
```{figure} imgs/resolution/mountains/32x32_gride.png
```
Chaque carreau contient 2 pixels, ce qui va nous aidez à compter. Par exemple, la première ligne est composée de 26 pixels blancs, codés *0*, et 6 pixels noirs, codés *1*. Il est possible de choisir un charactère qui n'est normalement pas afficher pour indiquer une multiplication. Choisissons la lettre *x* qui n'apparait normalement pas dans ce format. Il est possible de coder la première ligne
        26x0 6x1
L'ordinateur vas alors dessiner 26 pixels blancs avant d'en dessiner 6 noirs. Cette méthode est très utile lorsque le fond de l'image est uniforme. Dans notre exemple, l'ordinateur utilise au final 8 caractères au lieu de 32 pour coder la première ligne. Cela fait quand même 4 fois moins de caractères utilisés donc presque autant d'espace de stockage gagné. 

Néanmoins, il est possible de rendre un algorithme comme celui-ci encore plus performant. Prenons l'exemple d'un échiquier.
```{figure} imgs/motifs/chess.png
---
width: 300
---
```
Ce dernier est composé de 8 lignes comprenant chacune 8 cases. À première vu, il serait possible de se  dire qu'il n'est pas possible de comprimer plus cette image, néanmoins, il est possible comme en mathématiques de mettre en évidence les facteurs. Une première étape serait donc d'écrire la première ligne comme étant 4 fois un carré suivi d'un carré blanc, ce qui serait codé 4(x0 x1), puis la deuxième 4(x1 x0). 

        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)

À partir de là le piège serait de s'arrêter, or nous nous retrouverions avec une image représenter en 8 lignes de chacune 9 caratères ( le caractère de retour à la ligne est à prendre en compte), ce qui finalement reviens au même nombre que si nous n'avions pas compresser l'image. Or, nous répétons 4 fois les mêmes instructions, les lignes impaires étant semblables à la première ligne et les lignes paires à la seconde. Il est donc possible d'écrire le tout en seulement 3 lignes:

        4(4(x0 x1)
        4(x1 x0)
        )

De plus, nous avons au total 21 caratères alors que nous étions à 72 avant. L'espace que prend l'image sur le disque dur a diminué de 65%. Cela représente une quatité d'espace non négligeable. Il est important de noter que cette diminution est élever car l'exemple s'y prête bien. De plus, l'image est en noir et blanc, la couleur viendrait automatiquement rajouter de nombreux caratères inutiles. Ce genre de compression est bien plus efficaces avec de grandes images car l'effet se fera bien plus ressentir.

### Série d'exercices
:::{admonition} Consigne
Une image quadrillée vous sera montré et vous devrez la comprimer en identifiant les motifs qui la compose. Il est nécessaire de la compresser au maximum.
 :::
1
```{figure} imgs/motifs/exo/1.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
2
```{figure} imgs/motifs/exo/2.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
3
```{figure} imgs/motifs/exo/3.png
---
width: 150
---
``` 
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
4
```{figure} imgs/motifs/exo/4.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
5
```{figure} imgs/motifs/exo/5.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
6
```{figure} imgs/motifs/exo/6.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
7
```{figure} imgs/motifs/exo/7.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
8
```{figure} imgs/motifs/exo/8.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
9
```{figure} imgs/motifs/exo/9.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```
10
```{figure} imgs/motifs/exo/10.png
---
width: 150
---
```
```{figure} imgs/motifs/practise.png
---
width: 150
---
```

## Conclusion
La compression par indentifiction de motifs à un avantage considérable par rapport aux deux autres méthodes abordées précédemment : elle n'occasionne aucune perte d'information. Néamoins, l'algorithme derrière sera bien plus complexe si nous voulons que la compression reste optimale. De plus, le taux ne sera jamais aussi élevé que la réduction par résolution ou la réduction du nombre de couleurs. Un algorithme comme celui-ci peut être perfectionner en ne se bassant pas sur des valeurs de pixels mais sur l'encryptage en binnaire de l'image directement, augmentant ancore son efficacité. Un tel algorithme pourrait alors aussi être en mesure de compresser d'autres données que des images tel que des textes.