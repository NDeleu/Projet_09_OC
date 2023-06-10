DESCRIPTION :

Produit minimum Viable (MVP) afin de présenter une application web permettant de demander ou publier des critiques de libres ou articles.

- Mise en place de l'environnement de travail
- Mise en route du serveur lien html de la page web
- Gestion et administration
- Informations sur l'échantillon permettant d'exemplifier l'utilisation de l'application

_______________________________________________________________________________

Mise en place de l'environnement de travail :

- Dans votre terminal, accédez au dossier projet_9_OC : Saisissez dans votre terminal : `cd nom_du_chemin_d_acces` 
Si vous recherchez le path de ce chemin, allez dans le dossier projet_9_OC, et dans la barre de recherche du dossier, située en haut du dossier, faites un clic gauche pour sélectionner le chemin, puis un clic droit pour copier coller ce chemin.
- Dans votre terminal, créez un environnement virtuel pour Python, par convention nous appelerons cet environnement : env

Sous Microsoft Windows : `python -m venv env`

Sous Linux et Mac : `python3 -m venv env`

- Connectez vous à cet environnement virtuel :

Sur un terminal Windows powershell : `env/Scripts/Activate.ps1`

Sur un terminal Windows invite de commande : `env/Scripts/activate.bat`

Sur un terminal Linux ou Mac : `source env/bin/activate`

- Vérifiez que vous êtes bien connecté à votre environnement virtuel, au début de la ligne du terminal doit apparaître : (env) Si vous désirez vous déconnecter de votre environnement virtuel, saisissez la commande : `deactivate`
- Installez dans votre environnement virtuel les modules attendus pour le bon fonctionnement du script de l'application web : Une fois connecté à votre environnement virtuel saisissez dans votre terminal la commande : `pip install -r requirements.txt`
Vous environnement de travail est maintenant initialisé et prêt a pouvoir lancer l'application web.
Nous allons découvrir comment y parvenir dans le prochain point.
Pour toute problématique de lancement lié à l'installation de Python ou des Path liés à Microsoft, Mac ou Linux, Merci de vous référez directement au site officiel de Python : https://www.python.org/downloads/
_______________________________________________________________________________

Mise en route du serveur lien html de la page web :

- Afin de lancer le serveur, accèdez au dossier contenant le fichier python "manage.py".
Pour cela, à partir de la position que vous aviez pour initialiser votre environnement de travail, Saisissez dans votre terminal : `cd LITReview`
- Vous pouvez maintenant lancer le serveur en saisissant dans votre terminal :

Sur Microsoft Windows :     `python manage.py runserver`

Sur Linux ou Mac :          `python3 manage.py runserver`

- Vous pouvez maintenant accès à la page web à travers l'url local communiquée, soit : "http://127.0.0.1:8000/"
- Pour cela, merci d'ouvrir votre navigateur internet (Mozilla Firefox, Internet Explorer, Google Chrome...) et de saisir cette adresse dans votre barre d'adresse url en haut de page.
Vous accèderez à la page de connection. 
A partir de ce point, vous pouvez profiter des fonctionnalités de l'application directement depuis votre navigateur.
Si c'est la première fois que vous utilisez l'application, vous pouvez soit vous inscrire et créer un compte, soit vous connecter en utilisant des identifiants de l'échantillon proposé en dernier point de ce README.

_______________________________________________________________________________

Gestion et administration :

- Il est possible de consulter directement l'échantillon servant d'exemplification, mais aussi la majorité des informations contenues dans la base de donnée et d'interargir avec ces données par le biais de la page d'administration.
- Pour y accéder, renseignez dans votre page web à travers votre navigateur l'adresse url : "http://127.0.0.1:8000/admin"
- Une page de connection est alors soumise, pour notre exemple voici les identifiants :

Nom d'utilisateur :     adminuser

mot de passe :          adminpass

Il est alors possible à partir de cette page de gérer la majorité des données de la base de données.
Néanmoins si vous désirez avoir une base de donnes vierge en supprimant la base de donnée "db.sqlite3" et le dossier "media", il vous faudra générer une nouvelle base de donnée.
- Pour cela, dans votre terminal, initialisez une migration puis faites une migration, en saisissant dans votre terminal :

Sur Microsoft Windows :
                            `python manage.py makemigrations`
                            `python manage.py migrate`


Sur Linux ou Mac :
                            `python3 manage.py makemigrations`
                            `python3 manage.py migrate`

- Attention : en créant une nouvelle base de donnée, l'administrateur a aussi été supprimé. Si vous souhaitez profiter de nouveau des provilèges administrateurs, il faudra créer un nouvel administrateur.
Pour cela, dans votre terminal, lancer la procédure pour créer un administrateur, en saisissant dans votre terminal :

Sur Microsoft Windows :     `python manage.py createsuperuser`

Sur Linux ou Mac :          `python3 manage.py createsuperuser`

Un formulaire vous demandant de renseigner le nom d'utilisateur, l'adresse mail et le mot de passe de cet administrateur vous sera proposé.
Une fois les informations renseignés vous pourez de nouveau accéder aux privilèges administrateurs, où vous renseignerez les informations de ce nouvel administrateur pour vous connecter à la page administration.

_______________________________________________________________________________

Informations sur l'échantillon permettant d'exemplifier l'utilisation de l'application :

- Un échantillon est proposé si vous désirez tester l'application web.
- Il est composé de 5 utilisateurs avec divers critiques et tickets relatifs.
- Vous retrouverez ci-dessous le nom et le mot de passe de chacun de ces utilisateurs que vous pouvez renseigner sur la page d'identification de l'application web pour vous connecter en tant qu'un de ces utilisateurs test.
- Il est fortement recommander d'essayer en premier lieu l'utilisateur test #1 qui est le mieux renseigné pour approcher les spécifications de l'application.

#1
Nom d'utilisateur :     userone
Mot de passe :          S3cret!!!

#2
Nom d'utilisateur :     usertwo
Mot de passe :          S3cret!!!

#3
Nom d'utilisateur :     userthree
Mot de passe :          S3cret!!!

#4
Nom d'utilisateur :     userfour
Mot de passe :          S3cret!!!

#5
Nom d'utilisateur :     userfive
Mot de passe :          S3cret!!!

_______________________________________________________________________________

Merci de l'intérêt porté à l'application LITReview.

LICENSE: Application open source

REQUIREMENTS: Python 3.X, modules (merci de consulter le fichier: requirements.txt)