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
		self.trainer = ListTrainer(self.bot)
		
		# Création d'un menu de navigation
		def redirectionChatbot() :
			self.pagePrincipale()
		def redirectionTraining() :
			self.pageTraining()
		self.menubar = Menu(self.ecranLogiciel)  
		self.menubar.add_command(label="Chatbot", command=redirectionChatbot)  
		self.menubar.add_command(label="Training", command=redirectionTraining)   
		self.ecranLogiciel.config(menu=self.menubar)

		### Initialisation des images ###
		self.image00 = PhotoImage(file="../Personnage/basique.png")
		self.image01 = PhotoImage(file="../Personnage/parle.png")
		self.image02 = PhotoImage(file="../Personnage/triste.png")
		self.imageEmotionPersonnage = [self.image00, self.image01, self.image02]

		### Démarrage ###
		self.textarea = Text(self.canvaEcranLogicielDeux)
		self.questionField = Entry(self.canvaEcranLogicielTrois)
		self.pagePrincipale()
		self.ecranLogiciel.mainloop()

	def pagePrincipale(self):
		### Reset de l'écran ###
		self.canvaEcranLogiciel.delete(ALL)
		self.textarea.destroy()
		self.questionField.destroy()

		with open("listeTraining.txt", "r") as file:
			phrase = ""
			for line in file:
				tableauLigne = []
				for word in line.split():
					if word == "$" :
						tableauLigne.append(phrase[:-1])
						phrase = ""
					else : 
						phrase += word
						phrase += " "
				self.trainer.train([tableauLigne[0], tableauLigne[1]])

		def botReply(event):
			question= r.get()
			if question != "" :
				question = question.lower()
				question = question.capitalize()
				answer = self.bot.get_response(question)
				changementEmotion(answer)
				answer = str(answer)[2:]
				self.textarea.insert(END,'Vous : '+question+'\n\n')
				self.textarea.insert(END,'Deep : '+str(answer)+'\n\n')

				self.questionField.delete(0,END)
				self.textarea.yview_moveto(1)

		def changementEmotion(texteBot) :
			### Récupération des deux premieres caractères de la réponse du bot ###
			rechercheValeurEmotion = False
			compteur = 0
			valeurEmotion = ""
			for lettre in str(texteBot) :
				if compteur <= 1 :
					valeurEmotion = valeurEmotion + lettre
					compteur += 1

			### Traitement de la valeur obtenue ###
			if valeurEmotion == "01" :
				### Parle ###
				self.imageDeFond = self.imageEmotionPersonnage[1]
			elif valeurEmotion == "02" :
				### Triste ###
				self.imageDeFond = self.imageEmotionPersonnage[2]  
			else :
				### Neutre ###
				self.imageDeFond = self.imageEmotionPersonnage[0]
			self.canvaEcranLogiciel.create_image(self.largeurEcran / 2 / 2, self.hauteurEcran / 2, image=self.imageDeFond)


		### Images du chatbot ###
		self.canvaEcranLogiciel.create_image(self.largeurEcran / 2 / 2, self.hauteurEcran / 2, image=self.imageEmotionPersonnage[0])

		### Zone d'affichage du texte ###
		self.textarea = Text(self.canvaEcranLogicielDeux, font=('times new roman',20,'bold'), wrap='word', bg='black', fg='white')
		self.textarea.pack(fill=BOTH)

		### Barre de texte ###
		r = StringVar() 
		self.questionField=Entry(self.canvaEcranLogicielTrois, font=('verdana', int(self.hauteurEcran/12) ,'bold'), textvariable=r, bg='#EDFFF9', fg='black')
		self.questionField.pack(fill=BOTH)
		self.questionField.bind('<Return>', botReply)

	def pageTraining(self) :
		self.canvaEcranLogiciel.delete(ALL)
		self.textarea.destroy()
		self.questionField.destroy()

		self.imageTraining = PhotoImage(file="../Personnage/background.png")
		self.canvaEcranLogiciel.create_image(self.largeurEcran / 2 / 2, self.hauteurEcran / 2, image=self.imageTraining)

		self.etapeProcessus = 0
		self.ligneAjouter = ""
		self.ligneAjouterEphemere = ""

		def affichageTexte(event):
			question = r.get()
			if question != "" :
				question = question.lower()
				question = question.capitalize()
				if (self.etapeProcessus == 0) or (self.etapeProcessus == 2) :
						self.ligneAjouterEphemere = question
						self.textarea.insert(END,question + '\n\n')
						self.questionField.delete(0,END)
						self.textarea.yview_moveto(1)
						self.etapeProcessus += 1
						self.textarea.insert(END,'Sélectionner une émotions (00 - 13) : ' + '\n')
						self.textarea.insert(END,'00 - basique : ' + '\n')
						self.textarea.insert(END,'01 - parle : ' + '\n')
						self.textarea.insert(END,'02 - triste : ' + '\n')
				elif self.etapeProcessus == 1 :
					self.ligneAjouter += question
					self.ligneAjouter += self.ligneAjouterEphemere
					self.ligneAjouter += " $ " 
					self.textarea.insert(END, question + '\n\n')
					self.questionField.delete(0,END)
					self.textarea.yview_moveto(1)
					self.etapeProcessus += 1
					self.textarea.insert(END,'Entrer le deuxième message : ' + '\n')
				elif self.etapeProcessus == 3 :
					self.ligneAjouter += question
					self.ligneAjouter += self.ligneAjouterEphemere
					self.ligneAjouter += " $ "
					self.textarea.insert(END, question + '\n\n')
					self.questionField.delete(0,END)
					self.textarea.yview_moveto(1)

					self.ligneAjouter = "\n" + self.ligneAjouter
					
					file_object = open('listeTraining.txt', 'a')
					# Append 'hello' at the end of file
					file_object.write(self.ligneAjouter)
					# Close the file
					file_object.close()

					self.pageTraining()

		### Zone d'affichage du texte ###
		self.textarea = Text(self.canvaEcranLogicielDeux, font=('times new roman',20,'bold'), wrap='word', bg='black', fg='white')
		self.textarea.pack(fill=BOTH)
		self.textarea.insert(END,'Entrer le premier message : ' + '\n')

		### Barre de texte ###
		r = StringVar() 
		self.questionField=Entry(self.canvaEcranLogicielTrois, font=('verdana', int(self.hauteurEcran/12) ,'bold'), textvariable=r, bg='#EDFFF9', fg='black')
		self.questionField.pack(fill=BOTH)

		def entry_clear(e):
			self.questionField.delete(0, END)

		self.questionField.bind('<Return>', affichageTexte)


		



lancementLogiciel = Bot()
lancementLogiciel