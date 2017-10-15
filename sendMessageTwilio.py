from twilio.rest import Client

account_sid = "AC09957f78a8f3a5d5ba46580e14570f37"
auth_token = "6cc9372ff82ae11f1120bb9ad7a443b6"
client = Client(account_sid, auth_token)

phones = ["+12016831645", "+16625181320"]

for phone in phones:
    message = client.messages.create(
        to=phone,
        body="Hi! Here is the list of volunteer info for you.",
        from_="+16625461917"
    )

