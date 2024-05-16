import streamlit as st
from PIL import Image
import datetime
import time
from dateutil.relativedelta import relativedelta
import pandas as pd
import random

# Fonction pour lire les messages d'amour depuis un fichier CSV
def get_random_message(file_path):
    df = pd.read_csv(file_path)
    messages = df['message'].tolist()
    return random.choice(messages)

# Titre
st.title("Joyeuse Saint-Valentin !")

# Message personnalisé
file_path = 'messages.csv'  # Chemin vers votre fichier CSV
random_message = get_random_message(file_path)
message = f"Ma choupinette, je te souhaite une merveilleuse Saint-Valentin. Voici quelques souvenirs de nos moments ensemble. Je t'aime !\n\nMessage spécial : {random_message}"
st.write(message)

# Jouer une chanson
st.write("Notre chanson préférée en vidéo :")
url_video = "https://www.youtube.com/watch?v=v8oqbWrP1QY"
st.video(url_video)

# Définir la date de début de la relation
start_date = datetime.datetime(2022, 10, 1)

# Calculer la différence de temps
def calculate_time_difference(start_date):
    now = datetime.datetime.now()
    time_difference = now - start_date
    return time_difference

# Afficher le compteur
def display_counter():
    st.write("Depuis que nous sommes ensemble :")
    time_difference = calculate_time_difference(start_date)
    st.write(f"{time_difference.days} jours, {time_difference.seconds // 3600} heures, "
             f"{(time_difference.seconds // 60) % 60} minutes et {time_difference.seconds % 60} secondes.")

# Mettre à jour le compteur toutes les secondes
while True:
    display_counter()
    time.sleep(1)
    st.experimental_rerun()
