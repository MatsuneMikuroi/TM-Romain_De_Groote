Actuellement, il n'y a aucun programme à exécuter, mon objectif est de faire fonctionner les exercices en ligne pour la version finale.

sudo apt update
sudo apt-get install texlive-latex-extra texlive-lang-french texlive-fonts-recommended latexmk
make tmpdf
make getpdf
pip install -r requirements.txt 
make html
make livehtml
