# Explications des algorithmes
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
