from flask import Flask, url_for

app = Flask(__name__)

@app.route('/get/text')
def get_text():
    return ("hello from Flask using an explicit Response Object")

@app.route('/welcome/about')
def about():
    return """
    <html>
    <head>
    <title>About me</Title>
    </head>
    <body>
    <h1>About Anita</h1>
    <p>Anita is a 27 year old doctor living in London. Her favourite activities include reading, listening to music and trying out new food places in London. </p>
    <hr>
    </body>
    </html>
    
    """

@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    url_2 = url_for('about')
    return"""
    <html>
    <head>
    <title>Sample - Flask Routes</Title>
    </head>
    <body>
    <h1>Name Page</h1>
    <p>Hello {}!</p>
    <p>You are {} years old. </p>
    <hr>
    <a href= '{}'>Welcome</a>
     <hr>
    <a href= '{}'>About</a>
    </body>
    </html>
    
    """.format(name, age, url, url_2)


if __name__ == '__main__':
    app.run(debug=True)