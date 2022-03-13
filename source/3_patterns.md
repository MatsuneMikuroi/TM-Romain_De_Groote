# Indentification de patterns
Une autre méthode pour comprimer des données est d'identifier un pattern strict et de dire combien de fois ce dernier se répète. Reprenons notre exemple habituel en affichant une grille.
```{figure} imgs/mountains/32x32_gride.png
```
Chaque carreau contient 2 pixels, ce qui va nous aidez à compter. Par exemple, la première ligne est composée de 26 pixels blancs, codés *0*, et 6 pixels noirs, codés *1*. Il est possible de choisir un charactère qui n'est normalement pas afficher pour indiquer une multiplication. Choisissons la lettre *x* qui n'apparait normalement pas dans ce format. Il est possible de coder la première ligne
        26x0 6x1
L'ordinateur vas alors dessiner 26 pixels blancs avant d'en dessiner 6 noirs. Cette méthode est très utile lorsque le fond de l'image est uniforme. Dans notre exemple, l'ordinateur utilise au final 8 caractères au lieu de 32 pour coder la première ligne. Cela fait quand même 4 fois moins d'espace. 

## Série d'exercices 1
:::{admonition} Consigne
 Dans cette unique série d'exercices de ce chapitre, une image quadrillé vous sera montré et vous devrez la comprimer en identifiant les patterns qui la compose. Les images seront issus des exercices précédents.
:::
:::{raw} html
<iframe src="https://brython.info/gallery/phaser.html" width="100%" height="600"></iframe>
:::

:::{raw} latex
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
:::