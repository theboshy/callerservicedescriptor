from twilio.rest import Client

account_sid = "##"
auth_token = "##"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+573008914560",
   from_="+15152986078",
    url="https://github.com/theboshy/callerservicedescriptor/blob/master/descriptor/callresponse.xml"
)


#msg = client.messages.create(
 #   to="+573008914560",
  #   body="que ahce perro :U",
   # from_="+15152986078"
#)
 

print(call.sid)