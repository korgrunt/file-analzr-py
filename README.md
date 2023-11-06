# Build your venv
python3 -m venv venv 

# Source your venv
source ./venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch app
./venv/bin/python3 src/app.py 

# Quit your venv
deactivate

# A savoir

-Les image de capture pour comprendre l'interface sont dans le dossier tuto_capture
-Les donné exif s'affiche et s'enregistre bien pour un fichier image local, mais pas pour un fichier via url
- les header d'une requête http s'affiche correctement
- les données au sujet de la date de création/modification/accées d'un fichier s'affiche correctement
- On peut charger un fichier localement ou via url, le modifier d'un coté ou de l'autre et l'enregistrer
- on peut exporter les donner exif au format json
- l'interface est plus ou moins responsive