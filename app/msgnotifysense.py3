from twilio.rest import Client

account_sid = "##"
auth_token = "##"
client = Client(account_sid, auth_token)

call = client.calls.create(
   to="*to_phone_number*",
   from_="*twillio_caller_number*",
   url="https://github.com/theboshy/callerservicedescriptor/blob/master/descriptor/callresponse.xml"
)


# msg = client.messages.create(
 #   to="**",
 #   body="que hace perro :U",
 #   from_="**"
# )
 

print(call.sid)
