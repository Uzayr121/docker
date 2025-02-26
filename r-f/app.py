import os
from flask import Flask, render_template, jsonify
import redis # type: ignore

app = Flask(__name__)

redis_host = os.getenv ('REDIS_HOST', 'redis')
redis_port = int(os.getenv ('REDIS_PORT', '6379'))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/count')
def count():
    visits = r.incr('hits')
    return jsonify({'count': visits})

@app.route('/count-page')
def count_page():
    return render_template('count.html')
                

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)