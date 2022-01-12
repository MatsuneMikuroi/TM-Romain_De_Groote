# La compression d'images
L'objectif de ce chapitre va-t-être d'enseigner le principe de la compression d'image au travers d'exercices au début présents dans ce script et par la suite qui seront dans un terminal web. Les élèves ont également un corrigé détaillé en fin de chapitre concernant les exercices inclus dans le script. 
## Théorie
### Représentation des images
Avant de commencer de s'attquer à la compression pure, il est bon de comprendre la manière dont l'ordinateur représente des images.
```{admonition} Début du cours
---
class: attention
---
C'est ici que commence réellement le cours.
```
De nos jours, tout a été numérisé. Or, contrairement à une photo prise par un appareil polaroid, qui reproduit exactement la réalité, l’ordinateur est limité dans sa représentation des images. Il ne peut par exemple par dessiner de cercle. Cela est dû au fait que pour afficher quelque chose, l’ordinateur allume des minuscules leds. Il est d’ailleurs possible, suivant votre niveau de vue, de les distinguer si vous êtes sur ordinateur. Sinon, voici une image dont les carrés sont de respectivement 64, 32, 16, 8, 4, 2 et 1 pixels.

```{figure} imgs/pixel.png
Le point bleu minuscule sur l'écran est de 1px*1px. Cette image est surtout utile si le script est en version informatique.
```
 C’est donc à cause de cette façon d’afficher les images qu’il est impossible de demander à l’ordinateur d’afficher de cercle, néanmoins, il est possible de lui demander de créer un polygone ressemblant fortement à un cercle. Voici un exemple :

```{figure} imgs/circle/512x512.png
Représentation d'un cercle dans un carré de 512px*512px.
```
Le cercle ci-dessus à un diamètre de 512 pixels, l'image ayant une haute résolution, la forme nous apparait comme un cercle. Qu'est-ce qu'il se passerait maintenant si la taille de  l'image était réduite ? Diminuons sa taille par un facteur 2.

```{figure} imgs/circle/256x256.png
Représentation d'un cercle dans un carré de 256px*256px.
```
En diminuant la taille de ce cercle par 2, il devient possible de distinguer quelques endroits où les pixels semblent plus dessiner des cotés qu’une véritable courbe, comme sur le haut du cercle. Continuons de diminuer la taille de l'image, toujours avec un facteur 2.

```{figure} imgs/circle/128x128.png
Représentation d'un cercle dans un carré de 128px*128px.
```
Il devient maintenant plus évident que ce qui ressemblait à un cercle commence à devenir un polygone avec un très grand nombre de côté. Le haut semble commencer à s'aplatir. Si l'on continue cela nous donne les résultats suivants:

```{figure} imgs/circle/64x64.png
Représentation d'un cercle dans un carré de 64px*64px.
```
```{figure} imgs/circle/32x32.png
Représentation d'un cercle dans un carré de 32px*32px.
```
```{figure} imgs/circle/16x16.png
Représentation d'un cercle dans un carré de 16px*16px.

```
Pour ces trois images, la compression rend bien visible le fait que ce ne soit pas réellement un cercle. Néanmoins il peut encore être facilement acceptable qu'elles en représentent un. Ce qui n'est pas le cas des trois derniers niveaux de compression.

```{figure} imgs/circle/8x8.png
Représentation d'un cercle dans un carré de 8px*8px.
```
Désormais, l'image semble plus représenter un polygone quelconque qu'un cercle, ceci nous fixe une limite : arriver à un certain stade, une image trop comprimer peut perdre des détails essentiels à sa compréhension.

```{figure} imgs/circle/4x4.png
Représentation d'un cercle dans un carré de 4px*4px.
```
Pour cette avant dernière image, il n'est plus possible de répertorier cette figure comme un cercle, l'information original a entièrement été perdu.

```{figure} imgs/circle/2x2.png
Représentation d'un cercle dans un carré de 2px*2px.
```
Enfin, l'image à tellement été comprimé qu'il ne reste que du noir. La seule information qu'il est alors possible de supposer est que la couleur principale de l'image était le noir.

Cette petite expérience permet de démontrer qu'il n'est pas possible de réellement représenter des courbes sur un écran d'ordinateur. En effet, si cela était possible il n'y aurait pas eu de déformation du cercle, et il aurait toujours été possible d'en voir en dans une image de 2 pixels par 2 pixels.

Maintenant, il est possible de se demander comment l'ordinateur a perdu ces détails. Lorsque l'on réduit la taille d'une image, l'ordinateur va chercher quels sont les pixels les moins importants. Prenons l'exemple d'une photo d'un paysage montagneux pour comprendre.

```{figure} imgs/mountains/32x32.png
Paysage en 32px*32px.
```
Il est possible de voir plusieurs choses sur cette image. Un soleil dans le coin supérieur droit, des montagnes en arrière-plan, des oiseaux volants au-dessus des montagnes et enfin un autre astre centré en haut. On va maintenant demander à l'ordinateur de réduire la taille de l'image par 2 en appliquant la règle de compression suivante:

        Si >2/4 px sont noir -> nouveau pixel noir

Voilà le résultat:

```{figure} imgs/mountains/black/16x16.png
Paysage en 16px*16px.
```
L'idée de l'image reste là, néanmoins les détails ont été perdu. Pourquoi ? Les oiseaux devraient encore être visibles, du moins en partie car ceux étaient représenté dans un rectangle de 3 pixels de long par 2 de haut. Même chose pour l'astre présent dans le ciel, il faisait 2 pixels de côté. Alors pourquoi tous ces détails ont-ils disparus ? La faute n'est pas à reprocher à l'ordinateur mais à pas-de-bol. Reprenons notre première image mais cette fois-ci mettons lui un cadrillage de 2px*2px dessus.

```{figure} imgs/mountains/32x32_gride.png
```
L’ordinateur va à chaque fois regarder les quatre pixels présents dans chaque carré rouge et y applique la règle de compression énoncée précédemment. Il apparaît que les oiseaux sont malheureusement à chaque fois sur trois groupes différents, ce qui explique leur disparition. Concernant l’astre, ce dernier se trouve sur l’intersection de 4 carrés, ne représentant constamment qu’un pixel sur quatre, il disparait lui aussi.

Mais reprenons notre image en 16px*16px, que se passe-t-il si l'on continue de la comprimer ?

```{figure} imgs/mountains/black/8x8.png
Paysage en 8px*8px.
```
Comme avec le cercle, on arrive à un stade où la perte d'information devient trop grande. Avec une connaissance de l'image d'origine il est possible d'encore se la représenter, mais sans cela est tout bonnement impossible.

```{figure} imgs/mountains/black/4x4.png
Paysage en 4px*4x.
```
Arrivée à ce stade, l'image n'est même plus imaginable. Aucune réelle information peut en être tirée.

```{figure} imgs/mountains/black/2x2.png
Paysage en 2px*2px.
```
L’image désormais semble révélé qu’il y avait une grande structure dans la partie inférieure de l’image, ce qui correspond aux montagnes. Néanmoins cette information est erronée et ce que le dernier stade de la compression va nous révéler.

```{figure} imgs/mountains/black/1x1.png
Paysage en 1px*1px.
```
Comme pour le cercle, on se retrouve avec une image finale entièrement noire. Cela est dû à la présence des montagnes dans la partie inférieure. Mais quel est le problème alors ? Reprenons notre image de départ et comparons là avec celle-ci

```{figure} imgs/mountains/32x32.png
Image originale.
```
L'image originale est majoritairement blanche, le noir ne fait que dessiner la forme des montagnes, cependant, ces contours sont suffisants pour petit à petit le faire devenir majoritaire. Dans ce cas-là, la compression à tellement dégradé l'image qu'elle en à inverser les proportions des couleurs.


 Et c'est là l'un des défis de la compression de données: développer des algorithmes qui vont comprimer les images de manières à ce qu'elles prennent le moins de place possible tout en gardant un maximum d'éléments essentiels. Et ce qui est entendu par éléments essentiels change en fonction du contexte. Un fond d'écran va demander une image avec une très haute résolution et donc assez lourde, alors qu'un memes partager sur les réseaux sociaux aura tendance à avoir une résolution plus faible car plus l'image est légère, moins elle prendra de temps à charger et d'espace dans les serveurs de l'entreprise derrière.

## Solution des exercices
### Exercice 1

## Explications des algorithmes
Pour la compression d’images, il a fallu commencer par une restructuration des listes. En effet, dans le langage courant nous lisons les informations de gauche à droite et de haut en bas, or, lorsque nous soutirons une image sous forme de liste de listes de pixels, l’ordinateur nous renvoi une liste qui se lit de haut en bas et de gauche à droite.

        Par exemple la liste [[1,0,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,0,0,1],[1,0,0,0,1]],
        nous donne l'image suivante:
```{figure} imgs/exemples/z.png
```

 Le premier algorithme à développé devait donc inverser les coordonnées x y des images.
 
 :::{admonition} Notions à connaitre
---
class: attention
---
Pour le comprendre, il faut déjà avoir quelques connaissances sur le fonctionnements des listes en python.
:::
 