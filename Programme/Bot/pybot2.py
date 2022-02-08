from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyperclip

class Bot() :
	def __init__(self):
		### Paramètres ###
		self.LargeurEcran = 720
		self.HauteurEcran = 480 
		self.Ecran = Tk()
		self.Ecran.title("Le Botchat de Jolan")
		self.Ecran.geometry("720x480+200+40")
		self.Ecran.resizable(width=0, height=0)
		self.CanvaUn = Canvas(self.Ecran, width=self.LargeurEcran, height=self.HauteurEcran, bg="black")
		self.CanvaUn.pack()

		### Variables ###
		self.texteUn = ""
		self.texteDeux = ""
		self.texteTrois = ""
		self.texteQuatre = ""
		self.texteCinq = ""
		self.texteSix = ""
		self.texteSept = ""
		self.texteHuit = ""

		### Création du bot ###
		self.chatbot = ChatBot("Jolan")
		trainer = ListTrainer(self.chatbot)
		
		trainer.train([
		 	'Salut',
			'Salut, Comment allez-vous ?',
			'Je vais bien',
			'Que puis-je faire pour vous ?',
		 ])

		### Démarrage ###
		self.pagePrincipale()
		self.Ecran.mainloop()

	def pagePrincipale(self):
		### Reset ###
		self.CanvaUn.delete(ALL)

		### Images ###
		self.BackgroundDécor = PhotoImage(file="background.png")
		self.CanvaUn.create_image(self.LargeurEcran / 2, self.HauteurEcran / 2, image=self.BackgroundDécor)

		### Boutons ###
		self.boutonQuitter = Button(self.Ecran, text=" Quitter ", font=("OCR A Extended", 15), bg='#ffe5ea', fg='black', command=self.QuitterLejeux)
		self.boutonQuitter = self.CanvaUn.create_window((self.LargeurEcran/2)-285, 450, window=self.boutonQuitter)

		### Fonction ###
		def récupérationDuTexte():
			texte = un_entry.get()
			if (texte != "Entrer un message" and texte != "") :
				response = self.chatbot.get_response(texte)
				self.changerDeTexte(texte, response)
				self.pagePrincipale()

		def entry_clear(e):
			un_entry.delete(0, END)

		### Saisie  ###
		un_entry = Entry(self.Ecran, font=("Helvectica", 24), width=20, fg="#336d92", bd=0)
		un_window = self.CanvaUn.create_window((self.LargeurEcran/2)-10, 425, anchor="n", height=45, width=410,window=un_entry)
		un_entry.insert(0, "Entrer un message")
		un_entry.bind("<Button-1>", entry_clear)

		### Boutons ###
		self.boutonSendMessage = Button(self.Ecran, text="Send", font=("OCR A Extended", 15), bg='#5CB6AD', fg='black', command=récupérationDuTexte)
		self.boutonSendMessage = self.CanvaUn.create_window((self.LargeurEcran/2)+245, 450, window=self.boutonSendMessage)
		self.boutonCopy = Button(self.Ecran, text="Copy", font=("OCR A Extended", 15), bg='#5CB6FF', fg='black', command=self.copierLeTexte)
		self.boutonCopy = self.CanvaUn.create_window((self.LargeurEcran/2)+320, 450, window=self.boutonCopy)

		### Textes ###
		self.résultaCode = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+150, text="", font=("OCR A Extended", 30), fill="#1CF8FF")

		### Tchat ###
		self.chatUserPositionUn = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+150, text=self.texteUn, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionDeux = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+100, text=self.texteDeux, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionTrois = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)+50, text=self.texteTrois, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionQuatre = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2), text=self.texteQuatre, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionCinq = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)-50, text=self.texteCinq, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionSix = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2-100), text=self.texteSix, font=("OCR A Extended", 22), fill="#6CB6BB")
		self.chatUserPositionSept = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2)-150, text=self.texteSept, font=("OCR A Extended", 22), fill="#EAD0E2")
		self.chatUserPositionHuit = self.CanvaUn.create_text((self.LargeurEcran/2), (self.HauteurEcran/2-200), text=self.texteHuit, font=("OCR A Extended", 22), fill="#6CB6BB")

	def QuitterLejeux(self):
		self.Ecran.destroy()

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

lancerFenetre = Bot()
lancerFenetre


