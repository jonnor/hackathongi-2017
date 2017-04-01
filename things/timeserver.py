import datetime, sys

from flask import Flask, request
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

# Timeserver logic
@app.route("/cmds/timestamp")
def timestamp():
    now = datetime.datetime.now()
    epoch = datetime.datetime(1970,1,1)
    timestamp = ((now - epoch).total_seconds())
    s = str(int(timestamp))
    return s

@app.route("/cmds/formatted")
def formatted():
    now = datetime.datetime.now()
    formatting = request.args.get('format')
    if not formatting:
        formatting = "%Y-%m-%dT%H:%M:%S" # default to ISO 8601 
    return now.strftime(formatting)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)


