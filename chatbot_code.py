from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/lokesh jallu/Desktop/Hackathon1/Soft/'):
        data = open('C:/Users/lokesh jallu/Desktop/Hackathon1/Soft/'+files,'r').readlines()
        bot.train(data)

while True:
	message = input('you:')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot:',reply)
	if message.strip() == 'Bye':
		print('ChatBot : Bye')
		break
