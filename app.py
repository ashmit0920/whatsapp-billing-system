from flask import Flask, request, render_template
from twilio.rest import Client
import os
from dotenv import load_dotenv
from main import send_message

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    number = request.form['phone_number']
    item = request.form['item']
    amount = request.form['amount']

    # if number and item and amount:
    #     success = True
    #     failed = False
    # else:
    #     success = False
    #     failed = True
    
    try:
        send_message(number, amount, item)
        success = True
        failed = False
    except:
        success = False
        failed = True

    return render_template('index.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)