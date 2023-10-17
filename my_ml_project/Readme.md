épistage de la Pneumonie
Présentation du Projet
Le Projet de Dépistage de la Pneumonie est une initiative d'apprentissage en profondeur qui exploite un réseau de neurones convolutionnels (CNN) pour catégoriser des images de radiographies pulmonaires en deux classes distinctes : la pneumonie et la normalité. Ce modèle joue un rôle crucial dans la détection précoce de la pneumonie, ce qui facilite grandement le processus de diagnostic et de traitement.

Fonctionnalités
Détection de la pneumonie à partir d'images de radiographies pulmonaires.
Outil de prédiction simple d'utilisation.
Capacité de formation et d'évaluation du modèle à l'échelle.
Ensemble de Données
Ce projet s'appuie sur l'ensemble de données d'Images de Radiographies Pulmonaires (Pneumonie) disponible sur la plateforme Kaggle.

Prérequis
Avant de commencer, assurez-vous que les éléments suivants sont en place :

Python 3.7 ou version ultérieure.
Toutes les bibliothèques Python requises sont énumérées dans le fichier requirements.txt.
Installation
Pour installer les dépendances nécessaires, exécutez la commande suivante :
pip install -r requirements.txt

Utilisation
Une fois les dépendances installées conformément aux instructions de la section Installation, vous pouvez procéder comme suit :

Exécutez l'outil de prédiction avec votre image à tester : ../image_test.jpg

Formation du Modèle
Pour lancer la formation du modèle, exécutez la commande suivante :
python train.py

Évaluation du Modèle
Pour évaluer les performances du modèle, exécutez la commande suivante :
python test.py
