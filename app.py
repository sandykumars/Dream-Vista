from flask import Flask, render_template, request, redirect, url_for, flash
from dreamvista import DreamVista  # make sure dreamvista.py exists in same folder

app = Flask(__name__)
app.secret_key = "dream_vista_secret"
dream_app = DreamVista()


@app.route('/')
def home():
    # show the home page (interpret UI)
    return render_template('index.html')


@app.route('/interpret', methods=['POST'])
def interpret():
    dream_text = request.form.get('dream', '')
    if dream_text.strip() == '':
        flash("Please describe your dream!", "warning")
        return redirect(url_for('home'))
    results = dream_app.analyze_dream(dream_text)
    # re-render index with results and previous dream text
    return render_template('index.html', results=results, dream_text=dream_text)


@app.route('/add-symbol', methods=['GET', 'POST'])
def add_symbol():
    if request.method == 'POST':
        symbol = request.form.get('symbol', '').strip()
        meaning = request.form.get('meaning', '').strip()
        tone = request.form.get('tone', '').strip()
        category = request.form.get('category', '').strip()
        keywords = request.form.get('keywords', '').strip()
        if not symbol or not meaning:
            flash("Symbol name and meaning are required.", "warning")
            return redirect(url_for('add_symbol'))

        success = dream_app.add_custom_symbol(symbol, meaning, tone, category, keywords)
        if success:
            flash(f"Symbol '{symbol}' added successfully!", "success")
        else:
            flash(f"Failed to add symbol '{symbol}'. It may already exist.", "danger")
        return redirect(url_for('add_symbol'))

    return render_template('add_symbol.html')


@app.route('/stats')
def stats():
    data = dream_app.get_dream_statistics() or {}
    # ensure keys exist to avoid template errors
    data.setdefault('total_dreams', 0)
    data.setdefault('common_symbols', [])
    data.setdefault('emotional_tones', [])
    return render_template('stats.html', stats=data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    dreams = None
    symbol = ''
    if request.method == 'POST':
        symbol = request.form.get('symbol', '').strip()
        if symbol:
            dreams = dream_app.search_dreams_by_symbol(symbol)
        else:
            flash("Please enter a symbol to search.", "warning")
            return redirect(url_for('search'))
    return render_template('search.html', dreams=dreams, symbol=symbol)


if __name__ == '__main__':
    app.run(debug=True)
