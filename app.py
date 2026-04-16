from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Fun cosmic generation data
PREFIXES = ["Zor", "Gor", "Xan", "Vex", "Quar", "Lum", "Nyx", "Dra", "Zeph", "Vyn"]
SUFFIXES = ["thon", "pia", "prime", "x", "ium", "oria", "tar", "lus", "ia", "tron"]
TRAITS = [
    "Rains liquid diamonds every Tuesday.",
    "Inhabited strictly by sentient clouds.",
    "Has three purple suns that hum softly.",
    "Gravity reverses during an eclipse.",
    "Entirely made of bouncy castle material.",
    "The native language is interpretative dance.",
    "Oceans are made of carbonated grape soda.",
    "Every rock vibrates with lo-fi beats..."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    name = random.choice(PREFIXES) + random.choice(SUFFIXES)
    trait = random.choice(TRAITS)
    return jsonify({"name": name.capitalize(), "trait": trait})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
