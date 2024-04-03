
from requests import get
from random import sample
from time import sleep

url = 'https://teste-prometheus-09dad054d275.herokuapp.com/'

while True:
    for i in ['', 'naruto', 'busca-cep?cep=70852500', 'busca-cep?cep=65215000']:
        req = get(url + i)
        sleep(
        sample([2, 5], 1)[0]
    )
