import json
from flask import Flask, render_template

# Load config information from JSON file if available
try:
    with open('config.json') as f:
        config = json.load(f)
except:
    pass

app = Flask(__name__)
app.secret_key = config['secret_key']


# Endpoint for main dashboard
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

