# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:11:22 2023

@author: JO
"""
import time
time.clock = time.time
from chatterbot import ChatBot
bot=ChatBot("Mathbot", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

while True:
    user_text=input("Enter the mathematical equation : ")
    print("Mathbot :" + str(bot.get_response(user_text)))
