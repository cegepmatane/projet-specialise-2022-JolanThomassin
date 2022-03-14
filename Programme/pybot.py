### Interface graphique ###
from tkinter import *
### IA / Bot ###
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
### Copie presse papier ###
import pyperclip
### Youtube ###
import urllib.request
import re
### Météo ###
from requests_html import HTMLSession

class Bot() :
	def __init__(self):
		### Paramètres ###
		# Définition des dimensions de l'écran #
		self.largeurEcran = 720
		self.hauteurEcran = 480
		# Création de l'écran #
		self.ecranLogiciel = Tk()
		self.ecranLogiciel.title("Le Botchat de Jolan")
		self.ecranLogiciel.geometry("720x480+200+40")
		self.ecranLogiciel.resizable(width=0, height=0)
		self.canvaEcranLogiciel = Canvas(self.ecranLogiciel, width=self.largeurEcran, height=self.hauteurEcran, bg="black")
		self.canvaEcranLogiciel.pack()

		### Variables ###
		self.texteUn = ""
		self.texteDeux = ""
		self.texteTrois = ""
		self.texteQuatre = ""
		self.texteCinq = ""
		self.texteSix = ""
		self.texteSept = ""
		self.texteHuit = ""
		self.modeRechercheYoutubeActif = False
		self.police = 14

		### Création du bot ###
		self.chatbot = ChatBot("Jolan")
		trainer = ListTrainer(self.chatbot)
		
		### Train pour Début de conversation ###
		trainer.train([
		 	'Salut',
			'Salut, Comment allez-vous ?',
			'Je vais bien',
			'Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Hey',
			'Salut, Comment allez-vous ?',
			'Je vais bien',
			'Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Wesh',
			'Salut, Comment allez-vous ?',
			'ca va',
			'Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Bonjour',
			'Salut, Comment allez-vous ?',
			'Super',
			'Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Bonsoir',
			'Salut, Comment allez-vous ?',
			'Bien',
			'Que puis-je faire pour vous ?',
		])

		### Train pour Présentation ###
		trainer.train([
		 	'Présente toi',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'Qui es tu ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'Tu es ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'Présentation',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])

		### Train pour Loisirs / Passions ###
		trainer.train([
		 	'Quel sont tes loisirs ?',
			"J'aime la programmation et regarder des films",
			"Quel film ?",
			"Les films de gladiateurs",
		])
		trainer.train([
			"Quel genre de film ?",
			"Les films de gladiateurs",
		])
		trainer.train([
		 	'loisirs ?',
			"J'aime la programmation et regarder des films",
		])
		trainer.train([
		 	'Quesque tu aimes faire ?',
			"J'aime la programmation et regarder des films",
		])
		trainer.train([
		 	'Quesque tu aimes ?',
			"J'aime la programmation et regarder des films",
		])
		trainer.train([
		 	'Quel film aimes tu ?',
			"J'aime les films de gladiateurs",
		])
		trainer.train([
		 	'Quel sont tes passions ?',
			"J'aime les films de gladiateurs",
		])

		### Train pour GIT ###
		trainer.train([
		 	'Git',
			'https://github.com/cegepmatane/projet-specialise-2022-JolanThomassin',
		])
		trainer.train([
		 	'lien du Git',
			'https://github.com/cegepmatane/projet-specialise-2022-JolanThomassin',
		])
		trainer.train([
		 	'GitHub',
			'https://github.com/cegepmatane/projet-specialise-2022-JolanThomassin',
		])
		trainer.train([
		 	'ton GitHub',
			'https://github.com/cegepmatane/projet-specialise-2022-JolanThomassin',
		])
		trainer.train([
		 	'ton git',
			'https://github.com/cegepmatane/projet-specialise-2022-JolanThomassin',
		])

		### Train pour la météo ###
		trainer.train([
		 	'Météo',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Température',
			'Voici la température dans votre région : ',
		])

		### Train pour Youtube ###
		trainer.train([
		 	'Youtube',
			'Quel vidéo/musique cherchez vous ?',
		])

		### Train pour Loisirs ###
		trainer.train([
		 	'Quels sont tes loisirs ?',
			'Discuter avec vous.',
		])

		### Démarrage ###
		self.pagePrincipale()
		self.ecranLogiciel.mainloop()

	def pagePrincipale(self):
		### Reset de l'écran ###
		self.canvaEcranLogiciel.delete(ALL)

		### Images du chatbot ###
		self.imageDeFond = PhotoImage(file="background.png")
		self.canvaEcranLogiciel.create_image(self.largeurEcran / 2, self.hauteurEcran / 2, image=self.imageDeFond)

		### Fonction ###
		def récupérationDuTexte():
			texte = entreeUtilisateur.get()
			if self.modeRechercheYoutubeActif == False :
				if (texte != "Entrez un message" and texte != "") :
					reponseDuBot = self.chatbot.get_response(texte)
					if str(reponseDuBot) == 'Quel vidéo/musique cherchez vous ?' :
						self.modeRechercheYoutubeActif = True
					elif str(reponseDuBot) == 'Voici la température dans votre région :' :
						reponseDuBot = 'Voici la température dans votre région : ' + str(self.getMétéo()) + '°C' 
					self.changerDeTexte(texte, reponseDuBot)
					self.pagePrincipale()
			else :
				lienVideoYoutube = self.rechercheVideoSurYoutube(texte)
				self.modeRechercheYoutubeActif = False
				self.changerDeTexte(texte, lienVideoYoutube)
				self.pagePrincipale()
				
		def suppressionTexteBarreDeSaisie(e):
			entreeUtilisateur.delete(0, END)

		### Saisie ###
		entreeUtilisateur = Entry(self.ecranLogiciel, font=("Helvectica", 24), width=20, fg="#336d92", bd=0)
		barreDeSaisie = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)-10, 425, anchor="n", height=45, width=410,window=entreeUtilisateur)
		entreeUtilisateur.insert(0, "Entrez un message")
		entreeUtilisateur.bind("<Button-1>", suppressionTexteBarreDeSaisie)

		### Boutons du chatbot ###
		self.boutonEnvoieTexte = Button(self.ecranLogiciel, text="Send", font=("OCR A Extended", 15), bg='#5CB6AD', fg='black', command=récupérationDuTexte)
		self.boutonEnvoieTexte = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)+245, 450, window=self.boutonEnvoieTexte)
		self.boutonDeCopie = Button(self.ecranLogiciel, text="Copy", font=("OCR A Extended", 15), bg='#5CB6FF', fg='black', command=self.copierLeTexte)
		self.boutonDeCopie = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)+320, 450, window=self.boutonDeCopie)
		self.boutonQuitterApplication = Button(self.ecranLogiciel, text=" Quitter ", font=("OCR A Extended", 15), bg='#ffe5ea', fg='black', command=self.quitterLeJeu)
		self.boutonQuitterApplication = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)-285, 450, window=self.boutonQuitterApplication)

		### Chat de l'application ###
		self.chatUserPositionUn = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+150, text=self.texteUn, font=("OCR A Extended", self.police), fill="#EAD0E2")
		self.chatUserPositionDeux = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+100, text=self.texteDeux, font=("OCR A Extended", self.police), fill="#6CB6BB")
		self.chatUserPositionTrois = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+50, text=self.texteTrois, font=("OCR A Extended", self.police), fill="#EAD0E2")
		self.chatUserPositionQuatre = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2), text=self.texteQuatre, font=("OCR A Extended", self.police), fill="#6CB6BB")
		self.chatUserPositionCinq = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)-50, text=self.texteCinq, font=("OCR A Extended", self.police), fill="#EAD0E2")
		self.chatUserPositionSix = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2-100), text=self.texteSix, font=("OCR A Extended", self.police), fill="#6CB6BB")
		self.chatUserPositionSept = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)-150, text=self.texteSept, font=("OCR A Extended", self.police), fill="#EAD0E2")
		self.chatUserPositionHuit = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2-200), text=self.texteHuit, font=("OCR A Extended", self.police), fill="#6CB6BB")

	def quitterLeJeu(self):
		self.ecranLogiciel.destroy()

	def copierLeTexte(self):
		pyperclip.copy(str(self.texteUn))


	def changerDeTexte(self, texte, reponseDuBot):
		compteur = 0 
		for i in range(0, len(texte)) :
			compteur += 1

		if compteur < 62 :
			self.police = 14
		elif compteur >= 62 :
			self.police = 8

		self.texteHuit = self.texteSix
		self.texteSept = self.texteCinq
		self.texteSix = self.texteQuatre
		self.texteCinq = self.texteTrois
		self.texteQuatre = self.texteDeux
		self.texteTrois = self.texteUn
		self.texteDeux = texte
		self.texteUn = reponseDuBot

	def rechercheVideoSurYoutube(self, texte) :
		motRecherche = texte
		new_string = motRecherche.replace(" ", "+")
		lienRechercheVideo = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_string)
		lienVideo = re.findall(r"watch\?v=(\S{11})", lienRechercheVideo.read().decode())
		return("https://www.youtube.com/watch?v=" + lienVideo[0])

	def getMétéo(self):
		sessionWEB = HTMLSession()
		lieuRecherche = 'matane'
		url = f'https://www.google.com/search?q=weather+{lieuRecherche}'
		navigateurUtilise = sessionWEB.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50'})
		return(navigateurUtilise.html.find('span#wob_tm', first=True).text)

lancementLogiciel = Bot()
lancementLogiciel