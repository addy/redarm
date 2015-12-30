__author__ = 'x4nt'

from cat import getCatFacts
from time import sleep

class Messenger(object):

    def __init__(self, client, phone):
        self.client = client
        self.phone = phone
        self.messages = []

    def sendTexts(self, recipient):

        catFacts = getCatFacts(5)
        for fact in catFacts:
            self.messages.append(fact + " To end subscription, reply \"STOP\".")

        message = self.client.messages.create(
            body="Welcome to Cat Facts! Here's 5 complimentary facts.",
            to=recipient,
            from_=self.phone,
        )
        print message.sid
        print message.body
        sleep(10)

        for msg in self.messages:
            message = self.client.messages.create(
                body=msg,
                to=recipient,
                from_=self.phone,
            )
            print message.sid
            print message.body
            sleep(30)

        self.messages = []
