
import configparser
config = configparser.ConfigParser()
config.read('example.ini')

token = config['DEFAULT']['Token']
oauthsfile = config['DEFAULT']['OAuthFile']
streamoauthsfile = config['DEFAULT']['StreamOAuths']