
from twilio.rest import Client




# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
def dangerhandler():
    userFile = open('userlog.txt', 'r')
    str username = "Anish"
    i = userFile.readlines()
    userFile.close()
    call = [i[2], i[3], i[4]]      #BE CAREFUL  WHEN  YOU  CALL
    for i in call:
        account_sid = 'AC97ea76540cf38637f7f427e485b6e0b2'
        auth_token = 'f4e80c9beadd90fb402847f8014579b8'
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            twiml="<Response><Say>EMERGENCY  EMERGENCY !! LISTEN CAREFULLY !!  YOUR  RELATIVE     '{}'     ISsss  IN  DANGER.  I REPEAT   YOUR  RELATIVE      '{}'      IS  IN  DANGER .THIS  IS  AUTOMATED  FROM  SECUREZ</Say></Response>".format(username, username),
            to=i,
            from_='+12056714715'
        )
        message = client.messages.create(
            body="EMERGENCY !!Your relative {} have reported  that he/she  is in danger.This is from Securez. ".format(username),
            from_='+12056714715',
            to=i


        )
        print(call.sid)
        print(message.sid)



