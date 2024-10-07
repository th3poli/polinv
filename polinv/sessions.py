import cloudscraper

CHROME_VERSION = 128
USER_AGENT = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{CHROME_VERSION}.0.0.0 Safari/537.36'
#USER_AGENT_MOBILE = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{CHROME_VERSION}.0.0.0 Safari/537.36'

class Session(cloudscraper.CloudScraper):

    def __init__(self, profile: str, *args, **kwargs):

        self.profile = profile
        super().__init__(*args, **kwargs)

        self.headers.update({ 'User-Agent': USER_AGENT })
        self.headers.update({ 'Sec-Ch-Ua': f'"Not_A Brand";v="8", "Chromium";v="{CHROME_VERSION}", "Google Chrome";v="{CHROME_VERSION}"' })
        self.headers.update({ 'Sec-Ch-Ua-Mobile': '?0' })
        self.headers.update({ 'Sec-Ch-Ua-Platform': '"Windows"' })

    def info(self): return f'<Session profile={self.profile} />'
    def __str__(self): return self.info()
    def __repr__(self): return self.info()

def make_session(profile: str, *args, **kwargs): return Session(profile, *args, **kwargs)
