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
### Auto training ###
import time
import random

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
		self.timer = 0

		### Création du bot ###
		self.chatbot = ChatBot("Jolan")
		trainer = ListTrainer(self.chatbot)
		
		### Train en cours ###
		### Train pour Loisirs / Passions ###
		### Loisirs ###
		trainer.train([
		 	'Quel sont tes loisirs ?',
			"J'aime la programmation et regarder des films, et vous ?",
		])
		trainer.train([
		 	'Loisirs ?',
			"J'aime la programmation et regarder des films, et vous ?",
		])
		trainer.train([
		 	'As tu des loisirs ?',
			"J'aime la programmation et regarder des films, et vous ?",
		])
		trainer.train([
		 	"Comment t'occupes tu ?",
			"J'aime la programmation et regarder des films, et vous ?",
		])
		trainer.train([
		 	"Que fais tu ?",
			"Je parle avec vous",
		])

		### Passions ###
		trainer.train([
		 	'Quel sont tes passions ?',
			"J'aime la programmation et regarder des filmset vous ?",
		])
		trainer.train([
		 	"Qu'aimes tu faires ?",
			"J'aime la programmation et regarder des filmset vous ?",
		])
		trainer.train([
		 	"Passions ?",
			"J'aime la programmation et regarder des filmset vous ?",
		])

		### Film ###
		trainer.train([
		 	'Quel genre de film aime tu ?',
			"J'aime les films de gladiateurs, et vous ?",
		])
		trainer.train([
		 	'Tu aimes les films ?',
			"J'aime les films de gladiateurs, et vous ?",
		])
		trainer.train([
		 	'Films ?',
			"J'aime les films de gladiateurs, et vous ?",
		])

		### Réponses ###
		trainer.train([
		 	'Moi aussi',
			"Nous avons tous deux bon gouts alors.",
		])
		trainer.train([
		 	'Idem',
			"Nous avons tous deux bon gouts alors.",
		])
		trainer.train([
		 	"Je n'aimes pas ça",
			"Notre différence fait notre force !",
		])
		trainer.train([
		 	"Je préfères autre choses",
			"Notre différence fait notre force !",
		])

		### Train pour Présentation ###
		### Nom et rôle ###
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
		trainer.train([
		 	'Tu es qui ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])

		### Âge ###
		trainer.train([
		 	'Quel âge as tu ?',
			'Je suis né le 25 janvier 2022',
		])
		trainer.train([
		 	'Quel es ta date de naissance ?',
			'Je suis né le 25 janvier 2022',
		])
		trainer.train([
		 	'Quand es tu né ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'En quel année tu es né ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'En quel mois tu es né ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'Quel mois tu es né ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
		])
		trainer.train([
		 	'Quel jours tu es né ?',
			'Bonjour je suis Deep un chatbot réalisé en Python',
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
		### Train pour Humour ###
		trainer.train([
		 	'Raconte moi une blague',
			'La plage dit à l’océan : dire que tout le monde aime l’eau c’est assez vague',
		])
		trainer.train([
		 	'Raconte moi une blague',
			'C’est un panda qui en avait marre de la vie et un jour, il se panda…',
		])
		trainer.train([
		 	'Raconte moi une blague',
			'Que fait un poussin de 200kg ? PIOUUUU! PIOUUUU',
		])
		### Train pour la météo ###
		trainer.train([
		 	'Météo',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'météo',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Température',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'température',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Quel est la météo',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Quel est la température',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Quel est le temps de dehors ?',
			'Voici la température dans votre région : ',
		])
		trainer.train([
		 	'Quel est le temps de dehors',
			'Voici la température dans votre région : ',
		])
		### Train pour Youtube ###
		trainer.train([
		 	'Youtube',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'Ytb',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'YouTube',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'Je veux faire une recherche youtube',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'Recherche youtube',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'Recherche Youtube',
			'Quel vidéo/musique cherchez vous ?',
		])
		trainer.train([
		 	'Recherche YouTube',
			'Quel vidéo/musique cherchez vous ?',
		])
		### Train pour Début ###
		### Salutation ###
		trainer.train([
		 	'Salut',
			'Salut, Comment allez-vous ?',
		])
		trainer.train([
		 	'Hey',
			'Salut, Comment allez-vous ?',	
		])
		trainer.train([
		 	'Wesh',
			'Salut, Comment allez-vous ?',
		])
		trainer.train([
		 	'Bonjour',
			'Salut, Comment allez-vous ?',
		])
		trainer.train([
		 	'Bonsoir',
			'Salut, Comment allez-vous ?',
		])
		trainer.train([
		 	'Allo',
			'Salut, Comment allez-vous ?',
		])
		trainer.train([
		 	'Bon matin',
			'Salut, Comment allez-vous ?',
		])

		### État ###
		trainer.train([
		 	'Je vais bien',
			'Heureux pour vous ! Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Je vais mal',
			'Dommage, que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Bien',
			'Que puis-je faire pour vous ?',
		])
		trainer.train([
		 	'Mal',
			'Dommage, que puis-je faire pour vous ?',
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
			self.timer = 0
			texte = entreeUtilisateur.get()
			if self.modeRechercheYoutubeActif == False :
				if (texte != "Entrez un message" and texte != "") :
					if (texte == "lancement training") :
						def autoTrain() :
							while self.timer <= 50 :
								texte = ["Hey","Salut","Bonjour","Wesh","Bon matin","Allo", "Je vais bien",
								"Je vais mal", "Raconte moi une blague", "En quel année tu es né ?", "Quel es ta date de naissance ?",
								"Quel âge as tu ?","Quel mois tu es né ?","Tu es qui ?","Présente toi","Tu aimes les films ?",
								"Qu'aimes tu faires ","Quel sont tes passions ?","Que fais tu ?","As tu des loisirs ?",
								"Quel sont tes loisirs ?"]
								valeurAleatoire = random.randint(0, (len(texte)-1) )
								reponseDuBot = self.chatbot.get_response(texte[valeurAleatoire])
								self.changerDeTexte(texte[valeurAleatoire], reponseDuBot)
								self.pagePrincipale()
								self.timer += 1
								self.canvaEcranLogiciel.after(10, autoTrain)
						autoTrain()
					else :
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
		compteurUn = 0
		compteurDeux = 0 
		for i in range(0, len(texte)) :
			compteurUn += 1
		for y in range(0, len(str(reponseDuBot))) :
			compteurDeux += 1
		if compteurUn < compteurDeux :
			compteurUn = compteurDeux

		if compteurUn < 62 :
			self.police = 14
		elif compteurUn >= 62 :
			self.police = 10

		self.texteHuit = self.texteSix
		self.texteSept = self.texteCinq
		self.texteSix = self.texteQuatre
		self.texteCinq = self.texteTrois
		self.texteQuatre = self.texteDeux
		self.texteTrois = self.texteUn
		self.texteDeux = texte
		self.texteUn = reponseDuBot

	def rechercheVideoSurYoutube(self, texte) : 
		nouveauTexte = texte.replace(" ", "+")
		lienRechercheVideo = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + nouveauTexte)
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