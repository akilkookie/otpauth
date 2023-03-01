import random
from flask import Flask , render_template, request, session
from twilio.rest import Client
app = Flask(__name__)
app.secret_key = 'otp'
@app.route('/')
def home():
    return render_template('log.html')

@app.route('/getotp',methods = ['POST'])
def getotp():

    number = request.form['number']
    val = getotpapi(number)
    if val:
       return render_template('enterotp.html')

@app.route('/validateotp',methods = ['POST'])
def validateotp():
    otp = request.form['otp']
    if 'response' in session:
        s = session['response']
        session.pop('response',None)
        if s == otp:
            return 'You are authorized'
        else:
            return ' you are not authorized'
def generateOTP():
    return random.randrange(100000,999999)

def getotpapi(number):
    account_sid = 'AC055f4a459d19c5fa777a6042e7618a7b'
    auth_token = '2113a6ae1ac783c1d40bc9b99951cdc9'
    client = Client(account_sid, auth_token)
    otp = generateOTP()
    session['response'] = str(otp)
    body = 'your otp is ' + str(otp)
    message = client.messages.create(from_='+12764441710', body=body,
        to=number

    )

    if message.sid:
        return True
    else:
        return False



if __name__ == '__main__':
    app.run(port=5300, debug=True)