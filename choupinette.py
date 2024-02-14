import streamlit as st
from PIL import Image

# Titre
st.title("Joyeuse Saint-Valentin !")

# Message personnalisé
message = "Ma choupinette, je te souhaite une merveilleuse Saint-Valentin. Voici quelques souvenirs de nos moments ensemble. Je t'aime !"
st.write(message)

# Jouer une chanson
st.write("Notre chanson préférée en vidéo :")
url_video = "https://www.youtube.com/watch?v=v8oqbWrP1QY"
st.video(url_video)
