# Réduction du nombre de couleurs
Pour cette seconde méthode de confession, l'objectif va être de gagner de l'espace de stockage en réduisant le nombre de couleur de l'image. Prenons l'exemple d'un nuancier de rouge :
```{figure} imgs/couleurs/nuancier_rouge.png
---
width: 200
---
Nuancier de rouge en RGB
```

Petite question d'observation : selon vous, combien de couleur sont représenté sur cette image de 16 pixels par 16 pixels ? N'essayez pas de deviner, mais de repérer le nombre de nuances différentes.

Cette image comporte 256 nuances de rouge. Elles vont du rouge pur au noir pur, en réduisant uniquement la teinte de rouge. Dans le modèle RGB classique, chaque pixel peut possède une valeur entre 256 de rouge, de vert et de bleu. Ce qui fait au total 256 * 256 * 256 couleurs possibles, donc un ordinateur est capable d'afficher exactement 16'777'216 couleurs différentes. À titre de comparaison, l'œil humain peut percevoir entre 300'000 et 8'000'000 de couleurs [^src]. Cela veut dire qu'au moins la moitié des nuances produite par un ordinateur sont imperceptibles aux meilleurs yeux humains. Il serait intéressant de pouvoir réduire le nombre de couleur sur certaines images alors. Peut-être pas une photographie de haute qualité ou une image qui aurait pour but d'être exposé, mais imaginons une affiche pour un festival, est-ce qu'il est indispensable qu'elle soit en 16 millions de couleurs ? Si maintenant une commune veut garder une trace électronique des différentes photos publiées dans ses journaux, n'aurait-elle pas meilleur temps de réduire cette valeur, cela permettra de quand même garder une forte résolution si celles-ci devraient finir par être affiché ou imprimer en grand format. L'objectif est du coup de réduire le nombre de couleurs que l'ordinateur va afficher, elles ne seront donc plus codées sur 24 Bits, mais sur 12. Cela fera passer le nombre de couleur possible de plus de 16 millions à 4'096, néanmoins cela reste emballement suffisant dans de nombreuses utilisations. Pour cette méthode de compression, il va être plus simple de regarder non pas le code RGB auquel vous êtes maintenant habitué, mais à une version un peu modifier de ce dernier : le code hexadécimal.

Le code hexadécimal a été créé pour réduire la taille que prenaient les octets à l'écran et augmenter leur lisibilité. Dans un système binaire, les symboles représentant les nombres sont *0* et *1*. En base 10, ce sont les chiffres de *0* à *9* (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). Hors, pour compter en base 16, il nous manque 6 symboles, car 11 signifie "16^1 + 16^0", pour résoudre ce problème une solution assez simple a été trouvé : après *9* vient *a* qui correspond à une valeur de *10* en base hexadécimale. La liste des symboles est donc : "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f". Un rouge parfait s'écrit alors *ff0000* et un noir parfait *000000*. Sur notre nuancier, cela nous donne ceci :

```{figure} imgs/couleurs/nuancier_rouge_gride.png
---
width: 200
---
Ce nuancier se lit de haut en bas, de gauche à droite.
```

Pour réduire le nombre de couleur, il est possible de ne choisir alors que 16 de ces nuances, maintenant, il se pose la question du choix. Qu'elles vont être les couleurs que l'on va garder pour notre nouveau nuancier ?

À première vue, il semblerait être une bonne idée de prendre la ligne supérieure ou la ligne inférieure.

```{figure} imgs/couleurs/wrong.png
---
width: 200
---
Première et dernière lignes du nuancier du rouge pur.
```

Cette intuition est malheureusement fausse, en effet, la première ligne permet d'avoir un rouge parfait, mais pas de noir absolu. À contrario, la derrière ligne permet l'inverse. Un noir absolu, mais un rouge imparfait. La bonne combinaison est en fait la diagonale.
```{figure} imgs/couleurs/right.png
---
width: 200
---
Diagonale du nuancier du rouge pur.
```
Ce choix offre la possibilité d'avoir à la fois un rouge parfait et un noir absolu. De plus, la variation entre chaque pallier reste la même. Notre nouveau nuancier de rouge comporte donc les 16 couleurs suivantes :

    ff0000
    ee0000
    dd0000
    cc0000
    bb0000
    aa0000
    990000
    880000
    770000
    660000
    550000
    440000
    330000
    220000
    110000
    000000

Un pattern s'en dégage. Les valeurs hexadécimales se répètent deux fois. Pour notre compression, nous allons alors arrondir à la valeur double la plus proche. Petit exemple :

Si notre pixel de départ à la valeur *e30000*, alors il nous l'arrondirons à *e00*. Par contre, si sa valeur originelle est de *ea0000*, alors il sera arrondi *f00*. En d'autres termes à partir du moment où le pixel aura une valeur entre *X0* et *X7*, il sera arrondi à *X* et sera arrondi à la valeur supérieure entre *X8* et *Xf*.



### Série d'exercice

1
```{figure} imgs/couleurs/exo/1.png
---
width: 200
---
```
2
```{figure} imgs/couleurs/exo/2.png
---
width: 200
---
```
3
```{figure} imgs/couleurs/exo/3.png
---
width: 200
---
```
4
```{figure} imgs/couleurs/exo/4.png
---
width: 200
---
```
5
```{figure} imgs/couleurs/exo/5.png
---
width: 200
---
```
```{warning}
Les corrigés de ces exercices se trouvent à la fin du cours.
```
## Conclusion
La compression de couleur permet donc de réduire considérablement l'espace de stockage utilisé par une image, de plus, cela évite de perdre de trop gros détails, surtout lorqu'ils sont contrastés. Problème que nous rencontrions dans la compression par réduction de résolution. Néanmoins, les images deviennent plus fades. Cela peut ne pas poser de problème lorsque l'image n'a pas pour but d'être "belle" en soi. Cependant, il y a donc toujours perte d'information avec cette méthode.



[^src] : cette information est tirée du site (https://www.guide-gestion-des-couleurs.com/couleurs-et-informatique.html)