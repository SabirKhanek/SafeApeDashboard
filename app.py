from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST', 'GET'])
def getquery():
    wallet_address = request.form['address']
    print(wallet_address)
    return render_template("index.html", Address= wallet_address, Dividends= "10000 BNB", Unlock_time="13:10 UTC")

if __name__ == "__main__":
    app.run()
