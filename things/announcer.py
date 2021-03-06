import sys
import subprocess
import StringIO

from flask import Flask, request
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)

# Announcer
@app.route("/cmds/say")
def say():
    text = request.args.get('what', 'Error. You must specify WHAT to say using the "what" parameter')
    speed = request.args.get('speed', '175')
    voice = request.args.get('voice', 'spanish')
    amplitude = request.args.get('volume', '100')

    args = ['espeak', '-s', speed, '-v', voice, '-a', amplitude]
    process = subprocess.Popen(args, stdin=subprocess.PIPE, shell=False)
    process.stdin.write(text)
    process.communicate()[0]
    process.stdin.close()
    return "I said: '%s'" % (text,)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)


