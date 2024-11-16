from flask import Flask
from flask import request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    return html
@app.route('/url', methods=['POST'])
def submit():
    html=''
    with open('index.html',"r",encoding="utf-8") as f:
        html = f.read()
    submit = request.form.get('url')
    path=f'{submit}.txt'
    with open( path,'w',encoding="utf-8") as f:
        pass
    with open( path,'a',encoding="utf-8") as f:
        f.write('welcome'+'\n')
    return  html.replace('<out/>',f'https://publicchat-9i7r.onrender.com/{path}')

@app.route('/<string:filen>', methods=['GET','POST'])
def do(filen):
    html=''
    chatout=''
    with open('chat.html',"r",encoding="utf-8") as f:
        html = f.read()
    if request.method == 'POST':
        now=str(datetime.datetime.utcnow())
        username=request.form.get('username')
        input=request.form.get('input')
        #print(input)
        with open(filen, "a", encoding="utf-8") as f:
                    f.write(now+username+'--'+input+'\n')
    with open(filen,"r",encoding="utf-8") as f:
        chatout=f.read()
    chatout = chatout.replace("\n", "<br>")
    return  html.replace('<out/>',chatout)

app.run(debug=True, host='0.0.0.0')
