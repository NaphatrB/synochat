from flask import Flask, request

from synochat.webhooks import Bot

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
	token = 'C9zW2fCU2Zyzw3UPo72FP9viCqdHIStxKd0e6cLkLhf1GUo0Tve9TGFmki50b4wE'
	webhook = Bot(request.form, token, verbose=True)

	if not webhook.authenticate(token):
		return webhook.createResponse('Outgoing Webhook authentication failed: Token mismatch.')

	print(webhook)

	return webhook.createResponse('Pong')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug = True)