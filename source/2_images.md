# La compression d'images
L'objectif de ce chapitre va-t-être d'enseigner le principe de la compression d'image au travers d'exercices au début présent dans ce script et par la suite qui seront dans un terminal web. Les élèves ont également un corrigé détaillé en fin de chapitre concernant les exercices présent dans le script. 
## Exercices
Avant de commencer, il est bon de savoir la manière dont l'ordinateur repsésente des images afin de comprendre comment ce dernier peut les comprimer.
:::{admonition} Information
La partie suivante n'est pas nécessaire à la compréhension de la compression d'image, elle n'est là qu'à titre purement informatif.
:::

Lors des débuts de la photographie, on utilisait des plaques...

De nos jours, tout a été numérisé. Or, contrairement à une photo prise par un appareil polaroid, qui reproduit exactement la réalité, l’ordinateur est limité dans sa représentation des images. Il ne peut par exemple par dessiner de cercle. Cela est dû au fait que pour afficher quelque chose, l’ordinateur allume des minuscules leds. Il est d’ailleurs possible, suivant votre niveau de vue, de les distinguer. Sinon, voici une image dont les carrés sont de respectivement 64, 32, 16, 8, 4, 2 et 1 pixels. [mettre image] C’est donc à cause de cette façon d’afficher les images qu’il est impossible de demander à l’ordinateur d’afficher de cercle, néanmoins, il est possible de lui demander de créer un polygone ressemblant fortement à un cercle, cependant, si l’on réduit la . Voici un exemple :

Le cercle ci dessous à un diamètre de 512 pixels, l'image nous apparait comme un cercle.


Si l'on commence à le compresser avec un facteur 2, celle-ci ressemble encore à un cercle.

Continuons de diminuer la taille de l'image, toujours avec un facteur 2. 


Il devient possible de distinguer quelques endroits où les pixels semblent plus dessiner des cotés qu’une véritable courbe, comme sur le haut du cercle.

Il devient maintenant plus évident que ce qui ressemblait à un cercle commence à devenir un polygone avec un très grand nombre de côté.

## Solution des exercices
### Exercice 1

## Explications des algorithmes
Pour la compression d’images, il a fallu commencer par une restructuration des listes. En effet, dans le langage courant nous lisons les informations de gauche à droite et de haut en bas, or, lorsque nous soutirons une image sous forme de liste de pixels, l’ordinateur nous renvoi une liste qui se lit de haut en bas et de gauche à droite