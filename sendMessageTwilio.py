from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

phones = ["+12016831645", "+16625181320"]

for phone in phones:
    message = client.messages.create(
        to=phone,
        body="Hi! Here is the list of volunteer info for you.",
        from_="+16625461917"
    )

