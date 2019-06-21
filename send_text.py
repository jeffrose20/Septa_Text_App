from twilio.rest import Client

account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
from_number = '+12675551234'
to_number = '+15555551234'


def send_text(message):
    assert type(message) == str
    client = Client(account_sid, auth_token)

    message_output = client.messages.create(body=message,
                                            from_=from_number,
                                            to=to_number)
