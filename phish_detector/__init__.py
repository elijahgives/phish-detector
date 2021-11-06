import hashlib
import requests

class PhishDetector:
    def __init__(self, agent: str = 'Mozilla/5.0 (Macintosh) AppleWebKit/533.1.6 (KHTML, like Gecko) Version/5.1 Safari/53.1.6'):
        """ Create a PhishDetector instance.
        ``agent``: optional, user agent to use when requesting hash list
        """
        self.hash_list: list = []
        self.agent = agent
        self.ready: bool = False
        self.fetch_list()

    def get_domain(self, url: str):
        return url.split('?')[0].split('#')[0].replace('http://', '').replace('https://', '').split('/')[0].lower()

    def fetch_list(self):
        r = requests.get('https://cdn.discordapp.com/bad-domains/hashes.json')
        if r.status_code == 200:
            self.hash_list = r.json()
            self.ready = True
        else:
            raise f'Error while fetching hash list, code: {r.status_code}'

    def check(self, url: str) -> bool:
        """
        Check if a URL is in Discord's phishing list.
        ``url``: the url to check, required.

        Returns ``True`` if it's malicious, and ``False`` if it's not.
        """
        if not self.ready:
            raise 'Tried to check a URL when detector was not ready.'

        return hashlib.sha256(self.get_domain(url).encode('utf-8')).hexdigest() in self.hash_list