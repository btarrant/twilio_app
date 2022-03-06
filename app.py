from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="689-610-0627",
    from_="+19362263399",
    body="This is our first message"
)
