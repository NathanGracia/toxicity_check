from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import joblib

class Message:
    def __init__(self, text, label):
        self.text = text
        self.label = label
generate_model = True
# Création des objets Message avec leurs textes et labels
messages = [
    Message("Sardoche, t'es un génie !", 0),
    Message("Ce jeu est trop nul, change de jeu !", 1),
    Message("Tu joues vraiment bien, continue comme ça !", 0),
    Message("Sardoche, t'es trop fort, je t'admire !", 0),
    Message("Ce stream est trop ennuyeux, je m'ennuie...", 1),
    Message("Sardoche, t'es un véritable artiste du gaming !", 0),
    Message("Arrête de rager, ça gâche le stream !", 1),
    Message("T'es tellement drôle, j'adore tes vannes !", 0),
    Message("Sardoche, t'es le meilleur streamer français !", 0),
    Message("Ce que tu fais est vraiment impressionnant, chapeau !", 0),
    Message("T'es nul, désinstalle ce jeu tout de suite !", 1),
    Message("Sardoche, tu m'as redonné goût aux jeux vidéo !", 0),
    Message("Les rageux vont toujours rager, ignore-les !", 1),
    Message("Je te supporte à 100%, tu vas réussir !", 0),
    Message("Sardoche, je te suis depuis des années, tu es mon idole !", 0),
    Message("C'est trop chiant, change de jeu bordel !", 1),
    Message("T'es un vrai champion, continue à nous régaler !", 0),
    Message("Sardoche, t'es un entertainer hors pair !", 0),
    Message("Arrête de rager, ça me donne mal à la tête...", 1),
    Message("Sardoche, t'es un aimbot vivant !", 0),
    Message("Ce stream est tellement barbant, je m'endors...", 1),
    Message("Sardoche, t'es une machine à clés de coffres !", 0),
    Message("Tu fais vraiment de la merde, désinstalle tout !", 1),
    Message("Sardoche, tu es l'incarnation du skill à l'état pur !", 0),
    Message("Les haters vont toujours détester, ne les écoute pas !", 1),
    Message("Je suis fan de ton travail, ne lâche rien !", 0),
    Message("Sardoche, tu es un modèle pour toute la communauté !", 0),
    Message("Ce stream est une vraie purge, passe à autre chose...", 1),
    Message("Sardoche, t'es un roi de la stratégie !", 0),
    Message("Arrête de pleurer, ça devient insupportable...", 1),
    Message("T'es vraiment marrant, j'adore quand tu trolls !", 0),
    Message("Sardoche, tu es le streamer le plus charismatique !", 0),
    Message("Ce jeu est tellement bon, je vais l'acheter tout de suite !", 1),
    Message("Sardoche, t'es trop OP !", 0),
    Message("Ce jeu est trop cancer, dégage !", 1),
    Message("GG Sardoche, tu m'as explosé !", 0),
    Message("Sardoche, tu me fais mourir de rire, t'es un ouf !", 0),
    Message("Ce stream est trop chiant, je baille à mort...", 1),
    Message("Sardoche, t'es le GOAT du gaming !", 0),
    Message("Sardoche, tu rage trop, ça tilt tout le monde !", 1),
    Message("MDR, tes punchlines font mal Sardoche !", 0),
    Message("Sardoche, tu défonces tout sur ton passage !", 0),
    Message("Ce que tu fais c'est du lourd, t'es un vrai crack !", 0),
    Message("PTDR, t'es trop nul, désinstalle ce jeu frère !", 1),
    Message("Sardoche, t'es une machine de guerre, GG !", 0),
    Message("Les haters vont toujours te follow unfollow, fuck them !", 1),
    Message("Respect Sardoche, tu gères comme un boss !", 0),
    Message("Sardoche, je suis fan depuis la nightbot, t'es un dieu !", 0),
    Message("C'est trop relou, change de jeu bro, c'est chaud...", 1),
    Message("T'es OP Sardoche, tu déchires tout !", 0),
    Message("Sardoche, tu kiffes les clutchs, t'es un vrai showman !", 0),
    Message("MDR, arrête de rager, ça fait du LOL dans le chat !", 1),
    Message("Sardoche, t'es un aimbot vivant, GG EZ !", 0),
    Message("Ce stream est ultra boring, je pique du nez...", 1),
    Message("Sardoche, t'es un ouf, tu fais péter les records !", 0),
    Message("T'es vraiment trop noob, désinstalle tout frère !", 1),
    Message("Sardoche, tu es le streamer le plus OP de tous les temps !", 0),
    Message("Les haters vont toujours hate, laisse-les dans leur délire !", 1),
    Message("Je suis fan de ton skill, tu mets tout le monde à l'amende !", 0),
    Message("Sardoche, t'es la légende vivante de Twitch !", 0),
    Message("Ce stream est une purge totale, change de game direct...", 1),
    Message("Sardoche, t'es un crack de la stratégie, respect !", 0),
    Message("Arrête de pleurer, ça me rend Kappa Kappa...", 1),
    Message("PTDR, t'es trop troll, j'adore quand tu te lâches !", 0),
    Message("Sardoche, tu es le king incontesté de la streamosphère !", 0)
]

# Extraction des fonctionnalités et préparation des étiquettes
corpus = [message.text for message in messages]
labels = [message.label for message in messages]
if generate_model == False :

    # Extraction des fonctionnalités avec la représentation en sac de mots
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)

    # Division de l'ensemble de données
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Entraînement du modèle de forêt aléatoire
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Sauvegarde du modèle
    joblib.dump(model, 'modele.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

# Chargement du modèle sauvegardé
loaded_model = joblib.load('modele.pkl')
loaded_vectorizer = joblib.load('vectorizer.pkl')

# Prétraitement des messages de l'ensemble de test
X_test_text = [message.text for message in messages]
X_test_transformed = loaded_vectorizer.transform(X_test_text)

# Utilisation du modèle chargé pour des prédictions sur l'ensemble de test
y_pred = loaded_model.predict(X_test_transformed)
print(classification_report(labels, y_pred))