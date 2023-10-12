# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:42:20 2023

@author: JO
"""
import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from flask import Flask, render_template

#app = Flask(__name__, template_folder='templates')

bot = ChatBot("chatbot2", read_only=False, 
              
              logic_adapters=[
                  {
                  
                  "import_path":"chatterbot.logic.BestMatch",
                  "default_response":"Sorry, I dont have an answer",
                  "maximum_similarity_threshold": 0.9
                  
                  }])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

#@app.route("/")
#def main():
#    return render_template("index.html")

while True:

   user_response = input("User : ")
   print("Chatbot2 : " + str(bot.get_response(user_response)))
    
    
#if __name__=="__main__":
#   app.run(debug=True)