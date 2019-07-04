import csv
import random
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
#import os

app = Flask(__name__)

def rand():
    with open(r'truisms.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    return(chosen_row)

# Find these values at https://twilio.com/user/account
twilio_host='0.0.0.0'
twilio_port = 80
client = Client(account_sid, auth_token)


@app.route("/", methods=['POST','GET'])
def send_wisdom():
    message = client.messages.create(
        to='+13034085934',
        from_='+17206057729',
        body=rand()
       )
    return '', 200

        #body=request.headers
if __name__ == "__main__":
    app.run(host=twilio_host, port=twilio_port)
