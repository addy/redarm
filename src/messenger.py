__author__ = 'x4nt'

class Messenger(object):

    def __init__(self, client, phone):
        self.client = client
        self.phone = phone
        self.messages = []

    def sendText(self, recipient):
        msg = "Hello, World!"
        message = self.client.messages.create(
            body=msg,
            to=recipient,
            from_=self.phone,
        )
        print message.sid
