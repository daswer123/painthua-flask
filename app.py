# Install libraries
import subprocess
import sys
import argparse

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("flask")
install("flask-localtunnel")

# Import libraries
from flask import Flask, render_template
from flask_lt import run_with_lt

# Create an ArgumentParser
parser = argparse.ArgumentParser(description='Run Flask app with optional port argument.')
# Add a port argument
parser.add_argument('--listen-port', type=int, default=5000, help='Port number to listen on')
# Parse the command-line arguments
args = parser.parse_args()

# Create the Flask app
app = Flask(__name__)
run_with_lt(app)

@app.route('/')
def home():
    return render_template('index-non-colab.html')

if __name__ == '__main__':
    # Use the port specified in the command-line arguments, or the default (5000)
    app.run(port=args.listen_port)
