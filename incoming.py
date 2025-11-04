from synochat.webhooks import IncomingWebhook

token = "C9zW2fCU2Zyzw3UPo72FP9viCqdHIStxKd0e6cLkLhf1GUo0Tve9TGFmki50b4wE"
webhook = IncomingWebhook('example.com', token)

webhook.send('This text is sent to Synology Chat.')