import time
import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    interval = time.time() + 1

    # Simulates some CPU load.
    while time.time() < interval:
        x = 435344
        x * x
        x = x + random.randint(-12314, 10010)

    return 'Hello from the backend. Backend computed %d' % x
