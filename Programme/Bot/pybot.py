from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyperclip
import urllib.request
import re

class Bot() :
	def __init__(self):
		### Paramètres ###
		self.largeurEcran = 720
		self.hauteurEcran = 480 
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

		### Train pour Youtube ###
		trainer.train([
		 	'Youtube',
			'Quel vidéo/musique cherchez vous ?',
		])

		### Démarrage ###
		self.pagePrincipale()
		self.ecranLogiciel.mainloop()

	def pagePrincipale(self):
		### Reset ###
		self.canvaEcranLogiciel.delete(ALL)

		### Images ###
		self.BackgroundDécor = PhotoImage(file="background.png")
		self.canvaEcranLogiciel.create_image(self.largeurEcran / 2, self.hauteurEcran / 2, image=self.BackgroundDécor)

		### Boutons ###
		self.boutonQuitter = Button(self.ecranLogiciel, text=" Quitter ", font=("OCR A Extended", 15), bg='#ffe5ea', fg='black', command=self.QuitterLejeux)
		self.boutonQuitter = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)-285, 450, window=self.boutonQuitter)

		### Fonction ###
		def récupérationDuTexte():
			texte = un_entry.get()
			if self.modeRechercheYoutubeActif == False :
				if (texte != "Entrez un message" and texte != "") :
					response = self.chatbot.get_response(texte)
					if str(response) == 'Quel vidéo/musique cherchez vous ?' :
						self.modeRechercheYoutubeActif = True
					self.changerDeTexte(texte, response)
					self.pagePrincipale()
			else :
				url = self.rechercheVideoSurYoutube(texte)
				self.modeRechercheYoutubeActif = False
				self.changerDeTexte(texte, url)
				self.pagePrincipale()
				
		def entry_clear(e):
			un_entry.delete(0, END)

		### Saisie  ###
		un_entry = Entry(self.ecranLogiciel, font=("Helvectica", 24), width=20, fg="#336d92", bd=0)
		un_window = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)-10, 425, anchor="n", height=45, width=410,window=un_entry)
		un_entry.insert(0, "Entrez un message")
		un_entry.bind("<Button-1>", entry_clear)

		### Boutons ###
		self.boutonSendMessage = Button(self.ecranLogiciel, text="Send", font=("OCR A Extended", 15), bg='#5CB6AD', fg='black', command=récupérationDuTexte)
		self.boutonSendMessage = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)+245, 450, window=self.boutonSendMessage)
		self.boutonCopy = Button(self.ecranLogiciel, text="Copy", font=("OCR A Extended", 15), bg='#5CB6FF', fg='black', command=self.copierLeTexte)
		self.boutonCopy = self.canvaEcranLogiciel.create_window((self.largeurEcran/2)+320, 450, window=self.boutonCopy)

		### Textes ###
		self.résultaCode = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+150, text="", font=("OCR A Extended", 30), fill="#1CF8FF")

		### Tchat ###
		self.chatUserPositionUn = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+150, text=self.texteUn, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionDeux = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+100, text=self.texteDeux, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionTrois = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)+50, text=self.texteTrois, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionQuatre = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2), text=self.texteQuatre, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionCinq = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)-50, text=self.texteCinq, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionSix = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2-100), text=self.texteSix, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionSept = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2)-150, text=self.texteSept, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionHuit = self.canvaEcranLogiciel.create_text((self.largeurEcran/2), (self.hauteurEcran/2-200), text=self.texteHuit, font=("OCR A Extended", 22), fill="#6CB6BB")

	def QuitterLejeux(self):
		self.ecranLogiciel.destroy()

	def copierLeTexte(self):
		pyperclip.copy(str(self.texteUn))
		spam = pyperclip.paste()

	def changerDeTexte(self, texte, response):
		self.texteHuit = self.texteSix
		self.texteSept = self.texteCinq
		self.texteSix = self.texteQuatre
		self.texteCinq = self.texteTrois
		self.texteQuatre = self.texteDeux
		self.texteTrois = self.texteUn
		self.texteDeux = texte
		self.texteUn = response

	def rechercheVideoSurYoutube(self, texte) :
		search_keyword = texte
		new_string = search_keyword.replace(" ", "+")
		html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + new_string)
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
		return("https://www.youtube.com/watch?v=" + video_ids[0])

lancementLogiciel = Bot()
lancementLogiciel