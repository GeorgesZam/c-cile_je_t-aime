import streamlit as st
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

#compteur

# Définir la date de début de la relation
start_date = datetime.datetime(2023, 10, 1)

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

