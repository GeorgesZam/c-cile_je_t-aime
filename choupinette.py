import streamlit as st
import pandas as pd
import random
from PIL import Image
import datetime
import time
from dateutil.relativedelta import relativedelta

# Titre
st.title("Joyeuse Saint-Valentin !")

# Message personnalisé
message = "Ma choupinette, je te souhaite une merveilleuse Saint-Valentin. Voici quelques souvenirs de nos moments ensemble. Je t'aime !"
st.write(message)

# Jouer une chanson
st.write("Notre chanson préférée en vidéo :")
url_video = "https://www.youtube.com/watch?v=v8oqbWrP1QY"
st.video(url_video)

# Lire les phrases depuis le fichier CSV
@st.cache_data
def read_phrases(file_path):
    df = pd.read_csv(file_path)
    phrases = df['phrase'].tolist()  # Assurez-vous que votre CSV a une colonne nommée 'phrase'
    return phrases

# Sélectionner une phrase aléatoire
def get_random_phrase(phrases):
    return random.choice(phrases)

# Définir la date de début de la relation
start_date = datetime.datetime(2022, 10, 1)

# Calculer la différence de temps
def calculate_time_difference(start_date):
    now = datetime.datetime.now()
    time_difference = now - start_date
    return time_difference

# Réserver un emplacement pour la phrase aléatoire
phrase_placeholder = st.empty()

# Afficher le compteur
def display_counter():
    st.write("Depuis que nous sommes ensemble :")
    time_difference = calculate_time_difference(start_date)
    st.write(f"{time_difference.days} jours, {time_difference.seconds // 3600} heures, "
             f"{(time_difference.seconds // 60) % 60} minutes et {time_difference.seconds % 60} secondes.")

# Lire les phrases une seule fois
phrases = read_phrases("phrase.csv")

# Boucle pour mettre à jour la phrase et le compteur
while True:
    # Afficher une phrase aléatoire
    random_phrase = get_random_phrase(phrases)
    phrase_placeholder.write(f"Phrase aléatoire : {random_phrase}")

    # Afficher le compteur
    display_counter()

    # Attendre 10 secondes avant de mettre à jour
    time.sleep(10)
    st.experimental_rerun()
