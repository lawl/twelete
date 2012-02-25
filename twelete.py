import os
import tweepy

class Twelete:
    _api=None;
    _auth=None;

    def __init__(self):
        config=self.get_config()
        self._auth=tweepy.OAuthHandler(config['consumer_key'],config['consumer_secret'])
        self._auth.set_access_token(config['access_token'],config['access_token_secret'])
        self._api=tweepy.API(self._auth)
        print self.wipe_pages(3)

    def wipe_pages(self,pages):
        for cpage in range(2,pages+2):
            statuses=self._api.user_timeline(page=cpage,include_rts=1)
            for item in statuses:
                print "DELETING: ",item.text
                try:
                    self._api.destroy_status(item.id)
                except Exception:
                    pass

    def get_config(self):
        configtable={}
        config = open(os.getenv('HOME')+'/.config/twelete/config','r')
        for line in config.readlines():
            tmp=line.split("=")
            if len(tmp)==2:
                configtable[tmp[0]]=tmp[1].rstrip()
        return configtable

if __name__=='__main__':
    t=Twelete()
