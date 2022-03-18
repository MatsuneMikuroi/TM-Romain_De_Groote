# Indentification de motifs
Une autre méthode pour comprimer des données est d'identifier un pattern strict et de dire combien de fois ce dernier se répète. Reprenons notre exemple habituel en affichant une grille.
```{figure} imgs/mountains/32x32_gride.png
```
Chaque carreau contient 2 pixels, ce qui va nous aidez à compter. Par exemple, la première ligne est composée de 26 pixels blancs, codés *0*, et 6 pixels noirs, codés *1*. Il est possible de choisir un charactère qui n'est normalement pas afficher pour indiquer une multiplication. Choisissons la lettre *x* qui n'apparait normalement pas dans ce format. Il est possible de coder la première ligne
        26x0 6x1
L'ordinateur vas alors dessiner 26 pixels blancs avant d'en dessiner 6 noirs. Cette méthode est très utile lorsque le fond de l'image est uniforme. Dans notre exemple, l'ordinateur utilise au final 8 caractères au lieu de 32 pour coder la première ligne. Cela fait quand même 4 fois moins de caractères utilisés donc presque autant d'espace de stockage gagné. 

Néanmoins, il est possible de rendre un algorithme comme celui-ci encore plus performant. Prenons l'exemple d'un échiquier. Ce dernier est composé de 8 lignes comprenant chacune 8 cases. À première vu, il serait possible de se  dire qu'il n'est pas possible de comprimer plus cette image, néanmoins, il est possible comme en mathématiques de mettre en évidence les facteurs. Une première étape serait donc d'écrire la première ligne comme étant 4 fois un carré suivi d'un carré blanc, ce qui serait codé 4(x0 x1), puis la deuxième 4(x1 x0). 

        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)
        4(x0 x1)
        4(x1 x0)

À partir de là le piège serait de s'y arrêter, or nous nous retrouverions avec une image représenter en 8 lignes de chacune 9 caratères ( le caractère de retour à la ligne est à prendre en compte), ce qui finalement reviens au même nombre que si nous n'avions pas compresser l'image. Or, nous répétons 4 fois les mêmes instructions, les lignes impaires étant semblables à la première ligne et les lignes paires à la seconde. Il est donc possible d'écrire le tout en seulement 2 lignes:

        4(4(x0 x1)
        4(x1 x0)
        )

De plus, nous avons au total 21 caratères alors que nous étions à 72 avant. L'espace que prend l'image sur le disque dur a diminué de 65%. Cela représente une quatité d'espace non négligeable.

## Série d'exercices 1
:::{admonition} Consigne
 Dans cette unique série d'exercices de ce chapitre, une image quadrillée vous sera montré et vous devrez la comprimer en identifiant les patterns qui la compose. Les images seront issus des exercices précédents.
 :::
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```