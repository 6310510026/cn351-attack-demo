from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/claim_reward')
def claim_reward():
    # Execute the provided Python script
    subprocess.run(['python', 'Add.py'])
    return 'Reward claimed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
