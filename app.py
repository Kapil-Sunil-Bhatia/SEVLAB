from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user = request.form['user']
    web_server = request.form['web_server']
    web_app = request.form['web_app']
    mysql = request.form['mysql']
    app_server = request.form['app_server']
    app = request.form['app']
    internet = request.form['internet']

    plantuml_code = f'''
@startuml
actor {user}
node "{web_server}" {{
  rectangle {web_app}
  database {mysql}
}}

node "{app_server}" {{
  rectangle {app}
}}

cloud {internet}

{user} --> {web_app} : Requests
{web_app} --> {mysql} : Queries
{web_app} --> {app} : RPC
{user} --> {internet} : Browsing
{internet} --> {web_app} : HTTP
{internet} --> {app} : RPC
@enduml
'''

    return render_template('index.html', plantuml_code=plantuml_code)

if __name__ == '__main__':
    app.run(debug=True)
