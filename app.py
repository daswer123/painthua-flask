#parser
#python main.py --product_id 1001028

parser = argparse.ArgumentParser()
parser.add_argument('--product_id', dest='product_id', type=str, help='Add product_id')
args = parser.parse_args()

#app 
TEMPLATE = args.templates-folder
STATIC = args.static-folder

from flask import Flask, render_template
from flask_lt import run_with_lt

app = Flask(__name__,template_folder=TEMPLATE,static_folder=STATIC)
run_with_lt(app)

@app.route('/')

def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()


# !pip install Js2Py




