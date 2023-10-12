# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:03:27 2023

@author: JO
"""

import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot1", read_only=False, 
              
              logic_adapters=[
                  {
                  
                  "import_path":"chatterbot.logic.BestMatch",
                  "default_response":"Sorry, I dont have an answer",
                  "maximum_similarity_threshold": 0.9
                  
                  }])

list_to_train = [
    "Hi",
    "Hello there",
    "Whats your name",
    "Chatbot1",
    "How are you",
    "I am fine thank you"
]

list_to_train2 = [
    "Hi",
    "Hi, How can i help you?",
    "Whats your name",
    "My name is Chatbot1",
    "How are you",
    "I am doing well, thank you"
]
    
list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)
list_trainer.train(list_to_train2)

while True:

    user_response = input("User : ")
    print("Chatbot1 : " + str(bot.get_response(user_response)))