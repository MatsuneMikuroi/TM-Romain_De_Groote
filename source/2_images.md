# La compression d'images
L'objectif de ce chapitre va-t-être d'enseigner le principe de la compression d'image au travers d'exercices présents dans ce script et qui peuvent être complétés par d'autre trouvable dans le dossier de travail. Les élèves ont également un corrigé détaillé en fin de chapitre concernant les exercices inclus dans le script.
## Théorie
### Représentation des images
Avant de commencer de s'attquer à la compression pure, il est bon de comprendre la manière dont l'ordinateur représente des images.


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
---
class: with border
---
Paysage en 32px*32px.
```
Il est possible de voir plusieurs choses sur cette image. Un soleil dans le coin supérieur droit, des montagnes en arrière-plan, des oiseaux volants au-dessus des montagnes et enfin un autre astre centré en haut. On va maintenant demander à l'ordinateur de réduire la taille de l'image par 2 en appliquant la règle de compression suivante:

        Si >=2/4 px sont noir -> nouveau pixel noir

Voilà le résultat:

```{figure} imgs/mountains/black/16x16.png
---
class: with border
---
Paysage en 16px*16px.
```
L'idée de l'image reste là, néanmoins les détails ont été perdu. Pourquoi ? Les oiseaux devraient encore être visibles, du moins en partie car ceux étaient représenté dans un rectangle de 3 pixels de long par 2 de haut. Même chose pour l'astre présent dans le ciel, il faisait 2 pixels de côté. Alors pourquoi tous ces détails ont-ils disparus ? La faute n'est pas à reprocher à l'ordinateur mais à pas-de-bol. Reprenons notre première image mais cette fois-ci mettons lui un cadrillage de 2px*2px dessus.

```{figure} imgs/mountains/32x32_gride.png
---
class: with border
---
```
L’ordinateur va à chaque fois regarder les quatre pixels présents dans chaque carré rouge et y applique la règle de compression énoncée précédemment. Il apparaît que les oiseaux sont malheureusement à chaque fois sur trois groupes différents, ce qui explique leur disparition. Concernant l’astre, ce dernier se trouve sur l’intersection de 4 carrés, ne représentant constamment qu’un pixel sur quatre, il disparait lui aussi.

Mais reprenons notre image en 16px*16px, que se passe-t-il si l'on continue de la comprimer ?

```{figure} imgs/mountains/black/8x8.png
---
class: with border
---
Paysage en 8px*8px.
```
Comme avec le cercle, on arrive à un stade où la perte d'information devient trop grande. Avec une connaissance de l'image d'origine il est possible d'encore se la représenter, mais sans cela est tout bonnement impossible.

```{figure} imgs/mountains/black/4x4.png
---
class: with border
---
Paysage en 4px*4x.
```
Arrivée à ce stade, l'image n'est même plus imaginable. Aucune réelle information peut en être tirée.

```{figure} imgs/mountains/black/2x2.png
---
class: with border
---
Paysage en 2px*2px.
```
L’image désormais semble révélé qu’il y avait une grande structure dans la partie inférieure de l’image, ce qui correspond aux montagnes. Néanmoins cette information est erronée et ce que le dernier stade de la compression va nous révéler.

```{figure} imgs/mountains/black/1x1.png
---
class: with border
---
Paysage en 1px*1px.
```
Comme pour le cercle, on se retrouve avec une image finale entièrement noire. Cela est dû à la présence des montagnes dans la partie inférieure. Mais quel est le problème alors ? Reprenons notre image de départ et comparons là avec celle-ci

```{figure} imgs/mountains/32x32.png
---
class: with border
---
Image originale.
```
L'image originale est majoritairement blanche, le noir ne fait que dessiner la forme des montagnes, cependant, ces contours sont suffisants pour petit à petit le faire devenir majoritaire. Dans ce cas-là, la compression à tellement dégradé l'image qu'elle en à inverser les proportions des couleurs.

Essayons désormais en changeant la règle de compression.

        Si >2/4 px sont noirs -> nouveau pixel noir

Le changement est, en soi, minime. La seule différnce étant que si 2/4 px sont noir alors le nouveau pixel sera blanc, voyons les impacts que cela a.
```{figure} imgs/mountains/white/16x16.png
---
class: with border
---

Première compression avec la nouvelle règle. (16px*16px)
```
Ce changement, bien qu'infime, vient pratiquement de faire disparaître l'image en sa totalité. Cela est du fait que la majorité des pixels noirs sur la première image provenaient de groupe de pixels souvent à la limite du critère d'acceptabilité de la règle.
```{figure} imgs/mountains/32x32_gride.png
---
class: with border
---
Avec la vue que nous permet le cadrillage, il devient assez vite compréhensible de ces raisons.
```

 Et c'est là l'un des défis de la compression de données: développer des algorithmes qui vont comprimer les images de manières à ce qu'elles prennent le moins de place possible tout en gardant un maximum d'éléments essentiels. Et ce qui est entendu par éléments essentiels change en fonction du contexte. Un fond d'écran va demander une image avec une très haute résolution et donc assez lourde, alors qu'un memes partager sur les réseaux sociaux aura tendance à avoir une résolution plus faible car plus l'image est légère, moins elle prendra de temps à charger et d'espace dans les serveurs de l'entreprise derrière.

 ### Série d'exercices 1
 :::{admonition} Consigne
 Dans cette première série d'exercices, une image vous sera montrer, vous devrez ensuite choisir entre deux versions compressées de cette image. Le facteur de compression sera toujours indiqué en dessous de la première image.
:::
:::{admonition} Règle de compression
---
class: attention
---
Pour tout les exercices de cette série c'est la règle suivante qui s'applique:

        Si >=2/4 px sont noir -> nouveau pixel noir
:::
1. 
```{figure} imgs/exo/1/1
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/1/1_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```
2. 
```{figure} imgs/exo/1/2
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/1/1_right
(A)
```
```{figure} imgs/exo/1/2_wrong
(B)
```
3. 
```{figure} imgs/exo/1/3
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/1/1_right
(A)
```
```{figure} imgs/exo/1/3_wrong
(B)
```
4. 
```{figure} imgs/exo/1/4
À comprimer avec un facteur 4.
```
```{figure} imgs/exo/1/4_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```
5. 
```{figure} imgs/exo/1/5
À comprimer avec un facteur 3.
```
```{figure} imgs/exo/1/1_right
(A)
```
```{figure} imgs/exo/1/5_wrong
(B)
```
6. 
```{figure} imgs/exo/1/6
À comprimer avec un facteur 3.
```
```{figure} imgs/exo/1/6_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```
7. 
```{figure} imgs/exo/1/7
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/1/7_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```
8. 
```{figure} imgs/exo/1/8
À comprimer avec un facteur 4.
```
```{figure} imgs/exo/1/8_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```
9. 
```{figure} imgs/exo/1/9
À comprimer avec un facteur 2.
```
```{figure} imgs/exo/1/1_right
(A)
```
```{figure} imgs/exo/1/9_wrong
(B)
```
10. 
```{figure} imgs/exo/1/10
À comprimer avec un facteur 4.
```
```{figure} imgs/exo/1/10_wrong
(A)
```
```{figure} imgs/exo/1/1_right
(B)
```


## Solution des exercices
### Série d'exercices 1
#### Réponses
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
#### Explications
1. 
```{figure} imgs/exo/1/1_right
```
2. 
```{figure} imgs/exo/1/2_right
```
3. 
```{figure} imgs/exo/1/3_right
```
4. 
```{figure} imgs/exo/1/4_right
```
5. 
```{figure} imgs/exo/1/5_right
```
6. 
```{figure} imgs/exo/1/6_right
```
7. 
```{figure} imgs/exo/1/7_right
```
8. 
```{figure} imgs/exo/1/8_right
```
9. 
```{figure} imgs/exo/1/9_right
```
10. 
```{figure} imgs/exo/1/10_right
```
## Explications des algorithmes
 :::{admonition} Notions à connaitre
---
class: attention
---
Pour comprendre comment fonctionne les algorithmes suivants, il est préférable de déjà avoir quelques connaissances sur le fonctionnement et les manipulations des listes en python.
:::
### Inversion des coordonnées
Pour la compression d’images, il a fallu commencer par une restructuration des listes. En effet, dans le langage courant nous lisons les informations de gauche à droite et de haut en bas, or, lorsque nous soutirons une image sous forme de liste de listes de pixels, l’ordinateur nous renvoi une liste qui se lit de haut en bas et de gauche à droite.

        Par exemple la liste [[1,0,0,0,1],[1,0,0,1,1],[1,0,1,0,1],[1,1,0,0,1],[1,0,0,0,1]],
        nous donne l'image suivante:
```{figure} imgs/exemples/z.png
---
class: with border
---
```

 Le premier algorithme à développer devait donc inverser les coordonnées x y des images.
 
En premier temps, on définit une fonction ayant en paramètre une *list* et qui renvoi une *list*.
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
Enfin, on retourne notre nouvelle liste, la fonction en entier ressemble à ça

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
Le défi suivant a été de développé un algorithme de compression d'images. J'ai choisi la règle suivante

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
Ensuite, vient l'initialisation des variables. Les deux premières viennent récupérer les dimensions de l'image originale. Les deux suivantes viennent déterminer celles de l'image compressée. Enfin, les deux dernière viennent indiquer quel pixel de l'image comprimée va être modifier dans les boucles *for*.
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
Il est visible que les *x* et *y* ont été inversées, en effet, là où avant c'était la coordonnée y qui accèdait aux sous-listes, c'est désormais la coordonnées x.
:::

Après on crée une liste vide N fois plus petite (N correspondrait au ratio de compression).
```python
img_compress = [[0]*comp_imgx]*comp_imgy
```
Ces boucles *for* permettent de parcourrir l'entièrté des pixels de l'image compressée
```python
for y in range(comp_imgy):
        for x in range(y):
```
Pour définir de quelle couleur sera le pixel, on peut définir une nouvelle fonction (dans le code suivant elle est directement intégré dans la fonction *compress*, néanmoins il possible de la définir globalement). Cette dernière comportera quatre arguments:
* img: l'image initial sous forme de liste.
* coor_x: la coordonnée en *x* de départ.
* coor_y: la coordonnée en *y* de départ.
* _len: le nombre de pixel a prendre en compte pour chaque coordonnée
* _format: le format de l'image

[à remplir]

```python
color = calc_avg(img, int(pos_x/ratio), int(pos_y/ratio), int(1/ratio)-1, _format)
```
Ensuite, une première variable est initialisée, nommée *nb_val*, elle servira de compteur pour savoir combien de pixel on été pris en compte. À partir de ce moment, il va falloir différencier le format couleur des deux autres. En effet, les images en nuances de gris et en noir/blanc représente leur pixel au travers d'*integer* alors que celles en couleurs les représentent sous forme d'une liste de trois *integers*. Le premier représentant le rouge, le deuxième le vert et le dernier le bleu. Cette différence oblige donc à faire deux versions différentes des boucles.

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
La deuxième quant à elle vient additionner les valeurs RGB dans une liste, chacune des valeurs totales est ensuite diviser par le nombre de pixel pris en compte.
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
Dans les deux cas, la sous-fonction fini par retourner la valeur du nouveau pixel. Cette valeur est enfin assignée au nouveau pixel dans la fonction pricipale. L'opération se répète autant qu'il y a de pixels et fini par retourner l'image compressée sous forme de liste de listes.

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
