import socket
import socks
import random
import spintax.spintax
import logger

class Bot:
    def __init__(self,channel):
       self.channel = channel.lower() # convert to lowercase for the IRC standard
       self.socks = []
    
    def StartSock(self,oauthtoken,proxyip=None,proxyport=1080):
        try:
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
            return s
        except:
            # TODO adhere to config.ini 
            accounts = open("oauthlist.txt").read().split("\n")
            _token = random.choice(accounts)
            return self.StartSock(_token,proxyip,proxyport)
        
        return 0

    def SendMessage(self,message,account=None):
        message = "PRIVMSG #{0} :{1}\r\n".format(self.channel,message)
        if(account):
            s = self.socks[account]
            try:
                s.send(message.encode())
            except:
                pass
        else:
            for s in self.socks:
                try:
                    s.send(spintax.spintax.spin(message).encode())
                except:
                    pass   
            
    def CreateBots(self,amount,accountlist,proxyip=None,proxyport=1080):
        if(proxyip):
            print("Using proxy {0} on port {1}".format(proxyip,proxyport))
            logger.log("Using proxy {0} on port {1}".format(proxyip,proxyport))
        # Check if user is using Tor
        # Instead of checking the port we should just have a value that specifies it
        if(proxyport == 9050):
            import os
            import time
            import platform
            # Get a new IP from tor by restarting it
            if platform.system() == "Darwin":
                os.system("brew services restart tor")
            else:
                try:
                    os.system("/usr/sbin/service tor restart")
                except:
                    os.system("systemctl restart tor")

            time.sleep(.5)
        accounts = open(accountlist).read().strip().split("\n")
        
        logger.log(f"Connecting with {amount} bots")
        for i in range(amount):
            line = random.choice(accounts)
            _token = 'oauth:' + line.split(":")[2]
            print(_token)
            self.socks.append(self.StartSock(_token,proxyip,proxyport))
            accounts.pop(accounts.index(line))
