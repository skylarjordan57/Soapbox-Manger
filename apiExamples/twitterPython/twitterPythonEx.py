import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

cfg = {"consumer_key"        : "",
       "consumer_secret"     : "",
       "access_token"        : "",
       "access_token_secret" : ""}

api = get_api(cfg)
tweet = "Testing Testing Testing"
status = api.update_with_media('NASA_logo.png',tweet)

test = api.home_timeline()
print('IDs are:')
idList = [skytweet.text for skytweet in test]
print(test)
print(idList[0])
