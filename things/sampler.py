import sys, os
import subprocess

from flask import Flask, request

app = Flask(__name__)

sample_dir = os.path.join(os.path.dirname(__file__), '../data/samples')

# Sampler
@app.route("/cmds/play")
def say():
    sample = request.args.get('sample', 'alarm.wav')
    volume = int(request.args.get('volume', '100'))*(65555.0/100)

    filepath = os.path.join(sample_dir, sample)

    args = ['paplay', '--volume', str(volume), filepath]
    process = subprocess.check_output(args, shell=False)
    return "I played: '%s'" % (filepath,)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)


