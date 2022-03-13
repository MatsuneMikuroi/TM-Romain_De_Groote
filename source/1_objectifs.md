# Objectifs
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

