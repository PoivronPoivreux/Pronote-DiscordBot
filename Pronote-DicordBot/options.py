from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
from io import BytesIO

driver = webdriver.Chrome()
driver.get("Ton lien d'accès à la page de connexion de ton ENT")

driver.implicitly_wait(10)  # attendre 10 secondes maximum

# Localiser le champ de saisie en utilisant son ID, sa classe ou son nom
input_field = driver.find_element(By.ID, "email")

# Utiliser la méthode "send_keys" pour saisir du texte dans le champ de saisie
input_field.send_keys("ton nom d'utilisateur")

# Localiser le champ de saisie en utilisant son ID, sa classe ou son nom
input_field = driver.find_element(By.ID, "password")

# Utiliser la méthode "send_keys" pour saisir du texte dans le champ de saisie
input_field.send_keys("Ton mot de passe")

# Localiser le bouton en utilisant son ID, sa classe ou son nom
button = driver.find_element(By.CLASS_NAME, "flex-magnet-bottom-right")

# Utiliser la méthode "click()" pour simuler un clic sur le bouton
button.click()

# Localiser la partie spécifique de la page
element = driver.find_element(By.ID, "id_70")

# Utiliser la méthode "screenshot_as_png" pour capturer une image de la partie spécifique
image = element.screenshot_as_png

# Charger l'image en utilisant PIL
im = Image.open(BytesIO(image))

# Enregistrer l'image recadrée sur le disque
im.save("emploi.png")
