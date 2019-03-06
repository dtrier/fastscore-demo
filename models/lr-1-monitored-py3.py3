# fastscore.schema.0: close_price

import numpy as np
import pickle
import time
from sklearn.linear_model import LinearRegression
import random

def begin():
    global lr
    global window, window_size
    window = []
    window_size = 15
    with open('lr_pickle1.pkl', 'rb') as f:
        lr = pickle.load(f)

def action(x):
    global window, window_size
    x = x['Close']
    actual = x*random.uniform(0,1.5)
    window = window[1-window_size:] + [x]
    if len(window) < window_size:
        yield {"name": "price", "value":x, "monitor":actual}
    else:
        X = np.array([window])
        y = lr.predict(X)
        yield {"name":"price", "predicted": y[0,0],"actual":actual}

