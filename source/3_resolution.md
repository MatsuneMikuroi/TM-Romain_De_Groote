# La réduction de résolution
## Représentation des images
Avant de commencer à s'attaquer à la compression pure, il est bon de comprendre la manière dont l'ordinateur représente des images.


De nos jours, tout a été numérisé. Or, contrairement à une photo prise par un appareil polaroid, qui reproduit exactement la réalité, l’ordinateur est limité dans sa représentation des images. Il ne peut pas par exemple dessiner de cercle. Cela est dû au fait que pour afficher quelque chose, l’ordinateur allume des minuscules leds formant une matrice rectangulaire. Il est d’ailleurs possible, suivant votre niveau de vue, de les distinguer si vous êtes sur ordinateur. Sinon, voici une image dont les carrés sont respectivement de 64, 32, 16, 8, 4, 2 et 1 pixels.

```{figure} imgs/resolution/exemples/pixel.png
:alt:
Le point bleu minuscule sur l'écran est de 1px*1px.
```
C’est donc à cause de cette façon de représenter les informations qu'il lui est impossible d'afficher de cercle. Néanmoins, il est possible de lui demander de créer un polygone ressemblant fortement à un cercle. Voici un exemple :

```{figure} imgs/resolution/circle/128x128.png
---
width: 128
---
Représentation d'un cercle dans un carré de 128px*128px.
```
Le cercle ci-dessus à un diamètre de 512 pixels, l'image ayant une haute résolution, la forme nous apparaît comme un cercle. Que se passerait-il maintenant si la taille de l'image était réduite ? Diminuons sa taille par un facteur 2.

```{figure} imgs/resolution/circle/64x64.png
---
width: 128
---
Représentation d'un cercle dans un carré de 64px*64px.
```
En diminuant la taille de ce cercle par 2, il devient possible de distinguer quelques endroits où les pixels semblent plus dessiner des côtés qu’une véritable courbe, comme sur le haut du cercle. Continuons de diminuer la taille de l'image, toujours avec un facteur 2.

```{figure} imgs/resolution/circle/32x32.png
---
width: 128
---
Représentation d'un cercle dans un carré de 32px*32px.
```
```{figure} imgs/resolution/circle/16x16.png
---
width: 128
---
Représentation d'un cercle dans un carré de 16px*16px.
```
Pour ces trois images, la compression rend bien visible le fait que ce ne soit pas réellement un cercle. Néanmoins, il peut encore être facilement acceptable qu'elles en représentent un. Ce qui n'est pas le cas des trois derniers niveaux de compression.

```{figure} imgs/resolution/circle/8x8.png
---
width: 128
---
Représentation d'un cercle dans un carré de 8px*8px.
```
Désormais, l'image semble plus représenter un polygone quelconque qu'un cercle, ceci nous fixe une limite : arrivé à un certain stade, une image trop comprimée peut perdre des détails essentiels à sa compréhension.

```{figure} imgs/resolution/circle/4x4.png
---
width: 128
---
Représentation d'un cercle dans un carré de 4px*4px.
```
Pour cette avant-dernière image, il n'est plus possible de répertorier cette figure comme un cercle, l'information originale a entièrement été perdue.

```{figure} imgs/resolution/circle/2x2.png
---
width: 128
---
Représentation d'un cercle dans un carré de 2px*2px.
```
Enfin, l'image a tellement été comprimée qu'il ne reste que du noir. La seule information qu'il est alors possible de supposer est que la couleur principale de l'image était le noir.

Cette petite expérience permet de démontrer qu'il n'est pas possible de réellement représenter des courbes sur un écran d'ordinateur. En effet, si cela était possible, il n'y aurait pas eu de déformation du cercle, et il aurait toujours été possible d'en voir un dans une image de 2 pixels par 2 pixels.

## Images en noir et blanc
Maintenant, il est possible de se demander comment l'ordinateur a perdu ces détails. Lorsque l'on réduit la taille d'une image, l'ordinateur va chercher quels sont les pixels les moins importants. Prenons l'exemple d'une photo d'un paysage montagneux pour comprendre.

```{figure} imgs/resolution/mountains/32x32.png
---
class: with border
---
Paysage en 32px*32px.
```
Il est possible de voir plusieurs choses sur cette image. Un soleil dans le coin supérieur droit, des montagnes en arrière-plan, des oiseaux volant au-dessus des montagnes et enfin un autre astre centré en haut. On va maintenant demander à l'ordinateur de réduire la taille de l'image par 2 en appliquant la règle de compression suivante :

Si 2px sur 4 ou plus sont noir, alors le pixel qui en résultera sera noir.

Voilà le résultat :

```{figure} imgs/resolution/mountains/black/16x16.png
---
class: with border
---
Paysage en 16px*16px.
```
L'idée de l'image reste là, néanmoins les détails ont été perdu. Pourquoi ? Les oiseaux devraient encore être visibles, du moins en partie, car ils étaient représentés dans un rectangle de 3 pixels de long par 2 de haut. Même chose pour l'astre présent dans le ciel, il faisait 2 pixels de côté. Alors pourquoi tous ces détails ont-ils disparu ? La raison est la logique utilisée pour réduire l'image. Reprenons notre première image, mais cette fois-ci mettons lui un quadrillage de 2px*2px dessus.

```{figure} imgs/resolution/mountains/32x32_gride.png
---
class: with border
---
```
L’ordinateur va à chaque fois regarder les quatre pixels présents dans chaque carré rouge et y applique la règle de compression énoncée précédemment. Il apparaît que les oiseaux sont malheureusement à chaque fois sur trois groupes différents, ce qui explique leurs disparitions. Concernant l’astre, ce dernier se trouve à l’intersection de 4 carrés, ne représentant constamment qu’un pixel sur quatre, il disparaît lui aussi. Si l'image était décalée de ne serait-ce qu'un seul pixel sur la gauche ou la droite, l'astre serait apparu, de même que si elle avait été décalée d'un pixel vers le haut ou le bas, l'astre serait visible et cette fois-ci les oiseaux aussi.

Mais reprenons notre image en 16px*16px, que se passe-t-il si l'on continue de la comprimer ?

```{figure} imgs/resolution/mountains/black/8x8.png
---
class: with border
---
Paysage en 8px*8px.
```
Comme avec le cercle, on arrive à un stade où la perte d'information devient trop grande. Avec une connaissance de l'image d'origine, il est encore possible de se la représenter, mais sans cela, c'est tout bonnement impossible.

```{figure} imgs/resolution/mountains/black/4x4.png
---
class: with border
---
Paysage en 4px*4x.
```
Arrivée à ce stade, l'image n'est même plus reconnaissable. Aucune réelle information ne peut en être tirée.

```{figure} imgs/resolution/mountains/black/2x2.png
---
class: with border
---
Paysage en 2px*2px.
```
L’image, désormais, semble révéler qu’il y avait une grande structure dans la partie inférieure de l’image, ce qui correspond aux montagnes. Néanmoins, cette information est erronée et c'est ce que le dernier stade de la compression va nous révéler.

```{figure} imgs/resolution/mountains/black/1x1.png
---
class: with border
---
Paysage en 1px*1px.
```
Comme pour le cercle, on se retrouve avec une image finale entièrement noire. Cela est dû à la présence des montagnes dans la partie inférieure. Mais quel est le problème alors ? Reprenons notre image de départ et comparons-la avec celle-ci.

```{figure} imgs/resolution/mountains/32x32.png
---
class: with border
---
Image original.
```
L'image originale est majoritairement blanche, le noir ne fait que dessiner la forme des montagnes, cependant, ces contours sont suffisants pour petit à petit faire le noir devenir majoritaire. Dans ce cas-là, la compression a tellement dégradé l'image qu'elle en a inversé les proportions des couleurs.

Essayons désormais en changeant la règle de compression.

Si plus de 2px sur 4 sont noir, alors le pixel qui en résultera sera noir.

Le changement est, en soi, minime. La seule différence étant que si 2/4 px sont noir alors le nouveau pixel sera blanc, voyons les impacts que cela a.
```{figure} imgs/resolution/mountains/white/16x16.png
---
class: with border
---
Première compression avec la nouvelle règle. (16px*16px)
```
Ce changement, bien qu'infime, vient pratiquement de faire disparaître l'image en sa totalité. Cela est dû au fait que la majorité des pixels noirs sur la première image provenait de groupes de pixels souvent à la limite du critère d'acceptabilité de la règle.
```{figure} imgs/resolution/mountains/32x32_gride.png
---
class: with border
---
Avec la vue que nous permet le quadrillage, il devient assez vite compréhensible de ces raisons.
```

Et c'est là l'un des défis de la compression de données : développer des algorithmes qui vont comprimer les images de manière à ce qu'elles prennent le moins de place possible tout en gardant un maximum d'éléments essentiels. Et ce qui est entendu par éléments essentiels change en fonction du contexte. Un fond d'écran va demander une image avec une très haute résolution et donc assez lourde, alors qu'un mème partagé sur les réseaux sociaux aura tendance à avoir une résolution plus faible, car plus l'image est légère, moins elle prendra de temps à charger et d'espace dans les serveurs de l'hébergeur des données.

 ### Série d'exercices 1
 :::{admonition} Consigne
 Dans cette première série d'exercices, une image vous sera montrée, vous devrez ensuite choisir entre deux versions compressées de cette image. Le facteur de compression sera toujours indiqué en dessous de la première image.
:::
:::{admonition} Règle de compression
---
class: attention
---
Pour tous les exercices de cette série, c'est la règle suivante qui s'applique:

        Si >=2/4 px sont noir -> nouveau pixel noir
:::
1. 
```{figure} imgs/resolution/exo/bw/1/1.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/1_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/1_right.png
---
width: 200
---
(B)
```
2. 
```{figure} imgs/resolution/exo/bw/1/2.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/2_right.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/2_wrong.png
---
width: 200
---
(B)
```
3. 
```{figure} imgs/resolution/exo/bw/1/3.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/3_right.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/3_wrong.png
---
width: 200
---
(B)
```
4. 
```{figure} imgs/resolution/exo/bw/1/4.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/4_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/4_right.png
---
width: 200
---
(B)
```
5. 
```{figure} imgs/resolution/exo/bw/1/5.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/5_right.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/5_wrong.png
---
width: 200
---
(B)
```
6. 
```{figure} imgs/resolution/exo/bw/1/6.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/6_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/6_right.png
---
width: 200
---
(B)
```
7. 
```{figure} imgs/resolution/exo/bw/1/7.png
---
width: 200
---
À comprimer avec un facteur 4.
```
```{figure} imgs/resolution/exo/bw/1/7_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/7_right.png
---
width: 200
---
(B)
```
8. 
```{figure} imgs/resolution/exo/bw/1/8.png
---
width: 200
---
À comprimer avec un facteur 4.
```
```{figure} imgs/resolution/exo/bw/1/8_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/8_right.png
---
width: 200
---
(B)
```
9. 
```{figure} imgs/resolution/exo/bw/1/9.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/9_right.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/9_wrong.png
---
width: 200
---
(B)
```
10. 
```{figure} imgs/resolution/exo/bw/1/10.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/resolution/exo/bw/1/10_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/resolution/exo/bw/1/10_right.png
---
width: 200
---
(B)
```
```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```

Cette série d'exercices permet de mettre entre autre une chose en avant: La compression des "cercles". Ceux-ci ont tendance à vite partiellement s'effacer lorsqu'on les comprime et qu'ils sont trop fins. Pour éviter ce problème, il peut être judicieux d'avoir des contours assez marqués pour toute forme un peu courbée. De plus, les petits détails ont le même problème.

### Série d'exercices 2
```{admonition} Consigne
```

1.


```{figure} imgs/resolution/exo/bw/2/latex/1.png
---
width: 300
---
```
2.


```{figure} imgs/resolution/exo/bw/2/latex/2.png
---
width: 300
---
```
3. 
```{figure} imgs/resolution/exo/bw/2/latex/3.png
---
width: 300
---
```
4. 
```{figure} imgs/resolution/exo/bw/2/latex/4.png
---
width: 300
---
```
5. 
```{figure} imgs/resolution/exo/bw/2/latex/5.png
---
width: 300
---
```
6. 
```{figure} imgs/resolution/exo/bw/2/latex/6.png
---
width: 300
---
```
7. 
```{figure} imgs/resolution/exo/bw/2/latex/7.png
---
width: 300
---
```
8. 
```{figure} imgs/resolution/exo/bw/2/latex/8.png
---
width: 300
---
```
9. 
```{figure} imgs/resolution/exo/bw/2/latex/9.png
---
width: 300
---
```
10. 
```{figure} imgs/resolution/exo/bw/2/latex/10.png
---
width: 300
---
``` 

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```

Jusqu'à présent, la compression d'images a été abordé très visuellement. Néanmoins, cela n'est faisable uniquement avec des images en noir et blanc, car dès que des nuances de gris apparraissent, il devient difficile de déterminer la nuance à appliquer. C'est pour cela que désormais les images seront affichées de deux façons: l'image en tant que telle et l'image représenté en une matrice de pixels. Pour reprendre l'exemple de l'image des montagnes, on obtiendrait ceci:
```{figure} imgs/resolution/mountains/32x32.png
---
width: 200
---
Image visible.
```
```{figure} imgs/resolution/mountains/32x32_px.png
---
width: 200
---
Image "vue" par l'ordinateur.
```

Il est possbile de voir que l'ordinateur représente les pixels blancs par des *0* et les pixels noirs par des *1*
:::{admonition} Format utilisé
---
class: attention
---
Toute la théorie concernant la façon dont l'ordinateur représente les images n'est applicable qu'au fichiers PBM, PGM et PPM (mêmes si ils de légèrent variations). Ces formats ont été retenu car la majorité des formats d'images ont leur propre manière de les stocker et coder. L'avantage des format PBM/PGM/PPM est qu'ils sont très peu comprimés mais très compréhensibles pour des néophyte. Ceux-ci représentant les pixels par des valeurs uniquement numériques et laissant facilement apparaître les images.

## Images en nuances de gris
Maintenant que vous maîtrisez la représentation des images avec des valeurs et plus des couleurs, il est possible de s'attaquer à la compression d'images en nuances de gris. Il existe deux différences entre la compression en noir/blanc et celle en nuance de gris :
* Les valeurs ne sont plus *0* pour blanc et *1* pour noir, mais *0* pour noir et *15* pour blanc, chaque pallier intermédiaire correspondant à un niveau de gris. Cette différence est juste due au format utilisé. Les images en noir/blanc étaient des fichiers PBM alors celles en nuances de gris sont en PGM.
```{figure} imgs/resolution/exemples/nuances.png
---
class: with border
---
Nuancier du format PGM.
```
* La règle de compression à laquelle vous êtes habituée va légèrement se complexifier :
        trunc((valeur totale/nombre de pixel total) + 0.5) = valeur du nouveau pixel.

:::{tip} Conseil
        l'expression "trunc"

En précisant cette règle, la compression des images en noir et blanc fonctionne toujours, néanmoins, il est désormais possible de l'appliquer aux images en nuances de gris.
### Série d'exercices 1
:::{admonition} Consigne
 Cette première série d'exercices ressemble à la première des images en noir/blanc. Une image vous sera montrée, vous devrez ensuite choisir entre deux versions compressées de cette image. Le facteur de compression sera toujours indiqué en dessous de la première image.
:::
:::{admonition} Règle de compression
---
class: attention
---
Pour tous les exercices de cette série, c'est la règle suivante qui s'applique:

        int(valeur totale/nombre de pixel total) = valeur du nouveau pixel
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

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```

Ces exercices ont permis de mettre en lumière quelque-chose, les images semblent mieux proportionnées. Là où la compression en noir blanc avait tendance à vite perdre des informations, la compression en nuances de gris garde toujours une trace de tous pixels. Des zones plus claires indiquant la présence de pixels plus clairs en moyenne. Cela permet aussi d'éviter un changement de proportion entre clair et obscur. Là où nous avions vu que notre règle pouvait changer la proportion de pixels noirs et de pixels blancs, la compression en nuance de gris ne pourra donner un pixel noir comme compression finale si l'image était majoritairement blanche.

### Série d'exercices 2
:::{warning}
Cette série d'exercices varie selon si le script est en version papier ou en version web. Dans les deux cas des solutions seront proposées aux élèves. Néanmoins, la version web étant automatisée, la correction sera plus terre-à-terre.
:::

```{admonition} Consigne
Pour cette deuxième série d'exercices, vous aurez besoin, comme pour certaines séries de la compression en noir/blanc, d'une feuille cadrillée ainsi que de quoi écrire. Pour chacune des images qui suivront, vous devrez effectuer leur conversion avec le facteur donné, cette fois-ci en indiquant la valeur de chaque pixel.
```
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

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```

## La compression d'images en couleur
Pour finir ce chapitre sur la compression d'images par réduction de résolution, nous allons nous intéressé aux images en couleur. Le format utilisé est le PPM, ce dernier fonctionne comme le PBM et le PGM, la seule différence étant qu'il ne représente plus les couleurs des pixels par un nombre mais par une combinaison de trois nombre.
```{figure} imgs/exemples/color.png
9 couleurs "simples" en RGB.
```
L'image ci-dessus représenté comme une matrice dont les valeurs sont données en RGB. Petit point d'optique:

La lumière est composée de particules nommées photons, chacun possèdant une certaine longueur d'onde. Lorsqu'un photon vient taper l'oeil humain, il active des cellules réceptrices. Néanmoins, avec des photons dans les longueurs d'ondes des rouges, verts et bleus, il est en fait possible de produire toutes les couleurs visibles. Les pixels étant finalement que trois leds disposées côte à côte. Un pixel est noir lorsque toutes ses leds sont éteintes, il est blanc lorsqu'elles sont toutes allumées. Enfin, il est dans une nuance de gris si l'intensité en rouge est égale à celle en verte et en bleue. Sur l'image au-dessus (de gauche à droite), le premier carreau n'est composé que de pixels allumé sur la leds rouge uniquement. Le second des pixels dont seuls les leds vertes sont allumées et la troisième dont ce sont les leds bleues. Pour la seconde ligne, pour le carreau jaune ce sont les leds rouges et vertes qui sont allumées, pour le cyan les leds vertes et bleues, pour le magenta les leds bleues et rouges. Enfin, la troisième ligne est composée d'un carreau blanc, donc toutes ses leds sont allumées au maximum; d'un carreau gris, dont toutes les leds sont à la moitié de leur intensité maxiamle; finalement un carreau noir dont l'entièreté des leds sont éteintes. Représenté sous forme d'un tableau, nous obtenons ceci:
```{figure} imgs/exemples/colors_values.png
Représentations en valeurs RGB du carré coloré au dessus.
```
 Cependant, comme dit précédement, le format en couleur représente ses pixels sous formes d'un trio de valeur. Pour comprimer les images il faut alors reprendre la règle que nous avions utilisé pour la compression en nuances de gris et la modifier légèrement.
       int(valeur rouge totale/nombre de pixel total) = valeur rouge du nouveau pixel.

       int(valeur verte totale/nombre de pixel total) = valeur verte du nouveau pixel.

       int(valeur bleue totale/nombre de pixel total) = valeur bleue du nouveau pixel.

Cette version finale de la règle permet donc de représenté 256^3 de couleur (256 nuances en rouge * 256 nuances en vert * 256 nuances en bleu).


### Série d'exercices 1
:::{admonition} Consigne
 Cette première série d'exercices ressemble à la première des images en noir/blanc. Une image vous sera montrée, vous devrez ensuite choisir entre deux versions compressées de cette image. Le facteur de compression sera toujours indiqué en dessous de la première image.
:::
:::{admonition} Règle de compression
---
class: attention
---
Pour tous les exercices de cette série, c'est la règle suivante qui s'applique:

        Si >=2/4 px sont noir -> nouveau pixel noir
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

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```


### Série d'exercices 2
:::{warning}
Cette série d'exercices varie selon si le script est en version papier ou en version web. Dans les deux cas des solutions seront proposées aux élèves. Néanmoins, la version web étant automatisée, la correction sera plus terre-à-terre.
:::

```{admonition} Consigne
Pour cette dernière série d'exercices, vous aurez besoin, comme pour certaines séries de la compression en noir/blanc, d'une feuille cadrillée ainsi que de quoi écrire. Pour chacune des images qui suivront, vous devrez effectuer leur conversion avec le facteur donné, cette fois-ci en indiquant la valeur de chaque pixel.
```
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

```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```
## Conclusion
