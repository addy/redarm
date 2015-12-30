__author__ = 'x4nt'

from os import getenv
from sys import exit, argv
from twilio.rest import TwilioRestClient
from messenger import Messenger

ACCOUNT_SID = getenv('TWILIO_SID')
AUTH_TOKEN = getenv('TWILIO_TOKEN')
PHONE_NUMBER = getenv('TWILIO_PHONE')
if ACCOUNT_SID == None: exit('TWILIO_SID environment variable not set.')
if AUTH_TOKEN == None: exit('TWILIO_TOKEN environment variable not set.')
if PHONE_NUMBER == None: exit('TWILIO_PHONE environment variable not set.')

# Receiver phone number should be passed as a CL argument.
if len(argv) > 1: recipient = argv[1]

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
messenger = Messenger(client, PHONE_NUMBER)
messenger.sendTexts(recipient)
