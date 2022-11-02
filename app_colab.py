#Install libraries
#import subprocess
#import sys

#def install(package):
#   subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("flask")
#install("flask-localtunnel")

#app
from flask import Flask, render_template
#from flask_lt import run_with_lt

app = Flask(__name__)
#run_with_lt(app)

@app.route('/')

def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()