# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 19:34:20 2016

@author: Geetha Yedida
"""

from twilio.rest import TwilioRestClient

account_sid = "AC79aae9a8a786618b794aa8dba2442d37"
auth_token = "f1ec20abcbfd3ccfae9d20360fa110ea"
client = TwilioRestClient(account_sid,auth_token)

message = client.sms.messages.create(
    body = "Hi welcome to 2b part of course ",
    to="+14094660491",
    from_="+1 4092418334")
print message.sid