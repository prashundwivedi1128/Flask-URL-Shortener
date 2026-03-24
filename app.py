import sqlite3
import string
import random
# 1. Yahan 'render_template' hona chahiye
from flask import Flask, request, jsonify, redirect, render_template 

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS short_urls 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  original_url TEXT, 
                  short_code TEXT UNIQUE)''')
    conn.commit()
    conn.close()

init_db()

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# --- 2. YEH WALA ROUTE MISSING HAI (Isi se 404 hatagea) ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 3. Baaki routes (shorten aur redirect) neeche rehne do ---
@app.route('/shorten', methods=['POST'])
def shorten():
    # ... (tera purana shorten wala code)
    data = request.get_json()
    url = data.get('url')
    code = generate_short_code()
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO short_urls (original_url, short_code) VALUES (?, ?)", (url, code))
    conn.commit()
    conn.close()
    return jsonify({"shortUrl": f"http://127.0.0.1:5000/{code}"})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original_url FROM short_urls WHERE short_code = ?", (short_code,))
    row = c.fetchone()
    conn.close()
    if row:
        return redirect(row[0])
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)