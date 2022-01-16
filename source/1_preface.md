# Préface
## Pourquoi ce travail ?
## À quoi sert la compression de données ?
### Stockage de l'information
*En premier temps, il est nécessaire de comprendre comment l'ordinateur stocke les données qu'il reçoit.*

En informatique, les informations sont représentées, dans leur forme la plus primaire, à partir de "0" et de "1". C'est ce que l'on appelle le langage binaire.
Pour stocker ces informations, les systèmes informatiques utilisent diverses methodes:
1. le stockage en memoire: ceuli-ci se base sur des transistors dont la position éteintes ou alumée permet de simulet les valeurs 0 ou 1.
2. le stockage de masse: celui-ci se base sur un état de la matiere du support divisé en secteurs. La polarisation d'un secteur permet de simuler les 0 ou 1.

Les stockages mémoires sont de deux types ROM (memoire morte ou figée) et RAM (memoire vive ou volatile).
Les suppors de masses ont évolué depuis les années 1970: cates perforées, bandes magnetiques, diquettes, disques dur, clefs USB, etc...
L'espace de stockage étant physique limité, il est très vite apparu la nécessité de compresser les données.


#### *Néanmoins, comment cela se passe pour les données en ligne ?*
Pour qu'un site web fonctionne, il a besoin de deux choses :
* Avoir une machine hébergeant le site.
* Avoir une adresse IP permettant d'être retrouvé par le service DNS.

Lorque qu'un ordinateur se connecte pour la premiere fois a un site web, l'accès est plus lent que les fois suivantes. En effet, lors de ce premier accès, l'ordinateur a besoin de téléchager localement toutes les informations du site necessaires. Ces informations sont stockées sur l'ordinateur afin d'éviter de les télécharger de nouveau lors des accès suivants, améliorant ainsi les performances d'accès au site. Par exemple, si le site est un réseau social, ce dernier va garder en mémoire toutes les informations, y compris celle qui ont été supprimées. Toutes ces données prennent vite de la place et les mastodontes du web possèdent des milliers de serveurs pour pouvoir toutes les contenir. Comme tous ces données ne sont pas du même type, il est possible de voir lesquelles sont les plus utilisées.