import requests
import pandas as pd
import numpy as np


def requests_():
    r = requests.get('https://api.github.com/events')
    print(r.headers)


def pandas_(file):
    df = pd.read_csv(file)
    print(df.head(10))


def numry_():
    V = np.array([1, -2, 3, -4, 5])
    print(sum(V[V > 0]))


requests_()
pandas_('2019.csv')
numry_()
