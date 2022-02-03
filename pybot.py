from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import fr_dep_news_trf
nlp = fr_dep_news_trf.load()

chatbot = ChatBot("Lucas")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.french")

while True:
	request = input('Vous : ')
	response= chatbot.get_response(request)
	print('Bot : ', response)