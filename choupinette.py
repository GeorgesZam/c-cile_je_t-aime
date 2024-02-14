import streamlit as st
from PIL import Image

# Titre
st.title("Joyeuse Saint-Valentin !")

# Message personnalisé
message = "Mon amour, je te souhaite une merveilleuse Saint-Valentin. Voici quelques souvenirs de nos moments ensemble. Je t'aime !"
st.write(message)
"""
# Afficher une image
image_path = "chemin_vers_ta_photo.jpg"
image = Image.open(image_path)
st.image(image, caption="Nous ❤️")
"""
# Jouer une chanson
st.write("Notre chanson préférée en vidéo :")
url_video = "https://www.youtube.com/watch?v=v8oqbWrP1QY"
st.video(url_video)
