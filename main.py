import hashlib

from flask import Flask, request

app = Flask(__name__)

def create_sha256_hash(value, iterations):
    for i in range(0, iterations):
        value = hashlib.sha256(value.encode()).hexdigest()

    return value

@app.route("/hash/<value>", methods=['GET'])
def root(value):
    return create_sha256_hash(value, 100_000) + ", your IP is: " + request.remote_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, threaded=True)
