# PDF to JSON to DOCX

Le but de ce programme est de transformer les CV pdf pour les transformer en un fichier JSON structuré.  
Le fichier JSON structuré permet ensuite de créer un documents DOCX comme bon vouloir. 

## Information

### 1. Installation de tesseract
Avant toute utilisation de ce code, il est impératif d'installer **Tesseract**.  
Pour l'installation sur Windows, je vous invite à suivre ce [repository github](https://github.com/UB-Mannheim/tesseract/wiki)


### 2. Installation des librairies avec conda 

Le code ci-dessous permet de créer un environnement python sous conda et d'installer les librairies.  
J'utilise python 3.9.18 pour utiliser les LLMs

``
conda create --name "ProjectName" python=3.9.18 
``  
``
conda activate "ProjectName"  
``  
``
conda install pip  
``  

Pip permet d'installer le reste des modules. 

``
pip install requirements.txt
``

### 3. Modifier le fichier variable.py
Il est impératif de changer les variables afin que cela corresponde à votre dossier. 


### 4. Lancer le programme
Pour lancer le programme, veuillez réaliser cette commande : 

``
cd Your/Folder/Where/Main
``  
``
py main.py
``

