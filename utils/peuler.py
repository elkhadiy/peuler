import requests as rq
import requests_cache
from IPython.display import display, HTML

requests_cache.install_cache()

phtml = lambda i: f'https://projecteuler.net/minimal={i}'

def problem(i):
    display(HTML(f'<h1>Problem {i}</h1>'))
    display(HTML(rq.get(phtml(i)).text))