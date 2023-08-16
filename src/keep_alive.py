import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Bot Live" #Change this if you want

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port) #don't touch this

def keep_alive():
    server = Thread(target=run)
    server.start()
