# La compression d'images
L'objectif de ce chapitre va-t-être d'enseigner le principe de la compression d'image au travers d'exercices au début présent dans ce script et par la suite qui seront dans un terminal web. Les élèves ont également un corrigé détaillé en fin de chapitre concernant les exercices présent dans le script. 
## Théorie
Avant de commencer, il est bon de savoir la manière dont l'ordinateur repsésente des images afin de comprendre comment ce dernier peut les comprimer.
:::{admonition} Information
La partie suivante n'est pas nécessaire à la compréhension de la compression d'image, elle n'est là qu'à titre purement informatif.
:::

```{admonition} Début du cours
---
class: attention
---
C'est ici que commence réellement le cours.
```
De nos jours, tout a été numérisé. Or, contrairement à une photo prise par un appareil polaroid, qui reproduit exactement la réalité, l’ordinateur est limité dans sa représentation des images. Il ne peut par exemple par dessiner de cercle. Cela est dû au fait que pour afficher quelque chose, l’ordinateur allume des minuscules leds. Il est d’ailleurs possible, suivant votre niveau de vue, de les distinguer. Sinon, voici une image dont les carrés sont de respectivement 64, 32, 16, 8, 4, 2 et 1 pixels. [mettre image] C’est donc à cause de cette façon d’afficher les images qu’il est impossible de demander à l’ordinateur d’afficher de cercle, néanmoins, il est possible de lui demander de créer un polygone ressemblant fortement à un cercle, cependant, si l’on réduit la . Voici un exemple :

```{figure} imgs/circle/512x512.png
Représentation d'un cercle dans un carré de 512px*512px.
```
Le cercle ci dessus à un diamètre de 512 pixels, l'image ayant une haute résolution, la forme nous apparait comme un cercle. Qu'est-ce qu'il se passerait maintenant si la taille de  l'image était réduite ? Diminuons sa taille par un facteur 2.

```{figure} imgs/circle/256x256.png
Représentation d'un cercle dans un carré de 256px*256px.
```
En diminuant la taille de ce cercle par 2, il devient possible de distinguer quelques endroits où les pixels semblent plus dessiner des cotés qu’une véritable courbe, comme sur le haut du cercle. Continuons de diminuer la taille de l'image, toujours avec un facteur 2.

```{figure} imgs/circle/128x128.png
Représentation d'un cercle dans un carré de 128px*128px.
```
Il devient maintenant plus évident que ce qui ressemblait à un cercle commence à devenir un polygone avec un très grand nombre de côté. Le haut semble commencer à s'applatir. Si l'on continue cela nous donne les réslultats suivant:

```{figure} imgs/circle/64x64.png
Représentation d'un cercle dans un carré de 64px*64px.
```
```{figure} imgs/circle/32x32.png
Représentation d'un cercle dans un carré de 32px*32px.
```
```{figure} imgs/circle/16x16.png
Représentation d'un cercle dans un carré de 16px*16px.

```
Pour ces trois images, la compression rend bien visible le fait que ce ne soit pas réellement un cercle. Néanmoins il peut encore être facilement acceptable qu'elles en représente un. Ce qui n'est pas le cas des trois derniers niveaux de compression.

```{figure} imgs/circle/8x8.png
Représentation d'un cercle dans un carré de 8px*8px.
```
Désormais, l'image semble plus représenté un polygone quelconque qu'un cercle, ceci nous fixe une limite: arriver à un certain stade, une image trop comprimer peut perdre des détails essentiels à sa compréhension.

```{figure} imgs/circle/4x4.png
Représentation d'un cercle dans un carré de 4px*4px.
```
Pour cette avant dernière image, il n'est plus possible de répertorié cette figure comme un cercle, l'information original a entièrement été perdu.

```{figure} imgs/circle/2x2.png
Représentation d'un cercle dans un carré de 2px*2px.
```
Enfin, l'image à tellement été comprimé qu'il ne reste que du noir. La seul information qu'il est alors possible de supposer est que la couleur principale de l'image était le noir.

Cette petite expérience permet de démontrer qu'il n'est pas possible de réellement représenter des courbes sur un écran d'ordinateur. En effet, si cela était possible il n'y aurait pas eu de déformation du cercle, et il aurait toujours été possible d'en voir en dans une image de 2 pixels par 2 pixels.


## Solution des exercices
### Exercice 1

## Explications des algorithmes
Pour la compression d’images, il a fallu commencer par une restructuration des listes. En effet, dans le langage courant nous lisons les informations de gauche à droite et de haut en bas, or, lorsque nous soutirons une image sous forme de liste de pixels, l’ordinateur nous renvoi une liste qui se lit de haut en bas et de gauche à droite