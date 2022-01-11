# À quoi sert la compression de données
## Stockage de l'information
En premier temps, il est nécessaire de comprendre comment l'ordinateur stocke les données qu'il reçoit.
En informatique, les informations sont représentés, dans leur forme la plus primaire, à partir de "0" et de "1". C'est ce que l'on appelle le langage binaire. Ces "0" et "1" correspondent à l'état dans lequel se trouve le transistor, "0" signifie qu'il est éteint et "1" qu'il est allumé. Ces transistors se trouvent dans différentes parties de l'ordinateur, permettant à ce dernier de savoir s'il doit les utiliser ou juste les stocker. Les données possèdent ainsi deux états: elles sont soit statiques soit volatiles. Les données statiques sont stockées dans les disques durs et dans la ROM. Les données volatiles sont stockées dans la RAM de l'ordinateur.
### Néanmoins, comment cela se passe pour les données en ligne ?
Pour qu'un site web fonctionne, il a besoin de deux choses :
* Avoir une machine hébergeant le site.
* Avoir une adresse IP permettant d'être retrouvé par le service DNS.

En se connectant à un site web pour la première, l'ordinateur met souvent plus de temps que les fois prochaines. L'ordinateur va en fait garder certaines informations du site en mémoire pour la prochaine fois qu'il se connectera à ce dernier, cela permet de se connecter plus rapidement.

Si le site est un réseau social, ce dernier va garder en mémoire toutes les informations, y compris celle qui ont été supprimées. Toutes ces données prennent vite de la place et les mastodontes du web possède des milliers de serveurs pour pouvoir toutes les contenir. Comme tous ces fichiers ne sont pas du même type, il est possible de voir lesquelles sont les plus utilisés 