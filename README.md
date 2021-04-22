# TwitchSpam


### Features
* Follow bot.
* Spam reporting.
* Spam bot, that evades shadowbans with Tor.
* A command to stream a video to Twitch using one of the accounts.

It all works using the undocumented API Twitch internally uses.
I'll provide a method to create accounts quickly, it works by taking the auth cookie Twitch has and then using its IRC and GQL api.
You'll find a simple library for the spambot, along other things.


## Running on Linux:
```console
spammer@linux:TwitchSpam$ sudo apt-get install python3
spammer@linux:TwitchSpam$ sudo apt-get install tor
spammer@linux:TwitchSpam$ sudo apt-get install ffmpeg # Needed for encoding streams
spammer@linux:TwitchSpam$ pip3 install -r requirements.txt
spammer@linux:TwitchSpam$ python main.py
```

## Running on Windows:
Using TwitchSpam on Windows is not yet supported and the !stream command will not work.
Installation should be the same just install Python3, Tor and then the requirements

## Donating Accounts:

The JS code that is used with !donateoauth:

```JavaScript
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

var token = getCookie("auth-token")
console.log("\n\n\n\nCODE TO PASTE IN DISCORD:\n!donateoauth kimne78kx3ncx6brgo4mv6wki5h1ko:oauth:" + token + "\n\n\n\n")
```

Then do
```
!donateoauth {oauth}
```
