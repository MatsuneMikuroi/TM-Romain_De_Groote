# Réduction du nombre de couleurs
Pour cette seconde méthode de copression, l'objectif va être de gagner de l'espace de stockage en réduisant le nombre de couleur de l'image. Prenons l'exemple d'un nuancier de rouge :
```{figure} imgs/couleurs/nuancier_rouge.png
---
width: 150
---
```


Petite question d'observation: selon vous, combien de couleur sont représenté sur cette image de 16 pixels par 16 pixels ? N'essayez pas de deviner mais de repérer le nombre de nuances différentes.

Cette image comporte 256 nuances de rouge. Elles vont du rouge pur au noir pur, en réduisant uniquement la teinte de rouge. Dans le modèle RGB classique, chaque pixel peut possède une valeur entre 256 de rouge, de vert et de bleu. Ce qui fait au total 256 * 256 * 256 couleurs possibles, donc un ordinateur est capable d'afficher exactement 16'777'216 coueleurs différentes. À titre de comparaison, l'oeil humain peut percevoir entre 300'000 et 8'000'000 de couleurs [^src]. Cela veut dire qu'au moins la moitié des nuances produite par un ordinateur sont imperceptibles aux meilleurs yeux humains. Il serait intéressant de pouvoir réduire le nombre de couleur sur certaines images alors. Peut-être pas une photographie de haute qualité ou une image qui aurait pour but d'être exposé, mais imaginons une affiche pour un festival, est-ce qu'il est indispensable qu'elle soit en 16 millions de couleurs ? Si maintenant une commune veut garder une trace électronique des différentes photos publiées dans ses journaux, n'aurait-elle pas meilleure temps de réduire cette valeur, cela permettra de quand même garder une forte résolution si celles-ci devrait finir par être afficher ou imprimer en grand format. L'objectif est du coup de réduire le nombre de couleurs que l'ordinateur va afficher, elles ne seront donc plus codées sur 24 Bits mais sur 12. Cela fera passer le nombre de couleur possible de plus de 16 millions à 4096, néamoins cela reste emblement suffisant dans de nombreuses utilisations.

### Série d'exercice
1
```{figure} imgs/couleurs/exo/1.png
---
width: 150
---
```
2
```{figure} imgs/couleurs/exo/2.png
---
width: 150
---
```
3
```{figure} imgs/couleurs/exo/3.png
---
width: 150
---
``` 
4
```{figure} imgs/couleurs/exo/4.png
---
width: 150
---
```
5
```{figure} imgs/couleurs/exo/5.png
---
width: 150
---
```
6
```{figure} imgs/couleurs/exo/6.png
---
width: 150
---
```
7
```{figure} imgs/couleurs/exo/7.png
---
width: 150
---
```
8
```{figure} imgs/couleurs/exo/8.png
---
width: 150
---
```
9
```{figure} imgs/couleurs/exo/9.png
---
width: 150
---
```
10
```{figure} imgs/couleurs/exo/10.png
---
width: 150
---
```
## Conclusion

[^scr]: cette information est tirée du site (https://www.guide-gestion-des-couleurs.com/couleurs-et-informatique.html)