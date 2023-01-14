# Pronote-DiscordBot
Un bot discord qui en une seule commande récupère ton emploi du temps de ton interface pronote.


<details><summary>Installation</summary>
<p>

Avant toute chose il faudra installer ``Python`` sur le site de Python : https://www.python.org/downloads/.

Après il faudra installer ``Pillow``, ``dicord.py`` et ``Selenium`` :

```ruby
pip install Pillow
pip install discord.py
pip install selenium
```
Puis, une fois installé il faudra télécharger la dernière version de ``Pronote-DiscordBot`` [ici](https://github.com/PoivronPoivreux/Pronote-DiscordBot/releases/tag/Pronote-DicordBot) !
  
Et il faudra modifier le fichier ``bot.py`` et ``options.py``.
</p>
</details>

<details><summary>Modifications</summary>
<p>

``bot.py :``<br>
<br>
Il faut modifier le fichier comme marqué il faut donc modifier le token du bot (trouvable sur le [Portail des développeurs de Discord](https://discord.com/developers/applications) un tuto juste [là](https://www.youtube.com/watch?v=Y8RcqgmYVU8)) ainsi que l'ID du salon de ton serveur discord (trouvable en activant le mode développeur de discord dans tes paramètres et en faisant un clic droit sur le salon).
  
``options.py :``<br>
<br>
Il faut modifier le lien vers ton ENT, ton nom d'utilisateur et ton mot de passe (lors de la connextion à l'ENT il se peut qu'il y ait une erreur. En cas d'erreur il faut aller dans la section ``Aide``).

</p>
</details>
<details><summary>Aide</summary>
<p>

Si vous rencontrez une difficulté lors de la connexion à l'ENT il faut appuyer sur la touche ``F12`` depuis votre google et non celui de ``Selenium`` puis appuyer sur les touches ``CTRL + Shift + C`` et pointer les deux champs de saisie l'un après l'autre pour récupérer l'ID de chacun dans la partie sur la droite de votre écran puis les mettre à la place de ``email`` et ``password`` dans le fichier ``options.py``.

</p>
</details>
