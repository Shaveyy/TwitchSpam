# TwitchSpam

* Follow bot. (Broken as of new Twitch API Update)
* Spam reporting. (Broken as of new Twitch API Update)
* Spam bot, that evades shadowbans with Tor.
* A command to stream a video to Twitch using one of the accounts. (Broken as of new Twitch API Update)

It all works using the undocumented API Twitch internally uses.
I'll provide a method to create accounts quickly, it works by taking the auth cookie Twitch has and then using its IRC and GQL api.
You'll find a simple library for the spambot, along other things.


## Using it on Linux:
```console
spammer@linux:TwitchSpam$ sudo apt-get install python3
spammer@linux:TwitchSpam$ sudo apt-get install tor
spammer@linux:TwitchSpam$ sudo apt-get install ffmpeg # Needed for encoding streams
spammer@linux:TwitchSpam$ pip3 install -r requirements.txt
spammer@linux:TwitchSpam$ python main.py
```

## Why is everything broken?
Twitch has updated their public API (not the GQL one) to require Client IDs to be from the same holder as OAuth Tokens. Due to this a majority of the features we use have been completly broken. Fixing should be as easy as replacing ALL Twitch public API calls with their GQL API.

- [ ] Fix followbot
- [ ] Fix spambot
- [ ] Fix stream bot

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
console.log("\n\n\n\nCODE TO PASTE IN DISCORD:\n!donateoauth oauth:" + token + "\n\n\n\n")
```

Then do
```
!donateoauth {oauth}
```
