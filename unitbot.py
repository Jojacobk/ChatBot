# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:52:30 2023

@author: JO
"""

from chatterbot import ChatBot
bot=ChatBot("UnitBot", logic_adapters=["chatterbot.logic.UnitConversion"])

while True:
    user_text=input("Enter the input :")
    chatbot_response=str(bot.get_response(user_text))
    print(chatbot_response)