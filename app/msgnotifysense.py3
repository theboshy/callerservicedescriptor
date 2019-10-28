from twilio.rest import Client

#twillio configuration
account_sid = "##"  # SID by your twillio account 
auth_token = "##"   # authentication token in twillio account

#service configuration
to_call_number = ""   # number to call (+573007865467)
from_number = ""      # phone number provided by twillio to make your call

client = Client(account_sid, auth_token)

call = client.calls.create(
   to=to_call_number,
   from_=from_number,
   url="https://github.com/theboshy/callerservicedescriptor/blob/master/descriptor/callresponse.xml"
)


# msg = client.messages.create(
 #   to="**",
 #   body="que hace perro :U",
 #   from_="**"
# )
 

print(call.sid)
