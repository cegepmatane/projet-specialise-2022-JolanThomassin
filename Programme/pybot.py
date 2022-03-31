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
		self.largeurEcran = 1000
		self.hauteurEcran = 500
		# Création de l'écran #
		self.ecranLogiciel = Tk()
		self.ecranLogiciel.title("Le Botchat de Jolan")
		self.ecranLogiciel.geometry("1000x500+200+40")
		self.ecranLogiciel.resizable(width=0, height=0)

		self.canvaEcranLogiciel = Canvas(self.ecranLogiciel, width=self.largeurEcran/2, height=self.hauteurEcran, bg="black")
		self.canvaEcranLogiciel.pack(side=LEFT)

		self.canvaEcranLogicielTrois = Canvas(self.ecranLogiciel, width=self.largeurEcran/2, height=self.hauteurEcran/8, bg="blue")
		self.canvaEcranLogicielTrois.pack(side=BOTTOM)

		self.canvaEcranLogicielDeux = Canvas(self.ecranLogiciel, width=self.largeurEcran/2, height=self.hauteurEcran, bg="red")
		self.canvaEcranLogicielDeux.pack(side=TOP)

		self.bot = ChatBot('Bot')

		### Démarrage ###
		self.pagePrincipale()
		self.ecranLogiciel.mainloop()

	def pagePrincipale(self):
		### Reset de l'écran ###
		self.canvaEcranLogiciel.delete(ALL)

		def botReply(event):
		    question= r.get()
		    question=question.capitalize()
		    answer=self.bot.get_response(question)
		    self.textarea.insert(END,'Vous : '+question+'\n\n')
		    self.textarea.insert(END,'Deep : '+str(answer)+'\n\n')
		    self.questionField.delete(0,END)
		    self.textarea.yview_moveto(1)

		### Images du chatbot ###
		self.imageDeFond = PhotoImage(file="../Personnage/basique.png")
		self.canvaEcranLogiciel.create_image(self.largeurEcran / 2 / 2, self.hauteurEcran / 2, image=self.imageDeFond)

		### Zone d'affichage du texte ###
		self.textarea = Text(self.canvaEcranLogicielDeux, font=('times new roman',20,'bold'), wrap='word', bg='black', fg='white')
		self.textarea.pack(fill=BOTH)

		### Barre de texte ###
		r = StringVar() 
		self.questionField=Entry(self.canvaEcranLogicielTrois, font=('verdana', int(self.hauteurEcran/12) ,'bold'), textvariable=r, bg='grey', fg='white')
		self.questionField.pack(fill=BOTH)
		self.questionField.bind('<Return>', botReply)



lancementLogiciel = Bot()
lancementLogiciel