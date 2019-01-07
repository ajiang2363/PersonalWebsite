from flask import Flask

web = Flask (__name__)

@web.route("/")

def home():
    return "This is the home menu"

if __name__ == '__main__':
    web.run(debug=True)
