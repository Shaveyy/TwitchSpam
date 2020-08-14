# TwitchSpam

* Follow bot
* Spam reporting 
* Spam bot
* and a command to stream a video using one of the accounts (pretty sure its the same method the one of dudes who spammed the Artifact section did)

It all works using the undocumented API Twitch internally uses.
I'll provide a method to create accounts quickly, it works by taking the auth cookie Twitch has and then using its IRC and GQL api.
You'll find a simple library for the spambot and all the other things. I'd recommend using something that Windows Subsystem for Linux or just getting a Linux box.
We also use Tor to evade shadowbans

WSL is installable by the Windows store I'd recommend getting Ubuntu

## Using it on WSL or Linux:
```Bash
sudo apt-get install python3
sudo apt-get install tor
pip3 install -r requirements.txt
python main.py
```

## Donating Accounts:

The JS code that is used with !donateoauth:

```JavaScript
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

var token = getCookie("auth-token")
console.log("\n")
console.log("\n")
console.log("CODE TO PASTE IN DISCORD:")
console.log("\n")
console.log("!donateoauth oauth:" + token)
console.log("\n")
console.log("\n")
```

Then do
```
!donateoauth {oauth}
```