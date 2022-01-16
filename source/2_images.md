# La compression d'images
## Objectifs
L'objectif de ce chapitre va-t-être d'enseigner le principe de la compression d'image au travers d'exercices.
:::{raw} Latex
Les élèves ont également un corrigé détaillé en fin de chapitre concernant les exercices inclus dans le script.
:::
Nous nous attarderons en premier temps sur la compression d'images par réduction de résolution avant de s'attaquer à la compression par identifiacation de patterns.

La compression par réduction de résolution vise à réduire le nombre de pixels qui composent une image. En le réduisant, l'image prendra moins de place. Pour cette première partie, les formats PBM, PGM et PPM seront utilisé car très visuel et basique. Ils est possible de convertir les images sous ces formats en fichiers textes et celles-ci sont codées de la manière suivante: 
* L'indication du format (P1 pour un fichier PBM en ASCII et P4 en binaire, P2 pour un fichier PGM en ASCII et P5 en binaire, enfin P3 pour un fichier PPM en ASCII et P& en binaire).
* Le nombre de colonnes de pixels dans l'images (toujours sous la forme d'un nombre ASCII).
* Le nombre de ligne de pixels dans l'images (toujours sous la forme d'un nombre ASCII).
* L'image codée ligne par ligne
* Toute ligne commençant par '#' est perçu comme un commentaire

Pour le format PBM, la valeur '1' indique que le pixel est noir alors que la valeur '0' indique qu'il est blanc. Concernant le PGM, les différentes nuances de grise sont comprises entre '0' et '15' où '0' correspond au noir et '15' au blanc. Finalement, le PPM code chaque pixel en valeur RGB, donc '255 0 0' donne du rouge, '0 255 0' du vet et '0 0 255' du bleu.

Dans la théorie, nous allons commencé avec par compression en noir et blanc car elle permet de facillement imager le tout. Les pixels après compresions étant alors soit noir soit blanc. Deux séries d'exercices permettrons ensuite à l'élève de s'entrainer. Il devra dans un premier temps choisir entre deux images et choisir laquelle des deux est issu de la compression d'un modèle, dans la deuxième série une image lui sera montrer et l'élève devra par lui même effetuer la compression. Suite à ces premiers exercices, les couleurs seront petit à petit délaissées au profit des valeurs numériques. Des exercices semblablent aux deux premières séries seront proposés avant de passer à la compression en nuances de gris. À partir de là, les séries se répèteront, le type d'exercice ne variant que très peu, néanmoins la difficulté sera croissante. La dernière partie se consacrera à la compression d'image en couleurs. La difficulté supplémetaire sera de vérifier les trois valeurs RGB. Après avoir fini la compression par réduction de résolution, nous passeront à la compression par identifiction de patterns.

Cette dernière va permettre de passer de la compression d'images à la compression de texte. Ce chapitre aussi beaucoup plus court que le premier. Il ne contiendra qu'un peu de théorie et une série d'exercice, mélangeant des images en noir/blanc, nuances de gris et couleurs.

## La réduction de résolution
### Représentation des images
Avant de commencer à s'attquer à la compression pure, il est bon de comprendre la manière dont l'ordinateur représente des images.


De nos jours, tout a été numérisé. Or, contrairement à une photo prise par un appareil polaroid, qui reproduit exactement la réalité, l’ordinateur est limité dans sa représentation des images. Il ne peut pas exemple par dessiner de cercle. Cela est dû au fait que pour afficher quelque chose, l’ordinateur allume des minuscules leds formant une matrice rectangulaire. Il est d’ailleurs possible, suivant votre niveau de vue, de les distinguer si vous êtes sur ordinateur. Sinon, voici une image dont les carrés sont respectivement de 64, 32, 16, 8, 4, 2 et 1 pixels.

```{figure} imgs/exemples/pixel.png
:alt:
Le point bleu minuscule sur l'écran est de 1px*1px. Cette image est surtout utile si le script est en version informatique.
```
 C’est donc à cause de cette façon de représenter les information qu'il lui est impossible  d'afficher de cercle. Néanmoins, il est possible de lui demander de créer un polygone ressemblant fortement à un cercle. Voici un exemple :

```{figure} imgs/circle/512x512.png
Représentation d'un cercle dans un carré de 512px*512px.
```
Le cercle ci-dessus à un diamètre de 512 pixels, l'image ayant une haute résolution, la forme nous apparait comme un cercle. Que se se passerait-il maintenant si la taille de  l'image était réduite ? Diminuons sa taille par un facteur 2.

```{figure} imgs/circle/256x256.png
---
width: 256
---
Représentation d'un cercle dans un carré de 256px*256px.
```
En diminuant la taille de ce cercle par 2, il devient possible de distinguer quelques endroits où les pixels semblent plus dessiner des cotés qu’une véritable courbe, comme sur le haut du cercle. Continuons de diminuer la taille de l'image, toujours avec un facteur 2.

```{figure} imgs/circle/128x128.png
---
width: 256
---
Représentation d'un cercle dans un carré de 128px*128px.
```
Il devient maintenant plus évident que ce qui ressemblait à un cercle commence à devenir un polygone avec un très grand nombre de côté. Le haut semble commencer à s'applatir. Si l'on continue cela nous donne les résultats suivants:

```{figure} imgs/circle/64x64.png
---
width: 256
---
Représentation d'un cercle dans un carré de 64px*64px.
```
```{figure} imgs/circle/32x32.png
---
width: 256
---
Représentation d'un cercle dans un carré de 32px*32px.
```
```{figure} imgs/circle/16x16.png
---
width: 256
---
Représentation d'un cercle dans un carré de 16px*16px.
```
Pour ces trois images, la compression rend bien visible le fait que ce ne soit pas réellement un cercle. Néanmoins il peut encore être facilement acceptable qu'elles en représentent un. Ce qui n'est pas le cas des trois derniers niveaux de compression.

```{figure} imgs/circle/8x8.png
---
width: 256
---
Représentation d'un cercle dans un carré de 8px*8px.
```
Désormais, l'image semble plus représenter un polygone quelconque qu'un cercle, ceci nous fixe une limite : arriver à un certain stade, une image trop comprimée peut perdre des détails essentiels à sa compréhension.

```{figure} imgs/circle/4x4.png
---
width: 256
---
Représentation d'un cercle dans un carré de 4px*4px.
```
Pour cette avant dernière image, il n'est plus possible de répertorier cette figure comme un cercle, l'information originale a entièrement été perdue.

```{figure} imgs/circle/2x2.png
---
width: 256
---
Représentation d'un cercle dans un carré de 2px*2px.
```
Enfin, l'image à tellement été comprimé qu'il ne reste que du noir. La seule information qu'il est alors possible de supposer est que la couleur principale de l'image était le noir.

Cette petite expérience permet de démontrer qu'il n'est pas possible de réellement représenter des courbes sur un écran d'ordinateur. En effet, si cela était possible, il n'y aurait pas eu de déformation du cercle, et il aurait toujours été possible d'en voir un dans une image de 2 pixels par 2 pixels.

### Images en noir et blanc
Maintenant, il est possible de se demander comment l'ordinateur a perdu ces détails. Lorsque l'on réduit la taille d'une image, l'ordinateur va chercher quels sont les pixels les moins importants. Prenons l'exemple d'une photo d'un paysage montagneux pour comprendre.

```{figure} imgs/mountains/32x32.png
---
class: with border
---
Paysage en 32px*32px.
```
Il est possible de voir plusieurs choses sur cette image. Un soleil dans le coin supérieur droit, des montagnes en arrière-plan, des oiseaux volant au dessus des montagnes et enfin un autre astre centré en haut. On va maintenant demander à l'ordinateur de réduire la taille de l'image par 2 en appliquant la règle de compression suivante:

        Si >=2/4 px sont noir -> nouveau pixel noir

Voilà le résultat:

```{figure} imgs/mountains/black/16x16.png
---
class: with border
---
Paysage en 16px*16px.
```
L'idée de l'image reste là, néanmoins les détails ont été perdu. Pourquoi ? Les oiseaux devraient encore être visibles, du moins en partie, car ils étaient représentés dans un rectangle de 3 pixels de long par 2 de haut. Même chose pour l'astre présent dans le ciel, il faisait 2 pixels de côté. Alors pourquoi tous ces détails ont-ils disparu ? La raison est la logique utilisée pour réduire l'image. Reprenons notre première image mais cette fois-ci mettons lui un cadrillage de 2px*2px dessus.

```{figure} imgs/mountains/32x32_gride.png
---
class: with border
---
```
L’ordinateur va à chaque fois regarder les quatre pixels présents dans chaque carré rouge et y applique la règle de compression énoncée précédemment. Il apparaît que les oiseaux sont malheureusement à chaque fois sur trois groupes différents, ce qui explique leurs disparitions. Concernant l’astre, ce dernier se trouve sur l’intersection de 4 carrés, ne représentant constamment qu’un pixel sur quatre, il disparait lui aussi. Si l'image était décallée de ne serait-ce qu'un seul pixel sur la gauche ou la droite, l'astre serait apparu, de même que si elle avait été décallée d'un pixel vers le haut ou le bas, l'astre serait visible et cette fois-ci les oiseaux aussi.

Mais reprenons notre image en 16px*16px, que se passe-t-il si l'on continue de la comprimer ?

```{figure} imgs/mountains/black/8x8.png
---
class: with border
---
Paysage en 8px*8px.
```
Comme avec le cercle, on arrive à un stade où la perte d'information devient trop grande. Avec une connaissance de l'image d'origine, il est encore possible de se la représenter, mais sans cela, c'est tout bonnement impossible.

```{figure} imgs/mountains/black/4x4.png
---
class: with border
---
Paysage en 4px*4x.
```
Arrivée à ce stade, l'image n'est même plus reconnaissable. Aucune réelle information ne peut en être tirée.

```{figure} imgs/mountains/black/2x2.png
---
class: with border
---
Paysage en 2px*2px.
```
L’image désormais semble révélé qu’il y avait une grande structure dans la partie inférieure de l’image, ce qui correspond aux montagnes. Néanmoins cette information est erronée et c'est ce que le dernier stade de la compression va nous révéler.

```{figure} imgs/mountains/black/1x1.png
---
class: with border
---
Paysage en 1px*1px.
```
Comme pour le cercle, on se retrouve avec une image finale entièrement noire. Cela est dû à la présence des montagnes dans la partie inférieure. Mais quel est le problème alors ? Reprenons notre image de départ et comparons là avec celle-ci.

```{figure} imgs/mountains/32x32.png
---
class: with border
---
Image originale.
```
L'image originale est majoritairement blanche, le noir ne fait que dessiner la forme des montagnes, cependant, ces contours sont suffisants pour petit à petit le faire devenir majoritaire. Dans ce cas-là, la compression a tellement dégradé l'image qu'elle en a inversé les proportions des couleurs.

Essayons désormais en changeant la règle de compression.

        Si >2/4 px sont noirs -> nouveau pixel noir

Le changement est, en soi, minime. La seule différnce étant que si 2/4 px sont noir alors le nouveau pixel sera blanc, voyons les impacts que cela a.
```{figure} imgs/mountains/white/16x16.png
---
class: with border
---
Première compression avec la nouvelle règle. (16px*16px)
```
Ce changement, bien qu'infime, vient pratiquement de faire disparaître l'image en sa totalité. Cela est dû au fait que la majorité des pixels noirs sur la première image provenait de groupes de pixels souvent à la limite du critère d'acceptabilité de la règle.
```{figure} imgs/mountains/32x32_gride.png
---
class: with border
---
Avec la vue que nous permet le cadrillage, il devient assez vite compréhensible de ces raisons.
```

 Et c'est là l'un des défis de la compression de données: développer des algorithmes qui vont comprimer les images de manière à ce qu'elles prennent le moins de place possible tout en gardant un maximum d'éléments essentiels. Et ce qui est entendu par éléments essentiels change en fonction du contexte. Un fond d'écran va demander une image avec une très haute résolution et donc assez lourde, alors qu'un mème partager sur les réseaux sociaux aura tendance à avoir une résolution plus faible, car plus l'image est légère, moins elle prendra de temps à charger et d'espace dans les serveurs de l'hebergeur des données.

 #### Série d'exercices 1
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
```{figure} imgs/exo/bw/1/1.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/1_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/1_right.png
---
width: 200
---
(B)
```
2. 
```{figure} imgs/exo/bw/1/2.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/2_right.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/2_wrong.png
---
width: 200
---
(B)
```
3. 
```{figure} imgs/exo/bw/1/3.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/3_right.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/3_wrong.png
---
width: 200
---
(B)
```
4. 
```{figure} imgs/exo/bw/1/4.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/4_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/4_right.png
---
width: 200
---
(B)
```
5. 
```{figure} imgs/exo/bw/1/5.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/5_right.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/5_wrong.png
---
width: 200
---
(B)
```
6. 
```{figure} imgs/exo/bw/1/6.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/6_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/6_right.png
---
width: 200
---
(B)
```
7. 
```{figure} imgs/exo/bw/1/7.png
---
width: 200
---
À comprimer avec un facteur 4.
```
```{figure} imgs/exo/bw/1/7_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/7_right.png
---
width: 200
---
(B)
```
8. 
```{figure} imgs/exo/bw/1/8.png
---
width: 200
---
À comprimer avec un facteur 4.
```
```{figure} imgs/exo/bw/1/8_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/8_right.png
---
width: 200
---
(B)
```
9. 
```{figure} imgs/exo/bw/1/9.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/9_right.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/9_wrong.png
---
width: 200
---
(B)
```
10. 
```{figure} imgs/exo/bw/1/10.png
---
width: 200
---
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/bw/1/10_wrong.png
---
width: 200
---
(A)
```
```{figure} imgs/exo/bw/1/10_right.png
---
width: 200
---
(B)
```
```{warning}
Les corrigés de ces exercices se trouvent en fin de chapitre.
```

Cette série d'exercices permet de mettre entre autre une chose en avant: La compression des "cercles". Ceux-ci ont tendance à vite partiellement s'effacer lorsqu'on les comprime et qu'ils sont trop fins. Pour éviter ce problème, il peut être judicieux d'avoir des contours assez marqués pour toute forme un peu courbée. De plus, les petits détails ont le même problème.

#### Série d'exercices 2
:::{warning}
Cette série d'exercices varie selon si le script est en version papier ou en version web. Dans les deux cas des solutions seront proposées aux élèves. Néanmoins, la version web étant automatisée, la correction sera plus terre-à-terre.
:::

::::{raw} html

```{admonition} Conseil
Dans cette deuxième série d'exercices, vous allez pouvoir vous entrainez sur l'ordinateur directement. La fenêtre d'exécution en dessous, une fois lancée, vous montrera une image et vous devrez la compresser. Vous n'avez qu'à faire un clic pour passer de blanc à noir et inversemment. Il est possible de relancer le programme pour avoir une nouvelle image.
```

<iframe src="https://brython.info/gallery/phaser.html" width="100%" height="600"></iframe>

::::
:::{raw} latex
```{admonition} Consigne
Pour cette série d'exercices, vous aurez besoin d'une feuille cadrillée ainsi que de quoi écrire. Pour chacune des images qui suivront, vous devrez effectuer leur conversion avec le facteur donné.
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
:::


Jusqu'à présent, la compression d'images a été abordé très visuellement. Néanmoins, cela n'est faisable uniquement avec des images en noir et blanc, car dès que des nuances de gris apparraissent, il devient difficile de déterminer la nuance à appliquer. C'est pour cela que désormais les images seront affichées de deux façons: l'image en tant que telle et l'image représenté en une matrice de pixels. Pour reprendre l'exemple de l'image des montagnes, on obtiendrait ceci:
```{figure} imgs/mountains/32x32.png
---
width: 200
---
Image visible.
```
```{figure} imgs/mountains/32x32_px.png
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
:::

#### Série d'exercices 3
:::{admonition} Consigne
 Cette troisième série d'exercices ressemble à la première. Une image vous sera montrée, vous devrez ensuite choisir entre deux versions compressées de cette image. Le facteur de compression sera toujours indiqué en dessous de la première image.
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

Les co

## Indentification de patterns
Une autre méthode pour comprimer des données est d'identifier un pattern strict et de dire combien de fois ce dernier se répète. Reprenons notre exemple habituel en affichant une grille.
```{figure} imgs/mountains/32x32_gride.png
```
Chaque carreau contient 2 pixels, ce qui va nous aidez à compter. Par exemple, la première ligne est composée de 26 pixels blancs, codés *0*, et 6 pixels noirs, codés *1*. Il est possible de choisir un charactère qui n'est normalement pas afficher pour indiquer une multiplication. Choisissons la lettre *x* qui n'apparait normalement pas dans ce format. Il est possible de coder la première ligne
        26x0 6x1
L'ordinateur vas alors dessiner 26 pixels blancs avant d'en dessiner 6 noirs. Cette méthode est très utile lorsque le fond de l'image est uniforme. Dans notre exemple, l'ordinateur utilise au final 8 caractères au lieu de 32 pour coder la première ligne. Cela fait quand même 4 fois moins d'espace. 

### Série d'exercices 1
:::{admonition} Consigne
 Dans cette unique série d'exercices de ce chapitre, une image quadrillé vous sera montré et vous devrez la comprimer en identifiant les patterns qui la compose. Les images seront issus des exercices précédents.
:::
:::{raw} html
<iframe src="https://brython.info/gallery/phaser.html" width="100%" height="600"></iframe>
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



## Conclusion
Pour conclure ce chapitre, il est important de retenir que les images vont en vérité être comprimer de manière quasi-systématique. Comme il s'agit de l'une des principales informations, étant aussi à la base des vidéos, il est important que ces dernières ne remplissent pas l'intégralité de l'espace de stockage que nous possèdons. Les allégées permets aussi de se les échanger plus rapidement. Néanmoins, une image comprimée ne va pas forcément perdre de sa qualité. Il existe, en plus des deux types de compressions abordés, une troisième manière de comprimer les images, celle-ci visant à baisser le nombre de couleur qu'il est possible d'afficher.

## Solutions des exercices
### Réduction de résolution
#### Images en noir et blanc
##### Série d'exercices 1
###### Réponses
Les bonnes réponses étaient
1. (B)
2. (A)
3. (A)
4. (B)
5. (A)
6. (B)
7. (B)
8. (B)
9. (A)
10. (B)
###### Explications
1. 
```{figure} imgs/exo/bw/1/1_wrong_explain.png
---
width: 200
---
```
2. 
```{figure} imgs/exo/bw/1/2_wrong_explain.png
---
width: 200
---
```
3. 
```{figure} imgs/exo/bw/1/3_wrong_explain.png
---
width: 200
---
```
4. 
```{figure} imgs/exo/bw/1/4_wrong_explain.png
---
width: 200
---
```
5. 
```{figure} imgs/exo/bw/1/5_wrong_explain.png
---
width: 200
---
```
6. 
```{figure} imgs/exo/bw/1/6_wrong_explain.png
---
width: 200
---
```
7. 
```{figure} imgs/exo/bw/1/7_wrong_explain.png
---
width: 200
---
```
8. 
```{figure} imgs/exo/bw/1/8_wrong_explain.png
---
width: 200
---
```
9. 
```{figure} imgs/exo/bw/1/9_wrong_explain.png
---
width: 200
---
```
10. 
```{figure} imgs/exo/bw/1/10_wrong_explain.png
---
width: 200
---
```
##### Série d'exercices 2
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

##### Série d'exercices 3
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

##### Série d'exercices 4
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

#### Images en nuances de gris
##### Série d'exercices 1
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

##### Série d'exercices 2
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

#### Images en couleur
##### Série d'exercices 1
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

##### Série d'exercices 2
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


### Identification de patterns
#### Série d'exercices 1
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



## Explications des algorithmes
 :::{admonition} Prérequis
---
class: attention
---
Pour comprendre le fonctionnement des algorithmes suivants, il est conseillé d'avoir quelques connaissances sur le fonctionnement et les manipulations des listes en python.
:::

### Lecture des images
Dans ce chapitre,  les images utilisés sont sous format PBM, PGM et PPM. Ces formats ont deux particulartié intéresantes:
1. Il est possible de les transformer en fichier *.txt* juste en les renommant.
2. Ces fichiers *.txt* se présentent sous la forme suivante:
```{figure} imgs/exemples/txt.png
Fichier PBM mis en fichier texte.
```
Il est visible de voir, comme expliqué dans le cours, que la valeur des pixels est indiqué tel quel, sous la forme de liste. 
### Inversion des coordonnées
Pour la compression d’images, il a fallu commencer par une restructuration des listes. En effet dans le langage courant, nous lisons les informations de gauche à droite et de haut en bas, or, lorsque nous soutirons une image sous forme de liste de listes de pixels, l’ordinateur nous renvoi une liste qui se lit de haut en bas et de gauche à droite.

        Par exemple la liste [[1,0,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,0,0,1],[1,0,0,0,1]],
        nous donne l'image suivante:
```{figure} imgs/exemples/z.png
---
class: with border
---
```

 Le premier algorithme à développer devait donc inverser les coordonnées x y des images.
 
En premier temps, on définit une fonction ayant en paramètre une *list* et qui renvoie une *list*.
```python
def switch_xy(imgxy:list)->list:
```
Une fois chose faite, on initie trois variables:
* une liste vide dans laquelle on viendra par la suite rentrer les nouvelles coordonnées
```python
 imgyx: str = []
```
* deux variables de confort
```python
coord_x = len(imgxy)
coord_y = len(imgxy[0])
```
:::{admonition} Conseil
---
class: tip
---
Ces deux variables éviteront des erreurs entre les coordonnées. Concernant la deuxième, le fait de regarder la longueur de la première sous-liste permet de la définir car toutes les sous-listes ont le même nombre d'éléments, une image étant forcément rectangulaire.
:::

Ensuite on vient créer une image de même dimension mais entièrement blanche avec la boucle *for* suivante:
```python
for i in range(coord_y):
    imgyx.append([0]*coord_x)
```
Après, il ne reste plus qu'à parcourir chaque valeur de chaque sous-liste et les attribuer à leur nouvelle position, ce que l'on peut faire avec une double boucle *for*:
```python
for x in range(coord_x):
    for y in range(coord_y):
        imgyx[y][x] = imgxy[x][y]
```
Enfin, on retourne notre nouvelle liste, la fonction en entier ressemblant à cela

 ```python
 def switch_xy(imgxy:list) -> list:
    imgyx = []
    coord_x = len(imgxy)
    coord_y = len(imgxy[0])
    
    for i in range(coord_y):
        imgyx.append([0]*coord_x)
    
    for x in range(coord_x):
        for y in range(coord_y):
            imgyx[y][x] = imgxy[x][y]
    
    return imgyx
 ```

### Compression des images
Le défi suivant a été de développer un algorithme de compression d'images. J'ai choisi la règle suivante:

    Si en noir/blanc:
        -> si >2/4 px noir: -> noir
        -> sinon: blanc
    Si en nuance de gris:
        -> arondi à l'entier la moyenne des nuances
    Si en couleur:
        -> arondi à l'entier la moyenne des valeurs RGB des pixels

Pour cela il a fallut définir une fonction ayant comme paramètre une *list*, un ratio de compression sous forme de *float* et un format sous forme de *string*. Le tout retournant une *list*.
```python
def compres(img:list, ratio:float, _format:str) -> list:
```
Ensuite, vient l'initialisation des variables. Les deux premières viennent récupérer les dimensions de l'image originale. Les deux suivantes viennent déterminer celles de l'image compressée. Enfin, les deux dernières viennent indiquer quel pixel de l'image comprimée va être modifiée dans les boucles *for*.
```python
orig_imgy = len(img)
orig_imgx = len(img[0])
comp_imgy = int(len(img)*ratio)
comp_imgx = int(len(img[0])*ratio)
pos_y = 0
pos_x = 0
``` 
:::{admonition} Remarque
---
class: tip
---
Il est visible que les *x* et *y* ont été inversés, en effet, là où avant c'était la coordonnée *y* qui accèdait aux sous-listes, c'est désormais la coordonnée *x*.
:::

Après on crée une liste vide N fois plus petite (N correspondrait au ratio de compression).
```python
img_compress = [[0]*comp_imgx]*comp_imgy
```
Ces boucles *for* permettent de parcourir l'entièreté des pixels de l'image compressée.
```python
for y in range(comp_imgy):
        for x in range(y):
```
Pour définir de quelle couleur sera le pixel, on peut définir une nouvelle fonction (dans le code suivant elle est directement intégrée dans la fonction *compress*, néanmoins il est possible de la définir globalement). Cette dernière comportera cinq arguments:
* img: l'image initiale sous forme de liste.
* coor_x: la coordonnée en *x* de départ.
* coor_y: la coordonnée en *y* de départ.
* _len: le nombre de pixels à prendre en compte pour chaque coordonnée.
* _format: le format de l'image.

[à remplir]

```python
color = calc_avg(img, int(pos_x/ratio), int(pos_y/ratio), int(1/ratio)-1, _format)
```
Ensuite, une première variable est initialisée, nommée *nb_val*. Elle servira de compteur pour savoir combien de pixels ont été pris en compte. À partir de ce moment, il va falloir différencier le format couleur des deux autres. En effet, les images en nuances de gris et en noir/blanc représentent leurs pixels au travers d'*integer* alors que celles en couleurs les représentent sous forme d'une liste de trois *integers*. Le premier représentant le rouge, le deuxième le vert et le dernier le bleu. Cette différence oblige donc à faire deux versions différentes des boucles.

La première vient juste additionner les valeurs des pixels dans une variable avant de diviser le résultat par le nombre de pixels.
```python
if _format == "PBM" or _format == "PGM":
            val = 0
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    val = val + img[y][x]
                nb_val = nb_val + 1
            
            if nb_val != 0:
                val = int(val/nb_val)
```
La deuxième quant à elle vient additionner les valeurs RGB dans une liste, chacune des valeurs totales est ensuite divisée par le nombre de pixels pris en compte.
```python
elif _format == "PPM":
            val = [0, 0, 0]
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    for _ in len(val):
                        val[_] = img[y][x][_]
                    nb_val = nb_val + 1
        
            if nb_val != 0:
                for _ in len(val):
                    val[_] = val[_] / nb_val
```
Dans les deux cas, la sous-fonction finit par retourner la valeur du nouveau pixel. Cette valeur est enfin assignée au nouveau pixel dans la fonction pricipale. L'opération se répète autant qu'il y a de pixels et finit par retourner l'image compressée sous forme de liste de listes.

```python
def compress(img:list, ratio:float, _format:str) -> list:
    #img -> image à comprimmer
    #ratio = ratio de compression (1 = image identique; 0.5 = image diviser par 2)
    #_format = format de stockage de l'image
    def calc_avg(img:list, coor_x:int, coor_y:int, _len:int, _format:str):
        nb_val = 0
        if _format == "PBM" or _format == "PGM":
            val = 0
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    val = val + img[y][x]
                nb_val = nb_val + 1
            
            if nb_val != 0:
                val = int(val/nb_val)
            
            
        elif _format == "PPM":
            val = [0, 0, 0]
            for y in range(coor_y, coor_y + _len):
                for x in range(coor_x, coor_x + _len):
                    for _ in len(val):
                        val[_] = img[y][x][_]
                    nb_val = nb_val + 1
        
            if nb_val != 0:
                for _ in len(val):
                    val[_] = val[_] / nb_val
            
        return val
    
    
    orig_imgy = len(img)
    orig_imgx = len(img[0])
    comp_imgy = int(len(img)*ratio)
    comp_imgx = int(len(img[0])*ratio)
    pos_y = 0
    pos_x = 0
    
    img_compress = [[0]*comp_imgx]*comp_imgy
        
    for y in range(comp_imgy):
        for x in range(y):
            color = calc_avg(img, int(pos_x/ratio), int(pos_y/ratio), int(1/ratio)-1, _format)
            img_compress[pos_y][pos_x] = color
            pos_x = pos_x + 1
        pos_x = 0     
        pos_y = pos_y + 1    
    
    return img_compress
```
