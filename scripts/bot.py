import socket
import socks
import random

class Bot:
    def __init__(self,channel):
       self.channel = channel.lower() # convert to lowercase for the IRC standard
       self.socks = []
    
    def StartSock(self,oauthtoken,proxyip=None,proxyport=1080):
        print("Creating sock")
        s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
        if(proxyip):
            s.set_proxy(socks.SOCKS5,proxyip,proxyport)

        s.connect(("irc.chat.twitch.tv" , 6667))
        s.send("PASS {}\r\n".format(oauthtoken).encode())
        s.send("NICK lolsecurity\r\n".encode())
        join = "JOIN #" + self.channel + "\r\n"
        s.send(join.encode())
        #message = "PRIVMSG #" + channel + " :fuck you\r\n"
        #s.send(message.encode())
        #print(s.recv(2048))
        return s

    def SendMessage(self,message,account=None):
        message = "PRIVMSG #{0} :{1}\r\n".format(self.channel,message)
        if(account):
            s = self.socks[account]
            s.send(message.encode())
        else:
            for s in self.socks:
                try:
                    s.send(message.encode())
                except:
                    pass   
            
    def CreateBots(self,amount,accountlist,proxyip=None,proxyport=1080):
        if(proxyip):
            print("Using proxy {0} on port {1}".format(proxyip,proxyport))
        # Check if user is using Tor
        if(proxyport == 9050):
            import os
            import time
            import platform
            if platform.system() == "Darwin":
                os.system("brew services restart tor")
            else:
                os.system("service tor restart")
            time.sleep(.5)
            try:
                nymsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                nymsock.connect(("127.0.0.1",9050))
                nymsock.send("AUTHENTICATE \"password\"\r\nSIGNAL NEWNYM\r\n".encode())
                nymsock.close()
            except:
                pass
        accounts = open(accountlist).read().split("\n")
        
        for i in range(amount):
            self.socks.append(self.StartSock(random.choice(accounts),proxyip,proxyport))
