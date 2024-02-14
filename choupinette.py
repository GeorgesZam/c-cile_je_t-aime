import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# Fonction pour calculer la différence de temps en années, mois, jours, heures, minutes et secondes
def calculate_time_difference(start_date, end_date):
    difference = relativedelta(end_date, start_date)
    return {
        "years": difference.years,
        "months": difference.months,
        "days": difference.days,
        "hours": end_date.hour,
        "minutes": end_date.minute,
        "seconds": end_date.second
    }

# Définir la date de début de la relation
start_date = datetime.datetime(2023, 10, 1)

# Titre
st.title("Joyeuse Saint-Valentin !")

# Message personnalisé
message = "Ma choupinette, je te souhaite une merveilleuse Saint-Valentin. Voici combien de temps nous sommes ensemble :"
st.write(message)

# Jouer une vidéo YouTube
st.write("Notre chanson préférée en vidéo :")
url_video = "https://www.youtube.com/watch?v=v8oqbWrP1QY"
st.video(url_video)

# Affichage de la différence de temps
now = datetime.datetime.now()
time_difference = calculate_time_difference(start_date, now)
st.write(f"{time_difference['years']} années, "
         f"{time_difference['months']} mois, "
         f"{time_difference['days']} jours, "
         f"{time_difference['hours']} heures, "
         f"{time_difference['minutes']} minutes et "
         f"{time_difference['seconds']} secondes.")

# Note: La boucle et la fonction experimental_rerun ont été retirées pour éviter les problèmes de performance.
# Si tu souhaites que le compteur se mette à jour en temps réel, tu devrais considérer une autre approche,
# peut-être avec un callback ou une autre forme d'interaction.
