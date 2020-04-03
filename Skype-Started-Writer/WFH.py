import datetime, time, random
from skpy import Skype, SkypeChats, SkypeAuthException
from getpass import getpass

rand = random.randrange(30,45)
alarm = datetime.time(9,rand,10)
print(alarm)
while alarm> datetime.datetime.now().time():	
	print(datetime.datetime.now())
	time.sleep(120) #Checks time after every 2 minutes
skypeLogin = Skype(connect=False)
skypeLogin.conn.setTokenFile("tokens")
try:
    skypeLogin.conn.readToken()
except SkypeAuthException:
    skypeLogin.conn.setUserPwd("meaxaymishra@gmail.com",getpass()) #Enter Skype Email in code here and password on prompt screen. It'll generate a token.
    skypeLogin.conn.getSkypeToken()
    skypeLogin.conn.writeToken()
#print(skypeLogin.user)  -- Prints Logged in Skype User Details
skypeLogin.contacts
skypeChat = SkypeChats(skypeLogin)
#print(skypeChat.recent())  --Prints recent chat to get Chat ID
#rInfo=skypeLogin.chats["8:live:meakshaymishra"]
rInfo=skypeLogin.chats[{Enter ID of Chat you can use print recent to get id of chat}]
rInfo.sendMsg("Started!") #Sends Message in group
print("Message Published!")
