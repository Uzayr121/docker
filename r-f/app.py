import os
from flask import Flask
import redis # type: ignore

app = Flask(__name__)

redis_host = os.getenv ('REDIS_HOST', 'redis')
redis_port = int(os.getenv ('REDIS_PORT', '6379'))
r= redis.Redis(host=redis_host, port=redis_port)
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/count')
def count():
    visits=r.incr('hits')
    return "Number of hits: {}".format(visits)

#return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)